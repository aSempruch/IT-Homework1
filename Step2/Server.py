import numpy as mypy
import threading
import time
import random
import socket as mysoc


def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50010)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)

    # Accept multiple connections
    while 1:
        csockid,addr=ss.accept()
        print ("[S]: Got a connection request from a client at", addr)

        # Receive message from client
        message_from_client = csockid.recv(100).decode('utf-8')
        print("[S] Message from client ", message_from_client)

        # Revese String
        response = message_from_client[::-1]

        # send response  message to the client.  
        csockid.send(response.encode('utf-8'))
  
   # Close the server socket
    ss.close() 
    exit()

t1 = threading.Thread(name='server', target=server)
t1.start()

input("Hit ENTER  to exit")

exit()

