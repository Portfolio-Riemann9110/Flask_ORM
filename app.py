from flask import Flask, request
import requests

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import config as config

app.config.from_object(config.DevelopmentConfig())
db = SQLAlchemy(app)
app.app_context().push()

# table 생성 및 반영
db.create_all()


if __name__ == '__main__':
    app.run()



# https://lowelllll.github.io/til/2019/04/19/TIL-flask-sqlalchemy-orm/
# https://github.com/johyju03/-apartment_deal_history