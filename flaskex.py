from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/users')
def users():
    users = [
        { "username" : "thomas" },
        { "username" : "johanna" }
    ]
    return jsonify(users)