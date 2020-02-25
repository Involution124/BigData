from kafka import KafkaConsumer
import os
import sys
import subprocess

print("Here");
kafka_host = os.getenv('KAFKA_HOST_NAME')
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

print("Got here!")
numIterations = 0;
consumer  = KafkaConsumer("images", group_id="processor",  bootstrap_servers=kafka_host)
print("Consumder set up")
iterator = iter(consumer);
print(iterator);
print(next(iterator, b"A"));
for message in consumer:
    pass ; 
    print("Message : ) ")
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))
    f = open("/tmp/parsed-image.jpg", "wb")
    f.write(message.value)
    f.close();
    process = subprocess.Popen("Darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3_weights -i 0 -thresh 0.25 ./tmp/parsed-image.jpg")
    process.wait();"
