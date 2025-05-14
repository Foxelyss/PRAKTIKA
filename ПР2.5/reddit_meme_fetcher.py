import json
import random
from datetime import datetime

import requests


def get_meme_image():
    history = load_history()

    current_date = datetime.today()

    if (current_date - datetime.strptime(history["date"], "%Y-%m-%d")).days > 8:
        base_url = 'https://memesapi.vercel.app/give/ProgrammerHumor/100'
        response = requests.get(base_url)
        data = response.json()
        data["date"] = str(current_date.date())

        with open("meme_cache.json", "w", encoding='utf8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        return random.choice(data["memes"])

    return random.choice(history["memes"])


def load_history():
    try:
        with open("meme_cache.json", "r", encoding='utf8') as file:
            return json.load(file)
    except:
        return {"date": "2007-01-01"}