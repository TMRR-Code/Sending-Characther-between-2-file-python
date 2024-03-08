#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat IP server dan port tertentu
server_socket.bind(('192.168.43.209', 12345))

# Listen koneksi masuk
server_socket.listen(5)

print("Server berjalan. Menunggu koneksi...")

# Terima koneksi dari client
client_socket, address = server_socket.accept()
print(f"Terhubung dengan {address}")

# Terima pesan dari client dan kirim balik
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Pesan dari client:", data.decode())
    client_socket.sendall(data)

# Tutup koneksi
client_socket.close()
server_socket.close()



