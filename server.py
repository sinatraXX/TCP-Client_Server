#!/usr/bin/env python3

''' Source code ini menggunakan referensi dari https://realpython.com/python-sockets/
dan https://medium.com/python-pandemonium/python-socket-communication-e10b39225a4c '''

import socket

#Mendeklarasikan host dan port number (local)
HOST = '127.0.0.1'
PORT = 54321
SERVER_ADDRESS = (HOST, PORT)

#Membuat socket TCP/IP untuk Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	#Menyambungkan port yang sudah dideklarasikan sebelumnya ke socket yang baru kita buat
	print('Memulai koneksi pada {} di port {}'.format(*SERVER_ADDRESS))
	s.bind(SERVER_ADDRESS)

	#Mencari incoming connections
	s.listen()

	#Proses penerimaan dan pengiriman respons pesan
	while True:

		#Menunggu koneksi
		print('menunggu koneksi...')
		connection, client_address = s.accept()

		try:
			print('mendapatkan koneksi dari ', client_address)

			#Menerima pesan dalam potongan 16 bit dan melakukan retransmisi
			while True:
				message = connection.recv(16)
				print('menerima {!r}'.format(message))

				if message:
					print('mengirimkan kembali pesan kepada client..')
					connection.sendall(message)
				else:
					print('tidak ada pesan dari', client_address)
					break

		finally:
			#Memberhentikan koneksi
			print('Koneksi selesai.')