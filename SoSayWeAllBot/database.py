import MySQLdb
import datetime

class Connection:
    def __init__(self, user, password, host, database):
        self.connection = MySQLdb.connect(
            host=host, user=user, passwd=password, db=database
        )

    def get_connection(self):
        return self.connection

    def close(self):
        self.connection.close()

    def code_exists(self, comment_id):
        database = self.get_connection()
        cursor = database.cursor()

        query = "SELECT code FROM replied_to WHERE code = %s LIMIT 1"
        cursor.execute(query, [comment_id])

        affected_rows = database.affected_rows()

        return bool(affected_rows)

    def save_code(self, comment_id):
        database = self.get_connection()
        cursor = database.cursor()

        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO replied_to (code, created_at) VALUES (%s, %s)"
        cursor.execute(
            query,
            [comment_id, current_time]
        )
        database.commit()
