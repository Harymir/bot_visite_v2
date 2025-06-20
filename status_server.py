#!/usr/bin/env python3

from flask import Flask
import os

app = Flask(__name__)

@app.route("/status")
def status():
    return {"status": "running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
