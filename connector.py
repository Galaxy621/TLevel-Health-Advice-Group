import os

def Connector():
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Connector, cls).__new__(cls)
    
    def __init__(self):
        self.Host = os.environ.get('MYSQL_HOST') or 'localhost'
        self.User = os.environ.get('MYSQL_USER') or 'root'
        self.Password = os.environ.get('MYSQL_PASSWORD') or 'password'
        self.DB = os.environ.get('MYSQL_DB') or 'db'