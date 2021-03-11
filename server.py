from twisted.internet import protocol, reactor

class Chat(protocol.Protocol):
    def connectionMade(self):
        print('connected') #사용자가 서버에 접속하면 connected 메시지 출력
        
    def dataReceived(self, data):
        print(data) # 사용자가 서버에 메시지를 보내면 실행, 사용자메시지(data)출력

class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat() # 통신프로토콜 정의

print('Server started!')
reactor.listenTCP(8000, ChatFactory())
reactor.run()


