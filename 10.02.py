#!/bin/python3
#how to run :  ./10.02.py 127.0.0.1 (my system)

############################################## Port Scanner ####################################



import sys
import socket
from datetime import datetime



#Define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
    print(f"target : {target}")
else:
    print("invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

#add a pretty banner

print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)          # if it takes more than 1 sec it will leave
        result = s.connect_ex((target,port)) # returns error indicator : for open port it gives 0 for closed 1
        if result == 0:
            print(f"port {port} is open")
        # else:
        #     print(f"port {port} is not open")
        s.close()
except KeyboardInterrupt:
    print("\n....Exiting program.")
    sys.exit()
except socket.gaierror:
    print("hostname can't be resolved.")
    sys.exit()
except socket.error:                    # ingeneral occurs may be due to firewall, anti-virus or busy with some 
    print("can't connect to server")    # other client.
    sys.exit()


##########################################################################################################
########################################    OUTPUT      ##################################################


    # 🃏~/🃏 Start/Python 0.0 :) ./10.02.py 127.0.0.1          (Laptop)

    # target : 127.0.0.1                                       
    # --------------------------------------------------
    # Scanning target 127.0.0.1
    # Time started: 2020-05-09 18:10:28.555834
    # --------------------------------------------------
    # port 80 is open
    # port 443 is open
    # port 631 is open
    # port 902 is open
    # port 1716 is open
    # port 3306 is open
    # port 8307 is open
    # port 33060 is open

    # 🃏~/🃏 Start/Python 0.0 :) ./10.02.py 192.168.43.155         (mobile)

    # target : 192.168.43.155
    # --------------------------------------------------
    # Scanning target 192.168.43.155
    # Time started: 2020-05-09 18:12:39.045089
    # --------------------------------------------------
    # port 80 is open
    # port 443 is open
    # port 902 is open
    # port 1716 is open
    # port 33060 is open

    # 🃏~/🃏 Start/Python 0.0 :) 

##########################################################################################################
##########################################################################################################