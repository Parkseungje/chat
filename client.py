import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000)) # 서버에 접속한다 127.0.0.1 == localhost == 내 컴퓨터




