import yt_dlp

url = input("Enter YouTube URL: ")

print("\nChoose format:")
print("1. 1080p")
print("2. 720p")
print("3. 480p")
print("4. Audio only (MP3)")

choice = input("Enter choice: ")

if choice == "1":
    fmt = "bestvideo[height=1080]+bestaudio/best[height=1080]"
elif choice == "2":
    fmt = "bestvideo[height=720]+bestaudio/best[height=720]"
elif choice == "3":
    fmt = "bestvideo[height=480]+bestaudio/best[height=480]"
elif choice == "4":
    fmt = "bestaudio"
else:
    print("Invalid choice")
    exit()

ydl_opts = {
    'format': fmt,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
}

if choice == "4":
    ydl_opts.update({
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    })


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
