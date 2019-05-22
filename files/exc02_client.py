
import socket

sockfd = socket.socket()

sockfd.connect(('0.0.0.0',8882))

fr = open('a.png','rb')
for line in fr:
    sockfd.send(line)

data = sockfd.recv(1024)
print('from server:',data.decode())

fr.close()

sockfd.close()
