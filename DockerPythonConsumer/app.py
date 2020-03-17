# from kafka import KafkaConsumer
# import os
# import sys

# print("Here");
# kafka_host = os.getenv('KAFKA_HOST_NAME')
# if(kafka_host == None):
#     print("Failed, no KAFKA_HOST_NAME environment variable was set")
#     sys.exit(1)

# print("Got here!")
# numIterations = 0;
# consumer  = KafkaConsumer("images", group_id="processor",  bootstrap_servers=kafka_host)
# print("Consumder set up")
# iterator = iter(consumer);
# print(iterator);
# print(next(iterator, b"A"));
# for message in consumer:
#     pass ; 
#     print("Message : ) ")
#     print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))



from kafka import KafkaConsumer
import os
import sys
import tempfile
import subprocess

kafka_host = os.getenv('KAFKA_HOST_NAME')
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

# def get_image(parsed_kafka_msg):
#     cache = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg", prefix="classify")
# #    req = urllib.request.urlopen(parsed_kafka_msg["url"])
#     cache.write(parsed_kafaka_msg)
#     cache.close()
#     return cache

if __name__ == "__main__":
    print("starting main")
    cmd = 'Darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 {file}'
    consumer  = KafkaConsumer("images", group_id="processor",  request_timeout_ms=120000, 
                                session_timeout_ms=100000, bootstrap_servers=kafka_host)
#     iterator = iter(consumer)
#     next(iterator, b"A")
#     for message in consumer:
#         pass
#         print("Message: ")
#         print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))




    print("Got here!")
# numIterations = 0;
# consumer  = KafkaConsumer("images", group_id="processor",  bootstrap_servers=kafka_host, api_version=(0,10))
# print("Consumer set up")
#iterator = iter(consumer);
#print(iterator);
#print(next(iterator, b"A"));
    for message in consumer:
        #pass ; 
        #print("Message : ) ")
        #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))
        print("Got to pre-cache")
        # filecache = get_image(message.value)
        cache = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg", prefix="classify")
#       req = urllib.request.urlopen(parsed_kafka_msg["url"])
        cache.write(bytes(message.value))
        cache.close()
        filecache = cache
        process = subprocess.Popen(cmd.format(file=os.path.abspath(filecache.name)), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        out, err = process.communicate()
        print("Got to post-cache")
        print("stdout: %s", out)
        print("stderr: %s", err)
        filecache.close()
        print("finished cache")

# def get_image(parsed_kafka_msg):
#     cache = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg", prefix="classify")
# #    req = urllib.request.urlopen(parsed_kafka_msg["url"])
#     cache.write(parsed_kafaka_msg)
#     cache.close()
#     return cache
# # #    print("file starting write");
# # #    f = open("/tmp/parsed-image.jpg", "wb")
# # #    f.write("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))
# # #    f.close();
# # #    print("file written");
# # #    process = subprocess.Popen("Darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3_weights -i 0 -thresh 0.25 ./tmp/parsed-image.jpg")
# # #    process.wait();
