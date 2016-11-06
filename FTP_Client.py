import socket, re, os, glob, gzip, select, getpass



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
login = False
while not login:
    print("FTP Login 192.168.1.69")
    print("Please enter your username")
    username = input()
    password = getpass.win_getpass('Enter Password:')
    check1 = re.search("@", password)
    check2 = re.search(".", password["@":])
    if check1 is True & check2 is True:
        print("Access Granted")
        login = True
    else:
        print("Access Denied")




while connection:
    print(s.recv(1024).decode())
    command = input()
    if command == "":
        command = " "
    s.send(command.encode())
    print('test1')
    print(s.recv(1024).decode())
    print('test2')

    if command == "quit":
        print('Shutting down...')
        quit()







