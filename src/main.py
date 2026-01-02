from typing import Any
import requests

url: str = "https://api.deezer.com/playlist/"
quit: bool = False

while not quit:
    playlist_id = ""
    while not playlist_id:
        playlist_id = input("Enter playlist id> ")

    print("Searching...")

    r: requests.Response = requests.get(url+playlist_id.strip())
    try:
        data: dict[str, Any] = r.json()
    except:
        print("Failed to decode JSON")
        continue

    error = data.get("error")
    if error:
        print(f"""
              An error occurred!
              Type: {error.get("type")}
              Message: {error.get("message")}
              """)
        continue

    title = data.get("title", "No title")
    tracks = data.get("tracks", {}).get("data", [])

    result = f"{title}\n"
    for track in tracks:
        track_title = track.get("title", "No title")
        artist_name = track.get("artist", {}).get("name", "Unknown artist")
        result += f"{track_title} - {artist_name}\n"

    print(f"------------------------------\n{result}------------------------------")