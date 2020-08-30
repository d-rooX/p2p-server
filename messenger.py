from p2p import P2P
import threading

# create_session()
# close_connection()
# kill_server
# send
# raw_send
# get_request
# check_request
# check_address

PORT = 1337
MAX_CLIENTS = 2
p2p = P2P(PORT, MAX_CLIENTS)

def connect():
    ADDRESS = input('IP: ')
    try:
        thread = threading.Thread(target=p2p.create_session, name=ADDRESS, args=(ADDRESS,))
        thread.start()
    except:
        print(f'Connection with {ADDRESS} failed')
    else:
        print(f'Connection with {ADDRESS} succeed')

def disconnect():
    connection_list()
    ind = int(input('Index: '))
    ADDRESS = p2p.clients_ip[ind]
    try:
        p2p.close_connection(ADDRESS)
    except:
        print('Some error')
    print(f'Connection closed with {ADDRESS}')

def connection_list():
    print(p2p.clients_ip)


def serv_exit():
    print('Closing...')
    p2p.kill_server()


commands = {
    'connect': connect,
    'list': connection_list,
    'exit': serv_exit,
    'disconnect': disconnect
}

while p2p.running:
    com = input(': ').replace(' ', '').lower()
    commands[com]() if com in commands else print('There is no command like this')
