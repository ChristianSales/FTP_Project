import socket, re, os, glob, gzip, select


s = ''
mainDir = "D://"
currentDir = mainDir
os.chdir(mainDir)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 21))
    s.listen(1)
    c, addr = s.accept()
    print('Got connection from', addr)

except:
    print("connection failed")
    quit()

connection = True
"""
trying = True
password = False
while trying:
    while not password:
        c.send("Please enter a username and password")
        loginInfo = c.recv(1024)
        """




while connection:
    info = ""

    c.send(os.getcwd().encode())
    print("test1")
    data = c.recv(1024).decode()
    print("test2")
    command = data.split(' ')
    try:
        cmd = command[0]
    except IndexError:
        cmd = ""
        print('test3')
    try:
        wish = command[1]
    except IndexError:
        wish = ""
    if cmd == "ls":
        if len(wish) == 0:
            for length in range(len(os.listdir(currentDir))):
                info += (os.listdir(currentDir)[length] + " \n")
        else:
            info = "Please enter a valid command"

    elif cmd == "cd":
        if len(wish) > 0:
            try:
                print("test4")
                os.chdir(wish)
                currentDir = os.curdir
                info = " "
            except FileNotFoundError:
                info = "This file does not exist"
        else:
            info = "Please enter a directory path"

    elif cmd == "quit":
        quit()

    else:
        info = "Invalid Command"
    c.send(info.encode())



