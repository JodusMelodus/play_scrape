import requests

playlist_id: str|None = None
url: str = f"https://api.deezer.com/playlist/{playlist_id}"

r: requests.Response = requests.get(url)
data = r.json()
result: str = ""

result += str(data["title"]) + '\n'
for track in data["tracks"]["data"]:
    result += str(f"{track["title"]} - {track["artist"]["name"]}") + '\n'

print(result)