import numpy as mypy
import threading
import time
import random

import socket as mysoc

def client():
        
  
# Define the port on which you want to connect to the server
    port = 50010              
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
    

    # Open file containing messages
    file = open('./HW1test.txt')
    line = file.readline()
    outputFile = open('./HW1out.txt', 'w')
    while line:
        try:
            cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            print("[C]: Client socket created")
        except mysoc.error as err:
            print('{} \n'.format("socket open error ",err))
        # connect to the server on local machine
        server_binding=(sa_sameas_myaddr,port)
        cs.connect(server_binding)
        # Send Message to server
        msg = line.strip()
        print("('[C]: Sending '%s' to server)" % msg)
        cs.send(msg.encode('utf-8'))
        data_from_server=cs.recv(100)
        
        #receive data from the server 
        response = data_from_server.decode('utf-8')

        print("[C]: Data received from server::  ",response)
        outputFile.write(response + '\n')

        line = file.readline()

        # close the cclient socket 
        cs.close()
        time.sleep(0.5)
    
    file.close()
    outputFile.close()
    exit()   

t2 = threading.Thread(name='client', target=client)
t2.start()

input("Hit ENTER  to exit")

exit()

