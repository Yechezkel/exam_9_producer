import json
from kafka import KafkaConsumer, KafkaProducer
from mongo_db import insert_data


CONSUMER_TOPIC_NAME = "try_all"
PRODUCER_TOPIC_NAME = "try_suspected"

consumer = KafkaConsumer(
    CONSUMER_TOPIC_NAME,
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='1',
    value_deserializer=lambda m: json.dumps(m.decode('utf-8')),
)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for message in consumer:
    data = message.value
    print(f"Received message: {data}")
    insert_data(data)
    print("the message inserted into mongo-db")
    producer.send(PRODUCER_TOPIC_NAME, data)
    print("producer sent")
