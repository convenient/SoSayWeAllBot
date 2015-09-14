__author__ = 'lukerodgers90@gmail.com'
__version__ = '1.0'

import bot
import database
import configuration
import random

def main():

    config = configuration.Config()

    connection = database.Connection(
        config.get_database_username(),
        config.get_database_password(),
        config.get_database_host(),
        config.get_database_name()
    )

    json_comments = bot.get_comments()
    reddit_api = bot.get_reddit_api()

    filtered_comments = bot.filter_comments(reddit_api, json_comments)

    images = bot.get_images()

    for comment in filtered_comments:
        code = str(comment.id)

        if connection.code_exists(code):
            continue
        connection.save_code(code)

        image_url = str(random.choice(images))
        message = '[So Say We All](' + image_url + ')[!](https://github.com/convenient/SoSayWeAllBot)'

        print str(comment.author.name)

main()
