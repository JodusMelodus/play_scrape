import requests
import json

playlist_id: str|None = None
url: str = f"https://api.deezer.com/playlist/{playlist_id}"

r: requests.Response = requests.get(url)
data = r.json()

# Save data to playlist.json
with open("playlist.json", "w", encoding="utf-8") as f:
    string_data = str(data).replace("'", "\"").replace("True", "true").replace("False", "false")
    json.dump(json.loads(string_data), f, indent=4)


print(data["title"])
for track in data["tracks"]["data"]:
    print(f"{track["title"]} - {track["artist"]["name"]}")