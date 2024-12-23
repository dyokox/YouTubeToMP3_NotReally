from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.exceptions import VideoUnavailable
from pytubefix.exceptions import PytubeFixError
import promptlib


def main():
    while True:
        print("""MENU\n1. Audio Only\n2. Download playlist\n3. Exit""")
        choice = int(input("\n >> "))

        match choice:
            case 1:
                audioDownload()
            case 2:
                playlistDownload()
            case 3:
                break
            case _:
                print(f"{choice} is not valid.")
                continue

def audioDownload():
  
    try:
        url = str(input("URL\n>> "))
        prompter = promptlib.Files()
        yt = YouTube(url)
        audioDownload = yt.streams.get_audio_only()

    except VideoUnavailable:
        print("Failed to download")

    else:
        dir = prompter.dir()
        audioDownload.download(output_path=dir)
        print("Audio downloaded")

def playlistDownload():
    count = 0

    try:
        url = str(input("URL\n>> "))
        prompter = promptlib.Files()
        pl = Playlist(url)
        dir = prompter.dir()
        for video in pl.videos:
            pl = video.streams.get_audio_only()
            pl.download(output_path=dir)
            count += 1
        print(f"Downloaded {count} audio files.\nPlaylist downloaded")

    except PytubeFixError:
        print("Couldn't download playlist")
    except KeyError:
        print("Couldn't download playlist")

main()
