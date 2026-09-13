import os
import requests

def get_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url).json()
    if response.get("result") == "success":
        return response["rates"]["KRW"]
    raise Exception("환율 정보를 불러오는데 실패했습니다.")

def send_telegram_message(rate):
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    message = f"💱 [원/달러 일일 환율 알림]\n현재 USD/KRW: {rate:,.2f} 원"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)
    response.raise_for_status()

if __name__ == "__main__":
    rate = get_exchange_rate()
    send_telegram_message(rate)