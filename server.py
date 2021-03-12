from twisted.internet import protocol, reactor
import names

transports = set() # 클라이언트를 저장할 변수
users = set()

COLORS = [ # 터미널 컬러코드
    '\033[31m', # RED
    '\033[32m', # GREEN
    '\033[33m', # YELLOW
    '\033[34m', # BLUE
    '\033[35m', # MAGENTA
    '\033[36m', # CYAN
    '\033[37m', # WHITE
    '\033[4m',  # UNDERLINE
]

class Chat(protocol.Protocol):
    def connectionMade(self):
        # print('connected') 첫테스트. 사용자가 서버에 접속하면 connected 메시지 출력
        # self.transport.write('connected'.encode())  둘테스트.클라이언트가 연결되면 connected 메시지 출력 문자열 -> 바이트
        name = names.get_first_name() #랜덤한 이름을 생성한다.
        color = COLORS[len(users) % len(COLORS)]
        users.add(name) # 랜덤한 이름을 users에 추가한다.
        transports.add(self.transport) # 사용자가 접속하면 transport(클라이언트)추가
        
        self.transport.write(f'{color}{name}\033[0m'.encode()) #사용자가 접속하면 이름을 부여한다. 이름에만 색을칠하고 메시지는 칠하지않는다.

    def dataReceived(self, data):
        # print(data)  첫테스트. 사용자가 서버에 메시지를 보내면 실행, 사용자메시지(data)출력

        for t in transports:
            if self.transport is not t:
                t.write(data)
                
class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat() # 통신프로토콜 정의

print('Server started!')
reactor.listenTCP(8000, ChatFactory())
reactor.run()


