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
PORT = int(input('Port: '))
MAX_CLIENTS = int(input('Max clients: '))
IS_RUNNING = True
OPTIONS = ('Connect', 'Check info', 'Close program')

def option_connect():
    ADDRESS = input('Address: ')
    try:
        thread = threading.Thread(target=p2p.create_session, args=(ADDRESS,))
        thread.start()
    except Exception as e:
        print('Connection failed')
        print(e)
    print('Connection successfully created')
    while True:
        if p2p.check_request(ADDRESS):
            print('Request: ')
            print(p2p.get_request(ADDRESS))
        else:
            msg = input('Write message: ')
            if msg == '!quit':
                try:
                    p2p.close_connection(ADDRESS)
                except Exception as e:
                    print(e)
                print('Connection closed')
                break
            else:
                p2p.send(ADDRESS, msg)
                time.sleep(0.1)
    thread.join(0)

if __name__ == '__main__':
    try:
        p2p = P2P(PORT, MAX_CLIENTS)
    except Exception as e:
        print('Server initialization failed')
        print(e)
        IS_RUNNING = False

    while IS_RUNNING:
        print('\n', threading.active_count())
        for i in enumerate(OPTIONS): print(f'{i[0]} -> {i[1]}')

        ch = input(': ')
        if ch == '0':
            option_connect()
        elif ch == '2':
            p2p.kill_server()
            IS_RUNNING = False

    print('Closed')
