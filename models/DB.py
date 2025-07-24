import pymysql

class Db:

    def __init__(self):
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="electoral_system",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_connection(self):
        return self.__connection