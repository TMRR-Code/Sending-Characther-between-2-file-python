#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket

# Inisialisasi socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Aktifkan opsi broadcast
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind ke semua alamat IP dan port tertentu
client_socket.bind(('0.0.0.0', 12345))

# Dengarkan pesan broadcast
while True:
    data, address = client_socket.recvfrom(1024)
    print("Pesan dari", address, ":", data.decode())

# Tutup socket
client_socket.close()
