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
    username = input()                  # getpass library does not work on my IDE
    print("Please enter your password")    # will create way to hide password by final code due date
    password = input()
    check1 = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", password)
    if check1 is None or len(username) < 1:      # This regex is taken from EmailRegex.com
        print("Access Denied")

    else:
        print("Access Granted")
        login = True




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










