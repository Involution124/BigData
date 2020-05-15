from kafka import KafkaProducer
from keras.datasets import mnist

import os
import sys

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Connect to Kafka
kafka_host = os.getenv('KAFKA_HOST_NAME')
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

# Setup Kafka Producer
producer = KafkaProducer(bootstrap_servers=kafka_host)
numIterations = 0
for x_test as test:
    numIterations = numIterations+1
    # Stop after 50 iterations
    if(numIterations >= 50):
        exit(0)
    b = test1.tobytes()
    print("Message sent")
    response = producer.send('images', b)
    print("Response = " + str(response))
    result = response.get(timeout=30)
    print("Fetched Message = " + str(result))


