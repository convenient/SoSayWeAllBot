import praw
import os
import ConfigParser
import requests
import urllib

user_name = 'SoSayWeAllBot'

def get_comments():
    query = urllib.quote('"so say we all"')
    limit = '10'
    request = requests.get('http://api.pushshift.io/reddit/search?limit='+limit+'&q='+query)
    json = request.json()
    comments = json["data"]
    return comments

def get_config():
    config = ConfigParser.ConfigParser()
    config.read(os.path.dirname(__file__) + '/config.cnf')
    return config

def get_reddit_api():
    password = get_config().get('Reddit', 'password')

    r = praw.Reddit(user_name + '/1.0 (https://github.com/convenient/SoSayWeAllBot')
    r.login(user_name, password, disable_warning=True)

    if not r.is_logged_in():
        print "Oh god!"
        exit(-1)

    return r

def filter_comments(reddit_api, comments):

    filtered_comments = set()
    counter = 0

    for rawcomment in comments:
        counter += 1
        print str(counter) + "/" + str(len(comments))

        rawcomment['_replies'] = ''
        comment = praw.objects.Comment(reddit_api, rawcomment)

        # Do not want to get stuck in a "So Say We All" loop
        author = str(comment.author.name)
        if author == user_name:
            continue

        filtered_comments.add(comment)

    return filtered_comments
