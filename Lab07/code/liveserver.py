# Live Server
import socket
from time import ctime


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setblocking(0)
mysocket.settimeout(60)
mysocket.bind(('', 9998)) # leave the host IP empty '', it will bind to any IP

while True:
    mysocket.listen(5)
    conn, addr = mysocket.accept()
    while True:
        data = conn.recv(1000)
        print(len(data))
        text = data.decode('utf-8').strip()
        if not text or text == 'END':
            break
        #print(data.decode('utf-8'), len(data.decode('utf-8')))
        print("Received from client: %s" % text)
        print("Sending the server time to client: %s"  %ctime())
        try:
            conn.send(bytes('Time: ', 'utf-8'))
            conn.send(bytes(ctime(), 'utf-8'))
            conn.send(bytes(' Received: ', 'utf-8'))
            conn.sendall(bytes(text, 'utf-8'))
            conn.send(bytes('\n\n', 'utf-8'))
        except KeyboardInterrupt:
            print("Exited by user")
    conn.close()
mysocket.close()
