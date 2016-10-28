import socket, re, os, glob, gzip, select



print("Attempting connection to server...")
try:
    s = socket.socket()
    s.connect(('Bills', 21))
    userInput = input()
    s.send(userInput.encode())
    data = s.recv(4086).decode()
    print(data)
except socket.gaierror:
    print("Connection Failed")
    quit()

print("Connection Successful!")
connection = True
"""
while connection:
    try:
        s = socket.socket()
        s.connect(('Bills', 21))
        s.send('ls'.encode)
    except socket.gaierror:
        print("Connection Failed")
        connection = False



  userInput = input()
  s.send(userInput)
  userInput = input()
  if userInput == "ls":

  if userInput == "cd": """




