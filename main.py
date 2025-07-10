import requests
import time
import json
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_API_URL = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
TELEGRAM_USER_ID = <YOUR_TELEGRAM_USER_ID>

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    message = f"🚨 إشعار جديد من TradingView:\n{json.dumps(data)}"
    requests.post(TELEGRAM_API_URL, data={
        "chat_id": TELEGRAM_USER_ID,
        "text": message
    })
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)