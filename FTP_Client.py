import socket, re, os, glob, gzip, select, getpass

# Code by Sonny Rasavong and Hunter Sales

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
"""
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
"""

os.chdir("D://FTP_Client")

while connection:
    print(s.recv(1024).decode())
    command = input()
    if command == "":
        command = " "
    s.send(command.encode())
    if command == "ls":
        print(s.recv(1024).decode())
    if command == "cd":
        print(s.recv(1024).decode())

    if command == "get":
        data = command.split("/")
        filename = data[-1]
        answer = s.recv(1024).decode()
        if answer == "File not found" or "Please enter a file":
            print(answer)
        else:

            if filename[-3:] == 'jpg' or 'png':
                f = open(os.curdir + data[1], "wb")
                f.write(answer)
                f.close()
            elif filename[-3:] == 'txt':
                f = open(os.curdir + data[1], "w")
                f.write(answer)
                f.close()


    if command == "quit":
        print('Shutting down...')
        quit()










