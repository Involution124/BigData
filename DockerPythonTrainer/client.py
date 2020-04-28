import socket
import sys
import time 
HOST, PORT = "localhost", 9999

data = "aaa \n"
# Create a socket (SOCK_STREAM means a TCP socket)




while 1:
    try:
        # Connect to server and send data
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except socket.error:
        print("Couldn't connect to server, no model available");
        time.sleep(5);
        sock.close();
        continue
    
    sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
    sock.close()
    break 

print("Sent:     {}".format(data))
print("Received: {}".format(received))

