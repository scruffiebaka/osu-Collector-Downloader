import os
import threading
import window
import helper
from requestor import get_beatmap_collection
import jsonprocessor

# Create download folder on start
if(os.path.exists(helper.resource_path("Downloads")) == False):
    os.mkdir(helper.resource_path("Downloads"))

window.default_location = helper.resource_path("Downloads")

def download(id, location):
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
    
    # Set the info
    name = jsonprocessor.name
    description = jsonprocessor.description
    
    # Start the beatmap downloading
    def start_beatmap_download():
        print("Downloading beatmaps")
        for beatmap in beatmaplist:
            print(f"{beatmap} downloaded")
    
    # Threading stuff
    download_thread = threading.Thread(target=start_beatmap_download)
    download_thread.start()
    
    window.info("Downloads completed :3")

    # Enable the button after download
    window.enable_button()

window.init_window(download)