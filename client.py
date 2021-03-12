import socket
import select
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000)) # 서버에 접속한다 127.0.0.1 == localhost == 내 컴퓨터

name = None # 자신의 이름을 저장할 변수

while True:
    read, write, fail = select.select((s, sys.stdin), (), ()) # 소켓에서 메시지를 읽을수 있을때까지 대기

    for desc in read:
        if desc == s:
            data = s.recv(4096) # 메시지가 도착하면 소켓에서 4096바이트를 읽는다.
            print(data.decode()) # 바이트 -> 문자열 출력

            if name is None:
                name = data.decode() #처음 접속했다면 부여받은 이름을 저장하고
                s.send(f'{name} is connected!'.encode()) # 다른사람에게 접속 사실을 알린다.
        else:
            msg = desc.readline()
            msg = msg.replace('\n', '')
            s.send(f'{name} {msg}'.encode())


