from kafka import KafkaConsumer
import os
import sys
import time
import socket
from tensorflow import keras
import numpy as np

print("We are here");
kafka_host = os.getenv('KAFKA_HOST_NAME')
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

if __name__ == "__main__":

    HOST, PORT = "trainer-model-service", 80
    data = "my data"
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
        sock.sendall(bytes(data + " ", "utf-8"))
        # Receive data from the server and shut down
        print("Receiving the model:");
        received = b'';
        numReceived = 0 ;
        while True:
            data = sock.recv(1048576);
            print("Recevied data, len = " + str(len(data)) + ", this is byte num " + str(numReceived) + "\n");
            numReceived+=1;
            if not data: break
            received += data;
        sock.close()
        break


    print("Len = " + str(len(received)));
    f = open('/model.h5', 'wb')
    f.write(received)
    f.close()
    print("Model receieved");
    model = keras.models.load_model("/model.h5")

    consumer  = KafkaConsumer("images", group_id="processor",  request_timeout_ms=120000,session_timeout_ms=100000, bootstrap_servers=kafka_host)

    for message in consumer:
       bytestream = bytes(message.value)
       newer = np.frombuffer(bytestream, dtype=np.uint8)
       newer = newer.reshape((28,28))
       newer = np.expand_dims(newer, axis=0)
       newer = np.expand_dims(newer, axis=3)
       scores = model.predict(newer);
       print("Prediction = " + str(scores));

