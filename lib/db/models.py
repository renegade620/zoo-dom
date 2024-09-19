# imports
from sqlalchemy import create_engine,
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# tables
class Animal(Base):
    pass

class Enclosure(Base):
    pass

class Staff(Base):
    pass

class Visitors(Base):
    pass

class Veterinary(Base):
    pass

