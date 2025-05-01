import requests

def return_json(beatmapsetid):
    
    url = "https://osucollector.com/api/collections/" + beatmapsetid
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, params={})
        if(response.status_code != 200):
            raise Exception(f"Status code = {response.status_code}")
        return response.json()
    except Exception as e:
        raise Exception("Failed.")