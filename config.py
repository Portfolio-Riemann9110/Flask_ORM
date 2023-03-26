class Config:
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    def __init__(self):
        import json
        with open('config.json', 'r') as f:
            config = json.load(f)

        Config.SQLALCHEMY_DATABASE_URI = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
        Config.SQLALCHEMY_ECHO = config['DEFAULT']['SQLALCHEMY_ECHO']
        Config.SQLALCHEMY_TRACK_MODIFICATIONS = config['DEFAULT']['SQLALCHEMY_TRACK_MODIFICATIONS']