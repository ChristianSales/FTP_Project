import socket, re, os, glob, gzip, select
#  Code by Sonny Rasavong and Hunter Sales

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


def get(file):
    if file[-3:] == "jpg" or "png":
        try:
            with open(file, 'rb') as inf:
                content = inf.read()
                inf.close()
                return content
        except FileNotFoundError:
            return "File not found"
    elif file[-3:] == "txt":
        try:
            with open(file, 'r') as inf:
                content = inf.read()
                inf.close()
                return content
        except FileNotFoundError:
            return "File not found"














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

    elif cmd == "get":
        if len(wish) > 0:
            info = get(wish)
        else:
            info = "Please enter a file"

    elif cmd == "quit":
        quit()

    else:
        info = "Invalid Command"
    c.send(info.encode())




