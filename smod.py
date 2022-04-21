import os

def server_command(com,cli_sock,file_name=""):
	if com == "list":
		while True:
		# Then, read data from user and send to client
			bytes_sent = send_listening(cli_sock)
			if bytes_sent == 0:
				print("User-requested exit.")
				break
	elif com == "put":
		file_name = cli_sock.recv(2000).decode()
		if os.path.exists(file_name) == True:
			print("This file already exists on the server")
		else:
			recv_file(cli_sock,file_name)
	elif com == "get":
		file_name = cli_sock.recv(2000).decode()
		send_file(cli_sock,file_name)





def send_file(cli_sock, file_name):
	#Read up to 1048576 bytes at a time;
	BUFFER_SIZE = 1048576
	with open(file_name, "rb") as file:
		while True:
			bytes_read = file.read(BUFFER_SIZE)
			#if there is no more to read from file then break the loop
			if not bytes_read:
				break
			#send data through socket
			cli_sock.sendall(bytes_read)
	print("File Transfer Complete.")

def recv_file(cli_sock, file_name):
	# Read up to 1048576 bytes at a time;
	BUFFER_SIZE = 1048576
	with open(file_name, "wb") as file:
		while True:
			bytes_read = cli_sock.recv(BUFFER_SIZE)
			# if no more data in the file exit the loop
			if not bytes_read:
				break
			# make a new file and write in it received data
			file.write(bytes_read)
	print("File transfer Complete.")


def send_listening(socket):
	path = os.listdir("./")
	path = str(path)
	path = path.encode()
	socket.send(path)
	return 0


def recv_listening(socket):
	data = socket.recv(4096)
	data = data.decode('utf-8')
	return data


