import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
API_KEY = os.getenv("APi_KEY")  # Sua chave
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():

    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)
        response.raise_for_status()  # Gera exceção se status != 200

        data = response.json()
        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print(channel_playlistId)
        
        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()
