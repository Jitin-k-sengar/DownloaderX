from colorama import Fore
from logo import display_logo
import os
import requests
from youtube_search import YoutubeSearch
import yt_dlp as youtube_dl


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def Search(s : str):
    clear_screen()
    display_logo()
    count = 0
    global results
    results = YoutubeSearch(s, max_results=10).to_dict()
    global titles
    titles = [video['title'] for video in results]
    for title in titles:
        print(Fore.MAGENTA + f"{count+1}. {title}")
        count += 1
        
def Resolution_options():
    print("\n")
    options = Fore.MAGENTA + '''
    1.  Low Resolution
    2.  Medium Resolution
    3.  High Resolution
    '''
    print(options)
    print("\n")
    
def Format_options():
    print("\n")
    options = Fore.MAGENTA + '''
    1.  MP4 (Video)
    2.  MP3 (Audio)
    '''
    print(options)
    print("\n")
    
def Download(Type: int, Resolution: int, url: str):
    if Type == 1:  # Video
        if Resolution == 1:
            ydl_opts = {
                'format': 'bestvideo[height<=480]+bestaudio/best',  # Download 480p video
                'outtmpl': f'C:/Users/Jitin/Downloads/%(title)s.%(ext)s',
            }
        elif Resolution == 2:
            ydl_opts = {
                'format': 'bestvideo[height<=720]+bestaudio/best',  # Download 720p video
                'outtmpl': f'C:/Users/Jitin/Downloads/%(title)s.%(ext)s',
            }
        elif Resolution == 3:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'C:/Users/Jitin/Downloads/%(title)s.%(ext)s',
            }

    elif Type == 2:  # Audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'C:/Users/Jitin/Downloads/%(title)s.%(ext)s',
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Check connection before starting the download
            if not is_connected():
                print(Fore.RED + "Internet connection lost before download started.")
                return
            
            ydl.download([url])
            
            # You can also check the connection periodically (if you want).
            # However, this is not straightforward with yt-dlp as it does not provide hooks for this.
            # Instead, you can simply inform the user that they should ensure a stable connection.
            
        except Exception as e:
            print(Fore.RED + f"An error occurred during download: {e}")
            
def Details(title : str):
    clear_screen()
    display_logo()
    print("\n")
    for video in results:
        if video['title'] == title:
            print(Fore.BLUE + f"Title     : {video['title']}")
            print(Fore.BLUE + f"Channel   : {video['channel']}")
            print(Fore.BLUE + f"Duration  : {video['duration']}")
            print(Fore.BLUE + f"Views     : {video['views']}")
            print(Fore.BLUE + f"Published : {video['publish_time']}")
            print(Fore.BLUE + f"URL       : https://www.youtube.com" + video['url_suffix'])
            global Url
            Url = "https://www.youtube.com" + video['url_suffix']
    
def is_connected():
    try:
        # Attempt to connect to a website (e.g., Google)
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False
    
def main():
    if is_connected():
        
        while True:
            clear_screen()
            display_logo()
            
            while True:
                print("\n")
                search =  input(Fore.YELLOW + "Search : ")
                if is_connected():
                    Search(search)
                    break
                else:
                    print(Fore.RED + "Internet connection lost.")
                    input(Fore.RED + "Press Enter to Continue...")
            
            while True:
                try:
                    print("\n")
                    Choose_Song = int(input(Fore.YELLOW + "Choose Title (1 to {}): ".format(len(titles))))
                    if 1 <= Choose_Song <= len(titles):
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please choose a number between 1 and {}.".format(len(titles)))
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a number.")
            
            title = titles[Choose_Song-1]
            Details(title)
            Format_options()
            
            # Loop until a valid format is chosen
            while True:
                try:
                    choose_format = int(input(Fore.YELLOW + "Choose Format (1 or 2): "))
                    if choose_format in [1, 2]:
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please choose 1 for MP4 or 2 for MP3.")
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a number (1 or 2).")
            
            Resolution_options()
            
            # Loop until a valid resolution is chosen
            while True:
                try:
                    choose_resolution = int(input(Fore.YELLOW + "Choose Resolution (1, 2, or 3): "))
                    if choose_resolution in [1, 2, 3]:
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please choose 1 for Low, 2 for Medium, or 3 for High resolution.")
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a number (1, 2, or 3).")
                    
            clear_screen()
            display_logo()
            
            Details(title)
            
            print("\n")

            while True:
                if is_connected():
                    Download(Type=choose_format , Resolution=choose_resolution , url=Url)
                    break
                else:
                    print(Fore.RED + "No internet connection. Please check your connection and try again.")
                    input(Fore.RED + "Press Enter to Continue...")

            print("\n")
            input(Fore.RED + "Press Enter to  continue...")
    else:
        print(Fore.RED + "No internet connection. Please connect to the internet and try again.")
        print("\n")
        input(Fore.RED + "Press Enter to Continue...")

main()