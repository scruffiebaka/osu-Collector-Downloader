import requests
from window import error

def get_beatmap_collection(beatmapsetid):
    
    url = "https://osucollector.com/api/collections/" + beatmapsetid
    
    try:
        response = requests.get(url, params={})
        response.raise_for_status()
        
        try:
            return response.json()
        except:
            error("Something went wrong...", callback=None)
            return None
            
    except requests.HTTPError as e:
        error(f"Failed to get beatmaps from osu!collector. Please ensure beatmap ID is correct.", callback=None)
        return None