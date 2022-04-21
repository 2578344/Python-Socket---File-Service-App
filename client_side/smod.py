import os

def client_command(com,cli_sock,file_name=""):
		if com == "list":
			#send command to server
			st = 'list'
			byt = st.encode()
			cli_sock.send(byt)

			data = recv_listening(cli_sock)
			print(data)
		elif com == "put":
			#send command to server
			st = 'put'
			byt = st.encode()
			cli_sock.send(byt)

			#request name of a file
			file_name = input("File Name:")
			#send file_name to the server
			cli_sock.send(file_name.encode())

			send_file(cli_sock,file_name)
		elif com == "get":
			#send command to server
			st = 'get'
			byt = st.encode()
			cli_sock.send(byt)

			#request name of a file
			file_name = input("File Name:")
			#send file_name to the server
			cli_sock.send(file_name.encode())

			recv_file(cli_sock,file_name)





def send_file(cli_sock, file_name):
	# Read up to 1048576 bytes at a time;
	BUFFER_SIZE = 1048576
	with open(file_name, "rb") as file:
		while True:
			bytes_read = file.read(BUFFER_SIZE)
			#if there is no more to read from file then exit the loop
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
	#C://Users/Kasia/OneDrive/Pulpit/ae2
	path = os.listdir("./")
	path = str(path)
	path = path.encode()
	socket.send(path)


def recv_listening(socket):
	data = socket.recv(4096)
	data = data.decode('utf-8')
	return data


