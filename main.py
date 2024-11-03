from colorama import Fore
from logo import display_logo
import os
from youtube_search import YoutubeSearch


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
    
def Download(Type: int , Resolution : int, url : str):
    if Type == 1:
        if Resolution == 1:
            ...
        elif Resolution == 2:
            ...
        elif Resolution == 3:
            ...
    elif Type == 2:
        if Resolution == 1:
            ...
        elif Resolution == 2:
            ...
        elif Resolution == 3:
            ...
            
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
    
def main():
    while True:
        clear_screen()
        display_logo()
        
        search =  input(Fore.YELLOW + "Search : ")
        Search(search)
        
        print("\n")
        
        Choose_Song = int(input(Fore.YELLOW + "Choose Title : "))
        
        title = titles[Choose_Song-1]
        
        Details(title)
        
        Format_options()
        
        choose_format = int(input(Fore.YELLOW + "Choose  Format : "))
        
        Resolution_options()
        
        choose_resolution = int(input(Fore.YELLOW + "choose  Resolution : "))
        
        clear_screen()
        display_logo()
        
        Details(title)

        Download(Type=choose_format , Resolution=choose_resolution , url=Url)
        
        print("\n")
        input(Fore.RED + "Press Enter to  continue...")
    
main()