from socket import *
import sys
import threading
from datetime import datetime

local_dt = datetime.now()


#################################### Setup SERVER & PORT ####################################
SERVER = gethostbyname(gethostname())
PORT = 8000
server_address = (SERVER, PORT)
serversocket = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the port
serversocket.bind(server_address)

#################################### Define FORM & Client reply ####################################
# HTTP response
data_to_client = "HTTP/1.1 200 OK\r\n"
data_to_client += "Date:"+str(local_dt)+"\r\n"
#data_to_client += "Content-length:"+str(data_length)+"\r\n"
data_to_client += "Connection: Keep-Alive\r\n"
data_to_client += "Content-type: text/html; charset=utf-8\r\n"
data_to_client += "\r\n"
# actual data response 
data_to_client += "<html><body>EE-4210: Continuous assessment.<body><html>\r\n\r\n"
            
#################################### Client conenction and comms ####################################
def handle_client(client_data, client_address):
            print(f"\n[NEW CONNECTION] {client_address} connected\n")
            #data_length = len(client_data)
            # break pieces by \n
            #pieces = client_data.decode().split("\n")
            # immediately blast out message
            # sendto() used to send to right address since connectionless
            sent = serversocket.sendto(data_to_client.encode(), client_address)
            #print(f'sent {sent} bytes back to {client_address}')


def createserver():
            print('\nwaiting to receive message\n')
            while (1):
                        # UDP connectionless so no listen() & accept()
                        # data & address received from client
                         (client_data, client_address) = serversocket.recvfrom(4096)
        
                        # New thread started for client --> handle_client
                        thread = threading.Thread(target=handle_client, args=(client_data, client_address))
                        thread.start()
                        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print(f"Access http://{SERVER}:8000")
createserver()
