import socket


s=socket.socket()
print('Socket created')

s.bind(('localhost',9999))

s.listen(2)
print('Waiting for connections ')

while True:
    c,addr=s.accept()
    val=c.recv(1024).decode()
    print("Connected with",addr,val)
    
    c.send(bytes('Welcome Vigs','utf-8'))
    
    c.close()

