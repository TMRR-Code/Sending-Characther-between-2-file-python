# -*- coding: utf-8 -*-
"""client

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TilCKyOxuU4imPq-gCKHXfo1Pk8bfB2k
"""

import socket

host = socket.gethostname()
port = 12345

def send_message(message):
    s = socket.socket()
    s.connect((host, port))
    s.sendall(message.encode())
    data = s.recv(1024)
    s.close()
    return data.decode()

while True:
    message = input("Masukkan pesan: ")
    if message.lower() == 'exit':
        break
    response = send_message(message)
    print("Server:", response)

# import socket
# host = socket.gethostname()
# port = 12345
# s = socket.socket()
# s.connect((host, port))
# s.sendall(b'Halo nama Saya TMRR!')
# data = s.recv(1024)
# s.close()
# print(repr(data))
