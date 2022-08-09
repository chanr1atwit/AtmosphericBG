# WSL main application, runs in the background and performs essentia analysis
# Interacts with the main application through IPC sockets

import essentia
################## STARTER CODE
from multiprocessing.connection import Listener

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
while True:
    msg = conn.recv()
    # do something with msg
    

    if msg == 'close':
        conn.close()
        break
listener.close()

################## STARTER CODE
