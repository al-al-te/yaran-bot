from flask import Flask, request
import os
from modules.excel_writer import append_to_excel
from modules.ocr_passport import extract_passport_info
from modules.validator import validate_national_id, validate_passport_number

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_update():
    data = request.get_json()

    # بررسی اینکه پیام از نوع متنی باشه
    message = data.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if text and chat_id:
        print(f"✅ پیام جدید: {text} از {chat_id}")
        # پاسخ خودکار ساده
        send_message(chat_id, "✅ پیام شما دریافت شد. لطفاً اطلاعات خواسته‌شده را ارسال نمایید.")
    
    return "ok", 200

# تابع ارسال پیام به کاربر
def send_message(chat_id, text):
    import requests
    token = os.getenv("BOT_TOKEN")
    url = f"https://tapi.bale.ai/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    print("🚀 Bot is running...")
    app.run(host='0.0.0.0', port=5000)
