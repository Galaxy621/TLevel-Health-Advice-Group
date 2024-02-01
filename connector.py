import config

def Connector():
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(connector, cls).__new__(cls)
    
    def __init__(self):
        ...