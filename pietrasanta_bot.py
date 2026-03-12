from playwright.sync_api import sync_playwright
import requests
import time

TOKEN = "8746742027:AAHrUjaLmSlKEygSsVDPBrBX-ihP3YzJJB0"
CHAT_ID = "8557654793"

URL = "https://www.comune.pietrasanta.lu.it/it/book"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    while True:

        page.goto(URL)

        content = page.content()

        if "Edilizia privata" in content and "Disponibile" in content:

            send_telegram("⚠️ Slot disponibile EDILIZIA PRIVATA Pietrasanta!")

            print("slot trovato")

        else:

            print("nessuno slot")

        time.sleep(10)