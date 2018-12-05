import socket

HOST = '' # host here
PORT =  # port number here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    m = s.recv(1024)
    print(m)

    break

s.close()