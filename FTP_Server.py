import socket, re, os, glob, gzip, select
import time

#  Code by Sonny Rasavong and Hunter Sales

s = ''
mainDir = "D://FTP_Server"
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


def get(file):
    try:
        print(file)
        with open(file, 'rb') as inf:
            c.send("File found".encode())
            while True:
                inf_data = inf.read(4096)
                if inf_data == b'':
                    inf_data = "Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*"
                    c.send(inf_data.encode())
                    time.sleep(.1)
                    break
                time.sleep(.1)
                c.sendall(inf_data)
    except FileNotFoundError:
        c.send("File not found".encode())

def mget(file):
    files = file.split(' ')
    for length in range(len(files)):
        if files[length] != "mget":
            get(files[length])



while connection:
    info = ""
    c.send(os.getcwd().encode())
    data = c.recv(1024).decode()
    command = data.split(' ')
    try:
        cmd = command[0]
    except IndexError:
        cmd = ""
    try:
        wish = command[1]
    except IndexError:
        wish = ""
    if cmd == "ls" or cmd == "dir":
        if len(wish) == 0:
            for length in range(len(os.listdir(currentDir))):
                info += (os.listdir(currentDir)[length] + " \n")
            c.send(info.encode())
        else:
            info = "Please enter a valid command"
            c.send(info.encode())
    elif cmd == "cd":
        if len(wish) > 0:
            try:
                print("test4")
                os.chdir(wish)
                currentDir = os.curdir
                info = " "
                c.send(info.encode())
            except FileNotFoundError:
                info = "This file does not exist"
                c.send(info.encode())
        else:
            info = "Please enter a directory path"
            c.send(info.encode())
    elif cmd == "get":
        if len(wish) > 0:
            print(wish)
            get(wish)
            print("GET COMMAND EXECUTED")
        else:
            info = "Please enter a file\n"
            c.send(info.encode())
    elif cmd == "put":
        data = wish.split("/")
        filename = data[-1]
        answer = c.recv(4096).decode()
        if answer == "uploading":
            sentData = ''
            f = open(os.curdir + "/" + data[-1], "wb")
            while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                sentData = c.recv(4096)
                if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                    f.write(sentData)
                    print("Downloading")
            f.close()
            print("File downloaded")
    elif cmd == "mput":
        files = data.split()
        for length in range(len(files)):
            if files[length] != "mput":
                answer = c.recv(4096).decode()
                if answer != "Please enter files" and answer != "File not found":
                    sentData = ''
                    filepath = files[length].split('/')
                    if filepath[0] != "mput":
                        filename = filepath[-1]
                        f = open(os.curdir + '/' + filename, "wb")
                        while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                            sentData = c.recv(4096)
                            if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                                f.write(sentData)
                                print("Downloading...")
                        f.close()
                        print("File downloaded")




    elif cmd == "mget":
        if len(wish) > 0:
            print(wish)
            mget(data)
            print("MGET COMMAND EXECUTED")
        else:
            info = "Please enter a file\n"
            c.send(info.encode())

    elif cmd == "quit":
        quit()
    else:
        info = "Invalid Command"
        c.send(info.encode())
