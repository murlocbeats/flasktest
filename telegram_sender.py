import requests

# تابع برای ارسال پیام
def send_message(text):
    # اطلاعات ربات و کاربر
    bot_token = '7379827277:AAGIBu-tB1N4W6YEnoxPzFHXMFCFZ2WWcy0'
    chat_id = '441994773'

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    print('message sent!')
    return response.json()
