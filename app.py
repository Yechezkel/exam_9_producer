from flask import Flask, jsonify, request
from services import validate_body_data
from producer import produce_email_data

app = Flask(__name__)


@app.route('/api/email', methods=[ 'POST'])
def listen_to_email():
    data = request.get_json()
    if validate_body_data(data) == False:
        return jsonify({"error": "Invalid data"}), 400
    try:
        produce_email_data(data)
        return jsonify({"message": "Succeeded"}), 201
    except Exception as e:
        print(f"en error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500


if __name__ == '__main__':
    app.run()