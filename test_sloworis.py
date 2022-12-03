import socket
import uuid
import time

def init_sock():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('askyourgenie.com',80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: askyourgenie.com\r\n")
    return s
def keep_connection(a):
    a.send(b'x-tsu:%s\r\n' % str(uuid.uuid4()).encode('utf-8'))
start = time.time()
a = init_sock()
while True:
    try:
        keep_connection(a)
        time.sleep(5)
    except Exception as e:
        print(e)
        end = time.time()
        print(end- start)
        exit()


