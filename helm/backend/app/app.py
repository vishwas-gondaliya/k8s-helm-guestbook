from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/messages", methods=["GET", "POST"])
def handle_messages():
    if request.method == "POST":
        data = request.json
        messages.append(data)
        return {"message": "Message added"}, 201
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

