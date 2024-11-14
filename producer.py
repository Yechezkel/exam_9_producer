import json
from kafka import KafkaProducer


PRODUCER = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
TOPIK_NAME = "try"


def produce_email_data(data):
    PRODUCER.send(TOPIK_NAME, data)
    print("Message produced")

