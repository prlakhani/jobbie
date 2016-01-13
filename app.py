from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# from database_setup import 

engine = create_engine(os.environ.get(
    DATABASE_URL, "postgres://jobbieadmin:jobbieadmin@localhost/jobbie_test"))
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

from bleach import clean

app = Flask(__name__)

if __name__ == '__main__':
    app.secret_key = os.environ.get('FLASK_SECRET_KEY',
        "\xb6\xc8\xbe\xec\xfb\xbf;\x10\xe99\xcc\xb3\x92M\x94\x0e\xc9\x18\xc4\x83\x1c\xb0\xf5x")
