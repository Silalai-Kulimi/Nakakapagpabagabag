import threading
import time
import socket
import sys
import os

vers = 0
programFormat = ".py"
i = 0

filename = os.path.basename(__file__)
print(filename)
n = 0

username = input("username?")

for root, dirs, files in os.walk('./'):
    for name in files:
        if name.endswith(programFormat):
            n += 1
            print(n)
            if "./" + filename != os.path.join(root, name):
                os.remove(os.path.join(root, name))
                print(os.path.join(root, name))



def ChecknUpdate():
    if lastestVers > vers:
        while str(s.recv(1024), "utf-8") != "# ok":
            s.sendall(bytes("# u", "utf-8"))
            print("# u")
        newvers = open(str(lastestVers) + programFormat, "w+")
        fileFragment = ""
        i = 0
        while True:
            fileFragment = str(s.recv(1024), "utf-8")
            print(fileFragment + "fileFragment")
            print('Delivery completed' == fileFragment)
            if '' == fileFragment:
                i += 1
                if i > 10:
                    print(fileFragment + "___fileFragment")
                    print(lastestVers)
                    newvers.close()
                    os.system(str(lastestVers) + programFormat)
                    return
            if '# Delivery completed' == fileFragment:
                print(fileFragment + "___fileFragment")
                print(lastestVers)
                newvers.close()
                os.system(str(lastestVers) + programFormat)
                return
            newvers.write(fileFragment)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
print(local_ip)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"  # 192.168.212.108
port = 1509
s.connect((host, port))

lastestVers = float(str(s.recv(1024), "utf-8"))

ChecknUpdate()
# if lastestVers > vers:
#     i += 1
#     print(i)
#     s.sendall(bytes("u", "utf-8"))
#     newvers = open(str(lastestVers)+programFormat, "w+")
#     fileFragment = ""
#     i += 1
#     print(i)
#     while not 'Delivery completed' == fileFragment:
#         i += 1
#         print(i)
#         fileFragment = str(s.recv(1024), "utf-8")
#         if 'Delivery completed' == fileFragment:
#
#         newvers.write(fileFragment)
#         print(fileFragment+"fileFragment")
#     k = 0
#     k += 1
#     print(k)
#     print(lastestVers)
#     newvers.close()
#     k += 1
#     print(k)
s.close()
# k += 1
# print(k)

# while True:
#     msg = str(s.recv(1024), "utf-8")
#     print(msg)
#     s.sendall(bytes(input(), "utf-8"))
