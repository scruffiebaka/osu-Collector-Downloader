import requests
import re
import urllib.parse
import time
import os
import window
import jsonprocessor

def get_beatmap_collection(beatmapsetid):
    
    url = "https://osucollector.com/api/collections/" + beatmapsetid
    
    try:
        response = requests.get(url, params={})
        response.raise_for_status()
        
        try:
            return response.json()
        except:
            window.error("Something went wrong...", callback=None)
            return None
            
    except requests.HTTPError as e:
        window.error(f"Failed to get beatmaps from osu!collector. Please ensure beatmap ID is correct.", callback=None)
        return None

def get_beatmap_file(path, id):
    retry_limit = 5
    for attempt in range(retry_limit):
        url = f"https://catboy.best/d/{id}"
        try:
            headers = {
                "Accept": "*/*"
            }
            response = requests.get(url, stream=True, headers=headers)
            if(response.status_code == 429):
                window.warning("Ratelimit reached. On bystand for 2 minutes.")
                time.sleep(120)
                continue
            elif(response.status_code == 200):
                match = re.search(r'filename="(.+)"', response.headers.get('Content-Disposition', ''))
                beatmapname = os.path.join(path, urllib.parse.unquote(match.group(1)))
                content_length = int(response.headers.get('Content-Length', 0))
                
                with open(beatmapname, 'wb') as beatmap:
                    downloaded = 0
                    start_time = time.time()
                    
                    for chunk in response.iter_content(chunk_size=1024):
                        if(chunk):
                            beatmap.write(chunk)
                            downloaded += len(chunk)
                            
                            percent_downloaded = (downloaded/content_length) * 100
                            elapsed_time = time.time() - start_time
                            download_speed = downloaded / elapsed_time / 1024
                            
                            window.canvas.itemconfig(window.name_text, text=urllib.parse.unquote(match.group(1)))
                            window.canvas.itemconfig(window.size_text, text=f"{content_length / 1024 / 1024:.2f} MB")
                            window.canvas.itemconfig(window.progress_text, text=f"{percent_downloaded:.2f}% - {downloaded / 1024 / 1024:.2f} MB / {content_length / 1024 / 1024:.2f} MB")
                            window.canvas.itemconfig(window.speed_text, text=f"{download_speed:.2f} KB/s")
            else:
                continue
            return "ok"
        except requests.RequestException as e:
            print("Retrying...")
    return "error"

def init_downloader(id, location):
    window.disable_button()
    
    # Declare info
    global name, description
    
    if(location == None or os.path.exists(location) == False):
        window.error("Please enter a valid location.", callback=None)
        return
    
    def fetch_beatmap_list():
        print("Fetching beatmaps")
        data = get_beatmap_collection(id)
        if(data == None):
            return None
        return jsonprocessor.parse_beatmap_data(data)

    # Fetch the beatmap list
    beatmaplist = fetch_beatmap_list()
    if(beatmaplist == None or len(beatmaplist) < 1):
        window.error("Beatmaplist is empty :(", callback=None)
        return
    print(beatmaplist)
    # Set the info
    name = jsonprocessor.name
    description = jsonprocessor.description
    
    # Start the beatmap downloading
    def start_beatmap_download():
        window.canvas.itemconfig(window.setname_text, text=f"Downloading: {name}")
        if (os.path.exists(os.path.join(location, name)) == False):
            os.mkdir(os.path.join(location, name))
        for beatmap in beatmaplist:
            result = get_beatmap_file(os.path.join(location, name), beatmap)
            if(result == "error"):
                return None
            elif(result == "fail"):
                window.info("Download has been skipped due to an error.")
                continue
            window.progress['value'] = (((beatmaplist.index(beatmap) + 1)/len(beatmaplist)) * 100)
        return "success"
    
    target = start_beatmap_download()
    if(target == None):
        window.error("Something went wrong, please try again later.", callback=None)
        return
    
    window.info("Downloads completed :3")
    window.progress['value'] = 0
    window.enable_button()