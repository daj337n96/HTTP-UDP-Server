# HTTP-UDP-Server
UDP is connectionless and does not verify data and immediately blasts out data.

This HTTP_UDP_server will display the constant text "EE-4210: Continuous assessment.".

data_to_client defines the HTTP string response to the client.
FORM defines the html string to be sent to display the webpage form.
FORM_REPLY defines the HTTP reply to the client after the text is entered.

Function server unlike the TCP server will not listen and accept any client attempting to connec, it will only receive the client's request and create a thread for the it.
Function handle_client will be called by the thread function to handle the clients connected.

Connection will be terminated after.


