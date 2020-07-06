#!/bin/python


############################################## Socket Programming ####################################

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
### AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.

s.connect((HOST,PORT))

### to run above 1st run command $ nc -nvlp 7777 on other terminal

##########################################################################################################
##########################################################################################################
