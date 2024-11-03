from colorama import Fore
from logo import display_logo
import os
import yt_dlp

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_youtube(s: str):
    clear_screen()
    display_logo()
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(f"ytsearch10:{s}", download=False)['entries']
    return results

def display_results(results):
    print("\n")
    for count, video in enumerate(results, start=1):
        print(Fore.MAGENTA + f"{count}. {video['title']}")

def resolution_options():
    print("\n")
    options = Fore.MAGENTA + '''
    1.  Low Resolution
    2.  Medium Resolution
    3.  High Resolution
    '''
    print(options)

def format_options():
    print("\n")
    options = Fore.MAGENTA + '''
    1.  MP4 (Video)
    2.  MP3 (Audio)
    '''
    print(options)

def download_video(url: str, resolution: str):
    ydl_opts = {
        'ffmpeg_location': 'C:\ffmpeg\bin',
        'format': resolution,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(Fore.GREEN + "Video download completed!")

def download_audio(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(Fore.GREEN + "Audio download completed!")

def download(type: int, resolution: int, url: str):
    resolutions = {
        1: 'worstvideo',  # Low Resolution
        2: 'bestvideo[height<=360]',  # Medium Resolution
        3: 'bestvideo[height<=720]',  # High Resolution
    }
    if type == 1:  # Video
        download_video(url, resolutions[resolution])
    elif type == 2:  # Audio
        download_audio(url)

def display_details(video):
    clear_screen()
    display_logo()
    print("\n")
    print(Fore.BLUE + f"Title     : {video['title']}")
    print(Fore.BLUE + f"Channel   : {video['uploader']}")
    print(Fore.BLUE + f"Duration  : {video['duration']} seconds")
    print(Fore.BLUE + f"Views     : {video['view_count']}")
    print(Fore.BLUE + f"Published : {video['upload_date']}")
    print(Fore.BLUE + f"URL       : {video['webpage_url']}")
    return video['webpage_url']

def main():
    while True:
        clear_screen()
        display_logo()
        
        search = input(Fore.YELLOW + "Search : ")
        results = search_youtube(search)
        display_results(results)
        
        print("\n")
        choose_song = int(input(Fore.YELLOW + "Choose Title : "))
        
        selected_video = results[choose_song-1]
        url = display_details(selected_video)

        format_options()
        choose_format = int(input(Fore.YELLOW + "Choose Format : "))
        
        resolution_options()
        choose_resolution = int(input(Fore.YELLOW + "Choose Resolution : "))
        
        clear_screen()
        display_logo()
        
        display_details(selected_video)

        download(type=choose_format, resolution=choose_resolution, url=url)
        
        print("\n")
        input(Fore.RED + "Press Enter to continue...")

if __name__ == "__main__":
    main()