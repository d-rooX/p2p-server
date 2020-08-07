from serv_src import P2P
from time import sleep

ADDR = input('Address: ')
PORT = int(input('PORT: '))

p2p = P2P(PORT)
p2p.create_session(ADDR)
while True:
    print(p2p.get_request() + '>>>>')
