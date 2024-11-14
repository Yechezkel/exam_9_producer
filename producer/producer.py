import json
from kafka import KafkaProducer


PRODUCER = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
TOPIK_NAME = "try"


def produce_email_data(data):
    print("Message produced")
    PRODUCER.send(TOPIK_NAME, data)

