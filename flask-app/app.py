from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/static/asset')
def serve_asset(filename):
    return send_from_directory('static/assets', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)