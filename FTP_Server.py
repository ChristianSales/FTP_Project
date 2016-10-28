import socket, re, os, glob, gzip, select


connection = True
mainDir = "D://"
currentDir = mainDir
os.chdir(mainDir)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 21))
s.listen(1)
c, addr = s.accept()
print('Got connection from', addr)
"""
while connection:


    s.send(os.getcwd().encode) """
data = c.recv(1024).decode()
info = ""
if data == "ls":
        for length in range(len(os.listdir(currentDir))):
            info += (os.listdir(currentDir)[length] + " \n")
print(info)
c.send(info.encode())
   # if userInput == "cd":


