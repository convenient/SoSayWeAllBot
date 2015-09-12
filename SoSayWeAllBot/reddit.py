import praw
import os

class ApiWrapper:

    name = 'SoSayWeAllBot'

    def __init__(self):
        self.api = False

    def get_praw(self):
        if not self.api:

            with open(os.path.dirname(__file__) + '/config.cnf', 'r') as file:
                password = file.read().replace('\n', '')

            r = praw.Reddit(self.name + '/1.0 (https://github.com/convenient/SoSayWeAllBot')
            r.login(self.name, password, disable_warning=True)

            if not r.is_logged_in():
                print "Oh god!"
                exit(-1)

            self.api = r

        return self.api

    def filter_comments(self, comments):

        r = self.get_praw()
        filtered_comments = set()
        counter = 0

        for rawcomment in comments:
            counter += 1
            print str(counter) + "/" + str(len(comments))

            rawcomment['_replies'] = ''
            comment = praw.objects.Comment(r, rawcomment)

            # Do not want to get stuck in a "So Say We All" loop
            author = str(comment.author.name)
            if author == self.name:
                continue

            # If we've already replied to this comment, don't do it again!
            already_replied = False
            replies_list = r.get_submission(comment.permalink).comments[0].replies
            for reply in replies_list:
                author = str(reply.author.name)
                if author == self.name:
                    already_replied = True
                    break

            if already_replied:
                continue

            filtered_comments.add(comment)

        return filtered_comments
