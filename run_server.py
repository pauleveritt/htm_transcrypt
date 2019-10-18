import subprocess
from inspect import getfile
from pathlib import Path

from livereload import Server

from compile import compile


def main_watcher():
    currdir = Path(getfile(compile)).parent
    transcrypt_command = currdir / '.venv' / 'bin' / 'transcrypt'
    t = f'{transcrypt_command} -b -m -n {currdir}/main_compiled.py'
    with open('main.py') as main_py:
        with open(f'{currdir}/main_compiled.py', 'w') as main_compiled:
            # Stage 1 from Joachim
            compiled = compile(main_py.read())
            main_compiled.write(compiled)
            main_compiled.close()

            # Stage 2: Transcrypt
            subprocess.call(t, shell=True, cwd=currdir)


if __name__ == '__main__':
    server = Server()
    server.watch('main.py', func=main_watcher)
    server.watch('index.html')
    server.serve()
