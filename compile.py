import ast
import astor
import pathlib
from tagged import split


class Rewrite(ast.NodeTransformer):
    def visit_Call(self, node):
        self.generic_visit(node)

        if node.func.__class__.__name__ != "Name" or node.func.id != "html":
            return node
        if len(node.args) != 1 or node.args[0].__class__.__name__ != "Str":
            return node

        strings, exprs = split(node.args[0].s)

        func_node = ast.Attribute(value=node.func, attr="func", ctx=ast.Load())
        strings_node = ast.Tuple(elts=[ast.Str(s=s)
                                       for s in strings], ctx=ast.Load())
        exprs_node = ast.Tuple(elts=[ast.parse(expr, mode="eval")
                                     for expr in exprs], ctx=ast.Load())
        new_node = ast.Call(func=func_node, args=[
            strings_node, exprs_node], keywords=[])
        return ast.copy_location(new_node, node)


def compile(source):
    root = ast.parse(source)
    root = Rewrite().visit(root)
    return astor.to_source(root)


if __name__ == "__main__":
    import sys

    sys.stdout.write(compile(sys.stdin.read()))
