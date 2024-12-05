from flask import Flask, render_template, request
import requests

app = Flask(__name__)
BACKEND_URL = "http://backend:5001"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        requests.post(f"{BACKEND_URL}/messages", json={"name": name, "message": message})
    
    response = requests.get(f"{BACKEND_URL}/messages")
    messages = response.json()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

