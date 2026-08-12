serverAddress = ("0.0.0.0", 9339)

import socket
from Heart.Connection import Connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
server.bind(serverAddress)
print ("ABS V62 ЗАПУЩЕНО!")
while True:
    server.listen()
    socket, address = server.accept()
    print ("ПОДКЛЮЧЕНИЕ ПРЕРВАНО")
    Connection(socket, address).start()