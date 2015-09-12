import requests
import urllib

def get_comments():
    query = urllib.quote('"so say we all"')
    limit = '50'
    request = requests.get('http://api.pushshift.io/reddit/search?limit='+limit+'&q='+query)
    json = request.json()
    comments = json["data"]
    return comments
