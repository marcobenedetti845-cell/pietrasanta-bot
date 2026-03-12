import requests
import time

TOKEN = "IL_TUO_TOKEN"
CHAT_ID = "8557654793"

URL = "https://www.comune.pietrasanta.lu.it/it/book"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

send("🤖 Bot Pietrasanta avviato")

while True:

    try:

        r = requests.get(URL)

        html = r.text

        if "Edilizia privata" in html and "Disponibile" in html:

            send("⚠️ SLOT DISPONIBILE EDILIZIA PRIVATA PIETRASANTA\nhttps://www.comune.pietrasanta.lu.it/it/book")

            time.sleep(120)

        else:

            print("nessuno slot")

    except Exception as e:

        print(e)

    time.sleep(10)
