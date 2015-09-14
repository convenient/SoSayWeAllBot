import praw
import os
import requests
import urllib
import json
import random
import time

class SoSayWeAllBot:

    user_name = 'SoSayWeAllBot'

    def __init__(self, password, connection):
        self.time_started = time.time()

        self.connection = connection

        with open(os.path.dirname(__file__) + '/images.json') as data_file:
            data = json.load(data_file)

        self.images = data["images"]

        self.praw = praw.Reddit(self.user_name + '/1.0 (https://github.com/convenient/SoSayWeAllBot')
        self.praw.login(self.user_name, password, disable_warning=True)
        if not self.praw.is_logged_in():
            print "Oh god!"
            exit(-1)

    def run_loop(self):
        # Allow a few second to boot up the app, initialise connection to database etc
        runtime = 55

        while self.time_started + runtime > time.time():
            self.run()

    def run(self):
        comments = self.get_comments()
        counter = 0

        for comment in comments:
            counter += 1

            code = str(comment.id)

            if self.connection.code_exists(code):
                continue
            self.connection.save_code(code)

            print str(counter) + "/" + str(len(comments))

            image_url = self.get_random_image_url()
            message = '[So Say We All](' + image_url + ')[!](https://github.com/convenient/SoSayWeAllBot)'
            comment.reply(message)

    def search_for_comments(self):
        query = urllib.quote('"so say we all"')
        limit = '100'
        request = requests.get('http://api.pushshift.io/reddit/search?limit='+limit+'&q='+query)
        json = request.json()
        comments = json["data"]
        return comments

    def get_random_image_url(self):
        return str(random.choice(self.images))

    def get_reddit_api(self):
        return self.praw

    def get_comments(self):

        reddit_api = self.get_reddit_api()
        comments = self.search_for_comments()

        filtered_comments = set()

        # Only look at comments created in the last day
        recent_comment_time = int(self.time_started - 86400)

        for rawcomment in comments:
            rawcomment['_replies'] = ''
            comment = praw.objects.Comment(reddit_api, rawcomment)

            # Do not want to get stuck in a "So Say We All" loop
            author = str(comment.author.name)
            if author == self.user_name:
                continue

            timestamp_created_at = int(comment.created_utc)
            if (timestamp_created_at < recent_comment_time):
                continue

            filtered_comments.add(comment)

        return filtered_comments
