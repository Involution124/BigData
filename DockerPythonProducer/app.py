from kafka import KafkaProducer
import os
import sys
kafka_host = os.getenv('KAFKA_HOST_NAME')
os.system("env");
if(kafka_host == None):
    print("Failed, no KAFKA_HOST_NAME environment variable was set")
    sys.exit(1)

producer = KafkaProducer(bootstrap_servers=kafka_host)
for _ in range(21):
    print("Message sent")
    response = producer.send('images', b'some_message_bytes')
    print("Resposne = " + str(response))
    print("Fetching the message");
    result = response.get(timeout=30)
    print("Result = " + str(result))


