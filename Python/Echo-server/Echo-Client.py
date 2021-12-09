import socket

HOST = '127.0.0.1'
PORT = 65432 # 임시 프로그램이므로 임시로 정한 포트넘버

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello World')
    data = s.recv(1024)

print('Received', repr(data))