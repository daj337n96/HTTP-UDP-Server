from socket import *
import sys

#SERVER = 'localhost'
SERVER = gethostbyname(gethostname())
PORT = 8000

def createserver():
    # Create a TCP/IP socket
    sock = socket(AF_INET, SOCK_DGRAM)
    server_address = (SERVER, PORT)
    #try:
    #print(f'starting up on {SERVER} port {PORT}')
    # Bind the socket to the port
    sock.bind(server_address)

    while True:
         # UDP connectionless so no listen() & accept()
        print('\nwaiting to receive message\n')
        # data & address received from client
        client_data, client_address = sock.recvfrom(5000)
        data_length = len(client_data)

        # break pieces by \n
        pieces = client_data.decode().split("\n")
        # valid data
        if(len(pieces) > 0):
            # print out the HTTP GET and favicon
            # the HTTP GET request houses the word we typed
            # GET /hello HTTP/1.1
            print(pieces[0])

        print(f'received {data_length} bytes from {client_address}') 
        #print(client_data.decode())

        # HTTP response
        data_to_client = "HTTP/1.1 200 OK\r\n"
        data_to_client += "content-type: text/html; charset=utf-8\r\n"
        data_to_client += "\r\n"
        # actual data response 
        data_to_client += "<html><body>EE-4210: Continuous assessment.<body><html>\r\n\r\n"
            

            
        if client_data:
            # sendto() used to send to right address since connectionless
            sent = sock.sendto(data_to_client.encode(), client_address)
            print(f'sent {sent} bytes back to {client_address}')

print(f"Access http://{SERVER}:8000")
createserver()


