from livereload import Server, shell

transpile = '.venv/bin/python3 compile.py < main.py > main_compiled.py && .venv/bin/python3 -m transcrypt -b -p .none -n main_compiled.py'

if __name__ == '__main__':
    server = Server()
    server.watch('main.py', shell(transpile))
    server.watch('hydrate/demo.css')
    server.watch('hydrate/index.html')
    server.serve(root='hydrate')
