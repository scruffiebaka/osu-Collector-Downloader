import window
import threading


def download(id, location):
    window.disable_button()
    
    # Fetch the beatmap list first and then turn it into a list
    beatmaplist = []
    
    def fetch_beatmap_list():
        print("Fetching list")
        beatmaplist.append("Testbeatmap")

    threading.Thread(target=fetch_beatmap_list).start()
    
    print(beatmaplist)
    
    # Start the beatmap downloading
    def start_beatmap_download():
        print("Downloading beatmaps")
        for beatmap in beatmaplist:
            print(f"{beatmap} downloaded")
    threading.Thread(target=start_beatmap_download).start()
    
    window.enable_button()

window.init_window(download)