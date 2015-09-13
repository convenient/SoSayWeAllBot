import bot
import praw

__author__ = 'lukerodgers90@gmail.com'
__version__ = '1.0'

def main():
    json_comments = bot.get_comments()
    reddit_api = bot.get_reddit_api()

    filtered_comments = bot.filter_comments(reddit_api, json_comments)

    #for comment in filtered_comments:
        #print str(comment.author.name)

main()
