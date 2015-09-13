import MySQLdb

class Connection:
    def __init__(self, user, password, host, database):
        self.connection = MySQLdb.connect(
            host=host, user=user, passwd=password, db=database
        )

    def get_connection(self):
        return self.connection

    def get_comment_id(self, comment_id):
        return False

    def save_comment_id(self, comment_id):
        return False