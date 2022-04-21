import socket
import sys
from smod import send_listening, recv_file, send_file,server_command

# Create the socket
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Read up to 1048576 bytes at a time;
BUFFER_SIZE = 1048576

try:

    srv_sock.bind(("0.0.0.0", int(sys.argv[1])))  # sys.argv[1] port
    srv_sock.listen(5)
except Exception as e:
    # Print the exception message
    print(e)
    # Exit with a non-zero value, to indicate an error condition
    exit(1)

# Loop forever (or at least for as long as no fatal errors occur)
while True:

    try:
        print("Waiting for new client... ")

        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)

        print("Client " + cli_addr_str + " connected.")


        data = cli_sock.recv(2000)

        # receive command
        server_command(data.decode(),cli_sock)



    finally:

        cli_sock.close()


# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)
