#!/usr/bin/python3.7

import socket
from .dancing_rainbow_led import main

HOST = ''
PORT = 1339

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    while True:
        conn, addr = server.accept()
        print('connected')
        with conn:
            print(addr)
            data = conn.recv(1024).decode()
            if data == 'goal':
                print('GOAL!')
                main()
