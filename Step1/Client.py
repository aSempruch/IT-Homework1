import numpy as mypy
import threading
import time
import random

import socket as mysoc

def client():
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
        
  
# Define the port on which you want to connect to the server
    port = 50007                
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding) 
    data_from_server=cs.recv(100)
#receive data from the server 
  
    print("[C]: Data received from server::  ",data_from_server.decode('utf-8'))
# close the cclient socket 
    cs.close() 
    exit()   

t2 = threading.Thread(name='client', target=client)
t2.start()

input("Hit ENTER  to exit")

exit()

