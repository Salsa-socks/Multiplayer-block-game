import socket
import thread
import sys


#working locally. need mongo server settings
server = ""
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server.port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")

#server above - initialize