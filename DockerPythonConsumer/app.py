from kafka import KafkaConsumer
import os
import sys
import time
import tempfile
import subprocess

kafka_host = os.getenv('KAFKA_HOST_NAME')
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

if __name__ == "__main__":
    cmd = '/usr/local/bin/darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 {file}'

    consumer  = KafkaConsumer("images", group_id="processor",  request_timeout_ms=120000,
                                session_timeout_ms=100000, bootstrap_servers=kafka_host)

    for message in consumer:
        cache = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg", prefix="classify")
        cache.write(bytes(message.value))
        cache.close()
        filecache = cache
        process = subprocess.Popen(cmd.format(file=os.path.abspath(filecache.name)).split(), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        out, err = process.communicate()
        print("stdout: %s", out)
        print("stderr: %s", err)
        print("exited detection")
        filecache.close()
