import json
from kafka import KafkaProducer

TOPIK_NAME = "try_all"

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



def produce_email_data(data):
    print("Message produced")
    producer.send(TOPIK_NAME, data)


