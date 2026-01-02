# Play Scrape

![Python](https://img.shields.io/badge/Python-3.14.2-blue)
![Deezer](https://img.shields.io/badge/Deezer-💜-000000?logo=deezer&logoColor=white)

**Play Scrape** is a free, open-source tool that lets you quickly export any public Deezer playlist to a plain text file.

## ✨ Features

- Export Deezer playlists in seconds
- Simple, command-line workflow
- Saves results to a reusable playlist.txt file
- Open source, lightweight, no clutter

## 🛠️ Installation

1. Make sure you have [Python](https://www.python.org/) installed (3.14.2+).
2. Clone or Download this repository.
3. Install any required dependencies:
```bash
pip install requests
```

## 🚀 Usage

Run the script from the project root:
```bash
python src/main.py
```
Then follow the prompts:
1. Open the Deezer playlist you want to export.
2. Copy the playlist URL from your browser.
3. Paste the URL when prompted.
5. Press **Enter**

Your playlist will be saved as `playlist.txt`.
> Press **Ctrl + C** at any time to exit.

## 📄 Output format

The exported file contains one track per line:

```txt
Playlist Title
Track Title - Artist
```

## ⚠️ Notes

- Only works with **public playlists**.
- Internet connection required.
- If something fails double-check the URL.
