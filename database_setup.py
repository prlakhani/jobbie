from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Define classes(tables) here




# Do the setup

engine = create_engine(os.environ.get(
    DATABASE_URL, "postgres://jobbieadmin:jobbieadmin@localhost/jobbie_test"))

Base.metadata.create_all(engine)
