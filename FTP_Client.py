
import socket, re, os, glob, gzip, select



print("Attempting connection to server...")
s = ""

try:
    s = socket.socket()
    s.connect(('Bills', 21))
except (socket.gaierror,ConnectionRefusedError):
    print("Connection Failed")
    quit()

print("Connection Successful!")
connection = True
while connection:
    print(s.recv(1024).decode())
    command = input()
    if command == "":
        command = " "
    s.send(command.encode())
    print('test1')
    print(s.recv(1024).decode())
    print('test2')
    if command == "quit" or "Quit":
        print('Shutting down...')
        quit()




