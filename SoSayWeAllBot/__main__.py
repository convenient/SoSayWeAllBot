__author__ = 'lukerodgers90@gmail.com'
__version__ = '1.0'

import bot
import database
import configuration

def main():

    config = configuration.Config()

    connection = database.Connection(
        config.get_database_username(),
        config.get_database_password(),
        config.get_database_host(),
        config.get_database_name()
    )

    if not connection.code_exists('waffles'):
        connection.save_code('waffles')


    moo = 'cow'
    # json_comments = bot.get_comments()
    # reddit_api = bot.get_reddit_api()
    #
    # filtered_comments = bot.filter_comments(reddit_api, json_comments)

    # for comment in filtered_comments:
    #     print str(comment.author.name)

main()
