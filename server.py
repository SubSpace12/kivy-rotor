import socket			

s = socket.socket()		
print ("Socket successfully created")

port = 3333			
s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")

while True:
    conn, addr = s.accept()
    dataFromClient = conn.recv(1024).decode()
    
    if dataFromClient == "went left":
        conn.send("Rotor turned left".encode())
    else:
        conn.send("Rotor turned right".encode())

conn.close()
        