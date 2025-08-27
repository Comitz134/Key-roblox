# server.py
from flask import Flask
from datetime import datetime
import hashlib

app = Flask(__name__)

def get_daily_key():
    hoje = datetime.utcnow().strftime("%Y-%m-%d")  # AAAA-MM-DD
    key = hashlib.md5(hoje.encode()).hexdigest()[:10]  # pega 10 chars
    return key

@app.route("/dailykey")
def dailykey():
    return get_daily_key()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
