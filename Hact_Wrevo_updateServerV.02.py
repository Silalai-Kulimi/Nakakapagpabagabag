import socket
import sys
import threading
HOST = ''
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except(socket.error, msg):
    print('Bind failed. Error Code : '+str(msg[0])+' Message '+msg[1])
    sys.exit()
print('Socket bind complete')
s.listen(10)
print('Socket now listening')


def clientthread(conn):
    conn.send(bytes('Welcome to the server. Type something and hit enter\n', "utf8"))


while True:
    while 1:
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        threading.Thread(target=clientthread(conn)).start
        # start_new_thread(clientthread, (conn,))
        data = conn.recv(1024)
        reply = 'OK...'+str(data, "utf8")
        if not data:
            break
            print("break")
        conn.sendall(bytes(reply, "utf8"))
        conn.close()

s.close()
