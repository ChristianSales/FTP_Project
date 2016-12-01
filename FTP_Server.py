import socket, re, os, glob, gzip, select
import time

#  Code by Sunny Rasavong and Hunter Sales

s = ''
mainDir = "C://FTP_Server"    # Program starts in the FTP_Server
currentDir = mainDir
os.chdir(mainDir)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Open socket for listening
    s.bind((socket.gethostname(), 21))
    s.listen(1)
    c, addr = s.accept()
    print('Got connection from', addr)
except:
    print("connection failed")     # If it cannot connect
    quit()
connection = True
def get(file):    #  Get function
    try:
        print(file)
        with open(file, 'rb') as inf:    # Tries to open file for reading and sends confirm
            c.send("File found".encode())
            while True:
                inf_data = inf.read(4096)    # Reads through the file and sends in packets
                if inf_data == b'':          # Sends ending code when done
                    inf_data = "Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*"
                    c.send(inf_data.encode())
                    time.sleep(.1)
                    break
                time.sleep(.1)
                c.sendall(inf_data)
    except FileNotFoundError:
        c.send("File not found".encode())    # Sends not found if does not exist
def mget(file):          # Gets multiple files but iterating through a list and calling get function
    files = file.split(' ')
    for length in range(len(files)):
        if files[length] != "mget":
            get(files[length])
while connection:
    info = ""
    c.send(os.getcwd().encode())    # Sends the current file path
    data = c.recv(1024).decode()    # Gets the command from client
    command = data.split(' ')
    try:
        cmd = command[0]      # Splits the command to decide on which function to use
    except IndexError:
        cmd = ""
    try:
        wish = command[1]
    except IndexError:
        wish = ""
    if cmd == "ls" or cmd == "dir":     # Loops through directory and formats it to look nice
        if len(wish) == 0:
            for length in range(len(os.listdir(currentDir))):
                info += (os.listdir(currentDir)[length] + " \n")
            c.send(info.encode())
        else:
            info = "Please enter a valid command"    # If they enter extra nonsense
            c.send(info.encode())
    elif cmd == "cd":
        if len(wish) > 0:    # Checks for location
            try:
                os.chdir(wish)
                currentDir = os.curdir    # Try to switch to directory
                info = " "
                c.send(info.encode())
            except FileNotFoundError:
                info = "This file does not exist"    # Informs if does not exist
                c.send(info.encode())
        else:
            info = "Please enter a directory path"    # Informs did not enter path
            c.send(info.encode())
    elif cmd == "get":
        if len(wish) > 0:    # Checks to see if entered path
            print(wish)
            get(wish)    # Runs get function
            print("GET COMMAND EXECUTED")
        else:
            info = "Please enter a file\n"    # Informs if they enter no file
            c.send(info.encode())
    elif cmd == "put":    # Put code
        data = wish.split("/")    #
        filename = data[-1]    # Splits up string and locates the name of file
        answer = c.recv(4096).decode()
        if answer == "uploading":
            sentData = ''
            f = open(os.curdir + "/" + data[-1], "wb")    # Creates that file to write into
            while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                sentData = c.recv(4096)    # While not equal to end of file code, write to file
                if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                    f.write(sentData)
                    print("Downloading")
            f.close()    # Close file when done writing
            print("File downloaded")
    elif cmd == "mput":    # Putting multiple files on server
        files = data.split()    # Splits input and iterates through file locations and writes to each one
        for length in range(len(files)):
            if files[length] != "mput":
                answer = c.recv(4096).decode()
                if answer != "Please enter files" and answer != "File not found":
                    sentData = ''
                    filepath = files[length].split('/')
                    if filepath[0] != "mput":
                        filename = filepath[-1]
                        f = open(os.curdir + '/' + filename, "wb")    # Creates files and writes to them
                        while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                            sentData = c.recv(4096)
                            if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                                f.write(sentData)    # Checks for end of file code
                                print("Downloading...")
                        f.close()
                        print("File downloaded")
    elif cmd == "mget":
        if len(wish) > 0:
            print(wish)    # Calls mget, which calls get multiple times to send files to client
            mget(data)
            print("MGET COMMAND EXECUTED")
        else:
            info = "Please enter a file\n"
            c.send(info.encode())

    elif cmd == "quit":    # Shutdown the program
        quit()
    else:
        info = "Invalid Command"    # User entered a non command
        c.send(info.encode())
