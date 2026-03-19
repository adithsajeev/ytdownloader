# YouTube Downloader

A Python application for downloading YouTube videos in various quality formats and audio-only options.

## Features

- Download videos in 1080p, 720p, or 480p quality
- Extract audio as MP3
- Simple command-line interface

## Requirements

- Python 3.x
- yt_dlp
- FFmpeg (for audio extraction)

## Installation

1. Install dependencies:
```bash
pip install yt-dlp
```

2. Make sure FFmpeg is installed on your system.

## Usage

Run the script:
```bash
python main.py
```

Then follow the prompts:
1. Enter the YouTube URL
2. Select desired format (1080p, 720p, 480p, or MP3)
3. The video/audio will be downloaded to the `downloads/` folder

## Formats

- **1080p**: Full HD quality with best audio
- **720p**: HD quality with best audio
- **480p**: Standard quality with best audio
- **MP3**: Audio only in MP3 format

## License

This project is open source.
