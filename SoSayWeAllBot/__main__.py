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

    robot = bot.SoSayWeAllBot(config.get_reddit_password(), connection)

    robot.run_loop()

    connection.close()

main()
