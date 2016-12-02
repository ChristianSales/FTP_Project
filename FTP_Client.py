import socket, re, os, glob, gzip, select, getpass
import time

# Code by Sunny Rasavong and Hunter Sales

print("Attempting connection to server...")
s = ""

try:
    s = socket.socket()
    s.connect(('SuN', 21))    # creates a socket and connects to host
except (socket.gaierror, ConnectionRefusedError):
    print("Connection Failed")
    quit()

print("Connection Successful!")
connection = True
login = False

while not login:
    print("FTP Login 10.20.121.127")    # Asks for information for logging in
    print("Please enter your username")
    username = input()                  # getpass library does not work on my IDE
    print("Please enter your password")
    password = input()
    check1 = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", password)
    if check1 is None or len(username) < 1:      # This regex is taken from EmailRegex.com
        print("Access Denied")                   # Checks for proper email format
    else:
        print("Access Granted")
        login = True
        
os.chdir("D://FTP_Client")    # Set directory to FTP_Client
def put(wish):
    try:
        with open(wish, 'rb') as inf:    # Open file to be sent
            s.send("uploading".encode())
            while True:
                inf_data = inf.read(4096)    # read file into variable and send data to server
                if inf_data == b'':
                    inf_data = "Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*"
                    s.send(inf_data.encode())
                    time.sleep(.1)    # Once it reaches the end it breaks and closes
                    break
                time.sleep(.1)
                print("Uploading...")
                s.sendall(inf_data)
            print('File uploaded')
    except FileNotFoundError:
        s.send("File not found".encode())
        print('File not found')
while connection:
    print(s.recv(1024).decode())    # Gives current directory
    action = input()
    if action == "":
        action = " "
    inputs = action.split()    # takes input string and slices it for further options
    try:
        cmd = inputs[0]
    except IndexError:
        cmd = ""
    try:
        wish = inputs[1]
    except IndexError:
        wish = ""
    s.send(action.encode())
    if cmd == "ls" or cmd == "dir":
        print(s.recv(1024).decode())    # accepts the list of files in directory
    elif cmd == "cd":
        print(s.recv(1024).decode())    # Shows what directory changed too
    elif cmd == "get":
        data = wish.split("/")
        filename = data[-1]
        answer = s.recv(4096).decode()    # Gets name of file and open it to be written in too
        print(answer)
        if answer != "File not found" and answer != "Please enter a file\n":
            sentData = ''
            print('test1')
            f = open(os.curdir + '/' + data[-1], "wb")
            print("test2")
            while sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                sentData = s.recv(4096)    # writes into file until end code is hit
                if sentData != b'Finished sending)(*&^%$%^*(*&^%$%^&*&^%$%^&*(*&^%$#$%^&*(&^%$#$%^&*':
                    f.write(sentData)
                    print("Downloading...")
            f.close()    # closes down file when done writing into
            print("File downloaded")
        else:
            print("file not found")
    elif cmd == "put":
        put(wish)    # calls put function
    elif cmd == "mput":
        files = action.split(' ')
        if len(wish) > 0:    # calls put function multiple times until all requested files have been addressed
            for length in range(len(files)):
                if files[length] != "mput":
                    put(files[length])
        else:
            print("Please enter files")
            s.send("Please enter files".encode())
    elif cmd == "mget":
        files = action.split(' ')
        for length in range(len(files)):
            if files[length] != "mget":
                answer = s.recv(4096).decode()
                print(answer)    # Runs a for loop and prepares to accept incoming files and write them to files
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
        print(s.recv(1024).decode())    # Accepts invalid input information
    if cmd == "quit":
        print('Shutting down...')   # Shuts it down
        quit()
