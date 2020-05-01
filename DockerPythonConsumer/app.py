from kafka import KafkaProducer
import os
import sys
import tarfile
import urllib.request

import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

kafka_host = os.getenv('KAFKA_HOST_NAME')

if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)
    
producer = KafkaProducer(bootstrap_servers=kafka_host)
numIterations = 0
for x_test as test:
    numIterations = numIterations+1
    if(numIterations >= 50):
        exit(0)
    b = test.tobytes()
    print("Message sent")
    response = producer.send('images', b)
    print("Resposne = " + str(response))
    print("Fetching the message");
    result = response.get(timeout=30)
    print("Result = " + str(result))
    

