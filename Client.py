from socket import *
serverName = '10.2.12.233'
serverPort = 14500
clientSocket = socket(AF_INET, SOCK_DGRAM)
ls = ['nowhere.','north','south','west','north-west','south-west','east','north-east','south-east']
while True:
    print('<<Point a>>')
    x1 = input('Enter x coordinate: ')
    y1 = input('Enter y coordinate: ')
    print('<<Point b>>')
    x2 = input('Enter x coordinate: ')
    y2 = input('Enter y coordinate: ')
    clientSocket.sendto(x1.encode(),(serverName, serverPort))
    clientSocket.sendto(y1.encode(),(serverName, serverPort))
    clientSocket.sendto(x2.encode(),(serverName, serverPort))
    clientSocket.sendto(y2.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    h, serverAddress = clientSocket.recvfrom(2048)
    v, serverAddress = clientSocket.recvfrom(2048)
    #print(modifiedMessage.decode())
    print('Distance between('+str(x1)+','+str(y1)+')and('+str(x2)+','+str(y2)+')' )
    print('You are going',ls[int(modifiedMessage.decode())])
    print('Horizontal distance is',int(h.decode()) )
    print('Vertical distance is', int(v.decode()) )
    
clientSocket.close()