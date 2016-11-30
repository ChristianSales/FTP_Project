import socket, re, os, glob, gzip, select, getpass

# Code by Sonny Rasavong and Hunter Sales

print("Attempting connection to server...")
s = ""

try:
    s = socket.socket()
    s.connect(('Bills', 21))
except (socket.gaierror, ConnectionRefusedError):
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
    print('test1')
    print(s.recv(1024).decode())
    print('test2')
    action = input()
    if action == "":
        action = " "
    inputs = action.split()
    print('test3')
    try:
        cmd = inputs[0]
    except IndexError:
        cmd = ""
    try:
        wish = inputs[1]
    except IndexError:
        wish = ""

    s.send(action.encode())
    if cmd == "ls":
        print('test5')
        print(s.recv(1024).decode())
    elif cmd == "cd":
        print(s.recv(1024).decode())

    elif cmd == "get":

        data = wish.split("/")
        filename = data[-1]
        answer = s.recv(4096).decode()
        print(answer)
        if answer != "File not found" and answer != "Please enter a file\n":
            sentData = ''
            f = open(os.curdir + '/' + data[-1], "wb")
            while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                sentData = s.recv(4096)
                if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                    f.write(sentData)
                    print("Downloading...")
            f.close()
            print("File downloaded")

        else:
            print("file not found")
    elif cmd == "mget":
        files = action.split(' ')
        for length in range(len(files)):
            if files[length] != "mget":
                answer = s.recv(4096).decode()
                print(answer)
                if answer != "File not found" and answer != "Please enter a file\n":
                    sentData = ''
                    filepath = files[length].split('/')
                    print(filepath)
                    if filepath[0] != "mget":
                        filename = filepath[-1]
                        f = open(os.curdir + '/' + filename, "wb" )
                        while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                            sentData = s.recv(4096)
                            if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                                f.write(sentData)
                                print("Downloading...")
                        f.close()
                        print("File downloaded")








    else:
        print(s.recv(1024).decode())

    if cmd == "quit":
        print('Shutting down...')
        quit()
