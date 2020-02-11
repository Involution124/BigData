from kafka import KafkaProducer
import os
import sys
import tarfile
import urllib.request

dataURL = "https://zenodo.org/record/815657/files/P2E_S5.tar.xz"
dataFileName = "file.tar.xz"
kafka_host = os.getenv('KAFKA_HOST_NAME')
os.system("env");
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

urllib.request.urlretrieve(dataURL, dataFileName)
tar = tarfile.open(dataFileName, "r:xz")
tar.extractall()
tar = tarfile.open("P2E_S5_C1.tar.xz", "r:xz")
tar.extractall()
print("Extracted data")
producer = KafkaProducer(bootstrap_servers=kafka_host)
for filename in os.listdir("P2E_S5_C1.1"):
    with open("P2E_S5_C1.1/" + filename, "rb") as image:
        f = image.read()
        b = bytearray(f) 
        print("Message sent")
        response = producer.send('images', b)
        print("Resposne = " + str(response))
        print("Fetching the message");
        result = response.get(timeout=30)
        print("Result = " + str(result))


