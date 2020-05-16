from kafka import KafkaConsumer
from kafka import KafkaProducer
import os
import sys
import time
import tempfile
import subprocess
import socket
import tensorflow as tf
from tensorflow import keras
import numpy as np
import io
print("We are here");
kafka_host = os.getenv('KAFKA_HOST_NAME')
if(kafka_host == None):
    kafka_host = "kafka-service-train";

consumer  = KafkaConsumer("models-to-fit", group_id="worker",  request_timeout_ms=120000,session_timeout_ms=100000, bootstrap_servers=kafka_host)

while(1):
    print("Starting the worker process");
    for message in consumer:
        print("Waiting for message");
        bytestream = bytes(message.value)
        file_like_object = io.BytesIO(bytestream)
        tar = tarfile.open(fileobj=file_like_object)
        for member in tar.getmembers():
            f = tar.extractfile(member);
            print("F = " + str(f));
        break;

    print("Model receieved");
    model = keras.models.load_model("/model.h5")

    input_x = np.fromfile("input_x"); 
    input_y = np.fromfile("input_y");
    print("X and Y are loaded", str(input_x.shape), str(input_y.shape));

    metadata_file = open("metadata");
    metadata = json.load(metadata_file);
    metadata_file.close();
    print("Metadata has been received, = " + str(metadata));
    index =  metadata["index"];
    training_epochs = metadata["training_epochs"];
    validation_split = metadata["validation_split"];
    
    score = model.fit(input_x, input_y, epochs=training_epochs, validation_split=validation_split, batch_size=128)
    producer = KafkaProducer(bootstrap_servers=kafka_host)
    print("index, score = ", + str(index) + " "  + str(score));
    producer.send('models-fitted', {index: score})
    print("Resposne = " + str(response))
    result = response.get(timeout=30)
    print("Result = " + str(result))


