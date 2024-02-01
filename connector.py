import os

import mysql.connector as mysql

class Connector():
    _instance = None

    def __new__(cls):
        if cls._instance is None :
            cls._instance = super(Connector, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.Host = os.environ.get('MYSQL_HOST') or 'localhost'
        self.User = os.environ.get('MYSQL_USER') or 'root'
        self.Password = os.environ.get('MYSQL_PASSWORD') or ''
        self.DB = os.environ.get('MYSQL_DB') or 'hagdb'

        self.Connection = mysql.connect(
            host = self.Host,
            user = self.User,
            password = self.Password,
            database = self.DB
        )

    def __del__(self):
        self.Connection.close()