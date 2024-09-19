# imports
from sqlalchemy import Date, create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# tables
class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    species = Column(String())
    age = Column(Integer())
    enclosure_id = Column(Integer(), ForeignKey("enclosures.id")) # Foreign Key
    enclosure = relationship("Enclosure", backref="animals") # One to Many Relationship

class Enclosure(Base):
    __tablename__ = "enclosures"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    capacity = Column(Integer())
    

class Staff(Base):
    __tablename__ = "staffs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    role = Column(String())

class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    visit_date = Column(Date)

class Vete(Base):
   __tablename__ = "vets"
   id = Column(Integer(), primary_key=True)
   name = Column(String())
   species_specialization = Column(String())


engine = create_engine("sqlite:///zoo.db")
Base.metadata.create_all(engine)