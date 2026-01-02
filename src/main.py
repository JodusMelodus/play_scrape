from typing import Any
import requests

url: str = "https://api.deezer.com/playlist/"
quit: bool = False

print("""
Hello, Welcome to Play Scrape.
The free, open-source tool that lets you quickly export any public Deezer playlist to a plain text file.

1. Open the Deezer playlist you want to export.
2. Copy the playlist URL from your browser.
3. Paste the URL when prompted.
5. Press Enter

Your playlist will be saved as playlist.txt.
Press Ctrl + C at any time to exit.
""")

while not quit:
    playlist_url = ""
    while not playlist_url:
        playlist_url = input("Enter playlist URL> ")

    parts = playlist_url.split('/')
    playlist_id = parts[-1]

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

    print("Extracting...")
    title = data.get("title", "No title")
    tracks = data.get("tracks", {}).get("data", [])

    result = f"{title}\n"
    for track in tracks:
        track_title = track.get("title", "No title")
        artist_name = track.get("artist", {}).get("name", "Unknown artist")
        track = f"{track_title} - {artist_name}\n"
        result += track
        print(track, end="")
        
    with open("playlist.txt", "w") as f:
        f.write(result)

    print("--------------------------------------------------------------------------")