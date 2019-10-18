from livereload import Server

from compile import main

if __name__ == '__main__':
    server = Server()
    server.watch(
        'main.py',
        func=main
    )
    server.watch('index.html')
    server.serve()
