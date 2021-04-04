from socket import *
import sys

SERVER = 'localhost'
PORT = 8000


# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

server_address = (SERVER, PORT)
#message = "This is the message.  It will be repeated."
HTTP_cmd = 'GET http/ HTTP1.1'

try:

    # Send data
    print(f'sending {HTTP_cmd}')
    sent = sock.sendto(HTTP_cmd.encode(), server_address)

    # Receive response
    print('waiting to receive\n')
    data, server = sock.recvfrom(4096)
    print(f'{data.decode()}')

finally:
    print('closing socket')
    sock.close()
