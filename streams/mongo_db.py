from pymongo import MongoClient
from contextlib import contextmanager

@contextmanager
def get_db():
    client = MongoClient('mongo', 27017)
    db = client['emails']
    try:
        yield db
    finally:
        client.close()


def insert_data(data):
    with get_db() as db:
        try:
            db['all_messages'].insert_one(data)
        except Exception as e:
            print(f"an error occurred while inserting a message into mongo error: {e}")
