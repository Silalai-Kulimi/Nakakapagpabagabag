import threading
import time
import socket
import sys

vers = 0.1

programFormat = ".py"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
print(local_ip)
s.close()

HOST = ""
PORT = 1509

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# newvers = open(str(vers)+programFormat, "r")

s.listen(1024)
# Temporary_storage = ""

while True:
    conn, addr = s.accept()
    print('Connected with '+addr[0]+':'+str(addr[1]))
    print(conn)

    conn.sendall(bytes(str(vers), "utf8"))
    print(bytes(str(vers), "utf8"))
    if str(conn.recv(1024)) == "u":
        newvers = open(str(vers) + programFormat, "r", encoding='utf8')
        print(str(vers) + programFormat)
        l = "text"
        while l != "":
            l = newvers.read(1024)
            # Temporary_storage = Temporary_storage + l
            conn.sendall(bytes(l, "utf-8"))
            print(l+"line of recv")
            print("line of recv")
        # print(Temporary_storage+"text of stor")
        # print("text of stor")
        newvers.close()
        conn.sendall(bytes("# Delivery completed", "utf-8"))
    conn.close()
