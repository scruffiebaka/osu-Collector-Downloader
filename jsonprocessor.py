import json
from window import error

name = None 
description = None

def parse_beatmap_data(rawdata):
    try:
        global name, description
        name = rawdata.get("name", "")
        description = rawdata.get("description", "")
        
        beatmapsetids = []
        for beatmapset in rawdata.get("beatmapsets", []):
            beatmapsetid = beatmapset.get("id")
            if(beatmapsetid != None):
                beatmapsetids.append(beatmapsetid)
        return beatmapsetids
    except Exception as e:
        error(f"Something went wrong: {e}", callback=None)
        return None