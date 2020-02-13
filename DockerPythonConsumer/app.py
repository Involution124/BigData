from kafka import KafkaConsumer
import os
import sys

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
#for message in consumer:
#    pass ; 
#    print("Message : ) ")
#    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))
