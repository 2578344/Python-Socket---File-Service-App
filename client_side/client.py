import socket
import os
import sys

from smod import recv_listening, recv_file, send_file,client_command

# Create the socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#first argument server Ip, second port
srv_addr = (sys.argv[1], int(sys.argv[2]))
command = sys.argv[3]

# Convert to string
srv_addr_str = str(srv_addr)
#Read up to 1048576 bytes at a time;
BUFFER_SIZE = 1048576

try:
    print("Connecting to " + srv_addr_str + "... ")


    cli_sock.connect(srv_addr)

    print("Connected. Now")
except Exception as e:
    # Print the exception message
    print(e)
    # Exit with a non-zero value, to indicate an error condition
    exit(1)

client_command(command,cli_sock)


cli_sock.close()


# Exit with a zero value, to indicate success
exit(0)
