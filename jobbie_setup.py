from sqlalchemy import Integer, String, Text, Float, Date
from sqlalchemy import Table, Column, CheckConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import os
import datetime


Base = declarative_base()

# Define classes(tables) here


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(80),nullable=False)
    # logo col has imgur id of image
    logo = Column(Integer, default = 555555)
    locations = Column(ARRAY(Float))
    # checkconstraint that each location is len 2
    # this should be a 2d array, lat/long are cols and ea loc is a row
    __table_args__ = (CheckConstraint('array_length(locations,1)=2'),)


class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    createdDate = Column(Date, default=datetime.date.today(), nullable=False)
    location = Column(ARRAY(Float)) # Postgres doesn't enforce size constraint
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship(Company)
    description = Column(Text, nullable=False)
    # Checkconstraint on location that it is len 2 in dim 1
    __table_args__ = (CheckConstraint('array_length(location,1)=2'),)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


job_to_user_table = Table('applications', Base.metadata,
    Column('job_id', Integer, ForeignKey('job.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)


User.jobs = relationship('Job', secondary = job_to_user_table,
        backref='applicants')
# this needs to be done after the job_to_user_table is defined
Company.creator_id = Column(Integer, ForeignKey('user.id'))
Company.creator = relationship(User)
# this needs to be done only after the User class is created
# only the creator of a company object will be able to post jobs by that co.

# Do the setup

engine = create_engine(os.environ.get(
    'DATABASE_URL', "postgres://jobbieadmin:jobbieadmin@localhost/jobbie_test"))

Base.metadata.create_all(engine)
