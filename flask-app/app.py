from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/asset/<path:path>')
def serve_asset(path):
    return send_from_directory('static/asset', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)