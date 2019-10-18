import ast
import subprocess

import astor
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


def main():
    currdir = '/Users/pauleveritt/projects/scratchpad/htm_transcrypt'
    p = f'{currdir}/.venv/bin/python'
    t = f'{currdir}/.venv/bin/transcrypt -b -m -n {currdir}/main_compiled.py'
    args = f'-b -m -n {currdir}/main_compiled.py'
    with open('main.py') as main_py:
        with open(f'{currdir}/main_compiled.py', 'w') as main_compiled:
            # Stage 1 from Joachim
            compiled = compile(main_py.read())
            main_compiled.write(compiled)
            main_compiled.close()

            # Stage 2: Transcrypt
            subprocess.call(t, shell=True, cwd=currdir)
