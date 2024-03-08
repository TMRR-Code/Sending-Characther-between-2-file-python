#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server dengan IP dan port tertentu
client_socket.connect(('192.168.43.209', 12345))

# Kirim pesan ke server
while True:
    message = input("Masukkan pesan: ")
    client_socket.sendall(message.encode())
    if message.lower() == 'exit':
        break
    data = client_socket.recv(1024)
    print("Pesan dari server:", data.decode())

# Tutup koneksi
client_socket.close()
