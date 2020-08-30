from p2p import P2P
import threading
import time

# create_session()
# close_connection()
# kill_server
# send
# raw_send
# get_request
# check_request
# check_address

PORT = 11337
MAX_CLIENTS = 2
p2p = P2P(PORT, MAX_CLIENTS)

def connect():
    ADDRESS = input('IP: ')
    if not p2p.check_address(ADDRESS):
        thread = threading.Thread(target=p2p.create_session, name=ADDRESS, args=(ADDRESS,))
        thread.start()
        time.sleep(1)
        if p2p.check_address(ADDRESS):
            print(f'Connection to {ADDRESS} succeed')
        else:
            print(f'Connection to {ADDRESS} failed')
            thread.join()
    else:
        print(f'You are already connected to {ADDRESS}')
def disconnect():
    connection_list()
    ind = int(input('Index: '))
    ADDRESS = p2p.clients_ip[ind]
    try:
        p2p.close_connection(ADDRESS)
    except KeyError:
        pass
    print(f'Connection closed with {ADDRESS}')
def connection_list():
    for ind, ip in enumerate(p2p.clients_ip):
        if ip != '':
            print(f'{ind}) --> {ip}')
def serv_exit():
    print('Closing...')
    p2p.kill_server()
def connections_handler():
    while p2p.running:
        old_l = p2p.clients_ip
        time.sleep(2)
        if old_l != p2p.clients_ip:
            print('There is new connection')


commands = {
    'connect': connect,
    'list': connection_list,
    'exit': serv_exit,
    'disconnect': disconnect
}

while p2p.running:
    # com = input(': ').replace(' ', '').lower()
    # commands[com]() if com in commands else print('There is no command like this')
    print(p2p.client_sockets)
    time.sleep(0.5)