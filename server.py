import math

def check_horizontal(x,xx):
    h_distance = abs(x - xx)
    return str(h_distance)

def check_vertical(y,yy):
    v_distance = abs(y - yy)
    return str(v_distance)

def check_direction(x,y):
    pos = ''
    if x == 0:
        if y == 0:
            pos = '0'
        elif y > 0:
            pos = '1'
        else:
            pos = '2'
    elif x < 0:
        if y == 0:
            pos = '3'
        elif y > 0:
            pos = '4'
        else:
            pos = '5'
    else:
        if y == 0:
            pos = '6'
        elif y > 0:
            pos = '7'
        else:
            pos ='8'
            
        
      
    return pos
        

from socket import *
serverPort = 14500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while True:
    x1, clientAddress = serverSocket.recvfrom(2048)
    y1, clientAddress = serverSocket.recvfrom(2048)
    x2, clientAddress = serverSocket.recvfrom(2048)
    y2, clientAddress = serverSocket.recvfrom(2048)
    xpos = int(x2.decode())-int(x1.decode()) 
    ypos = int(y2.decode())-int(y1.decode()) 
    modifiedMessage = check_direction(xpos,ypos)
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    
    h = check_horizontal(int(x1.decode()),int(x2.decode()))
    v = check_vertical(int(y1.decode()),int(y2.decode()))
    serverSocket.sendto(h.encode(),clientAddress)
    serverSocket.sendto(v.encode(),clientAddress)