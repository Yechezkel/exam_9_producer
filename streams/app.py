import json
from kafka import KafkaConsumer, KafkaProducer

print("the streams server started")

TOPIC_NAME = "try"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='1',
    value_deserializer=lambda m: json.dumps(m.decode('utf-8')),
)

# producer = KafkaProducer(bootstrap_servers='localhost:9092')

for message in consumer:
    data = message.value
    print(f"Received message: {data}")
















#
# # app.debug = True
#
# print("the server started")  # to remove
#
#
#
# if __name__ == '__main__':
#     app.run(
#         host='0.0.0.0',
#         port=5001,
#         debug=True
#     )