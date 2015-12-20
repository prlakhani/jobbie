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


