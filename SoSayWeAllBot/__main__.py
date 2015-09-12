import comment_finder
import reddit

__author__ = 'lukerodgers90@gmail.com'
__version__ = '1.0'

r = ReferenceError

def main():
    wrapper = reddit.ApiWrapper()

    json_comments = comment_finder.get_comments()

    comments = wrapper.filter_comments(json_comments)

    for comment in comments:
        print str(comment.author.name)

main()
