import os
import ConfigParser


class Config:

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.dirname(__file__) + '/config.cnf')

    def get_reddit_password(self):
        return self.config.get('Reddit', 'password')

    def get_database_host(self):
        return self.config.get('SQL', 'host')

    def get_database_username(self):
        return self.config.get('SQL', 'username')

    def get_database_password(self):
        return self.config.get('SQL', 'password')

    def get_database_name(self):
        return self.config.get('SQL', 'db')
