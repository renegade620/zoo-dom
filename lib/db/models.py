# imports
from sqlalchemy import Date, create_engine
from sqlalchemy import ForeignKey, Column, Integer, String, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# joint tables
staff_animal = Table (
    'staff_animal',
    Base.metadata,
    Column('staff_id', Integer, ForeignKey('staff.id')),
    Column('animal_id', Integer, ForeignKey('animals.id'))
)

visitor_animal = Table (
    'visitor_animal',
    Base.metadata,
    Column('visitor_id', Integer, ForeignKey('visitors.id')),
    Column('animal_id', Integer, ForeignKey('animals.id'))
)

# vet_animal = Table (
#     'vet_animal',
#     Base.metadata,
#     Column('vet_id', Integer, ForeignKey('vets.id')),
#     Column('animal_id', Integer, ForeignKey('animals.id'))
# )

# main tables
class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    species = Column(String())
    age = Column(Integer())
    enclosure_id = Column(Integer(), ForeignKey("enclosures.id")) # Foreign Key

    # Relationships
    enclosure = relationship("Enclosure", backref=backref("animals"))
    staff = relationship("Staff", secondary=staff_animal, backref="animals")
    visitors = relationship("Visitor", secondary=visitor_animal, backref="animals")
    # vets = relationship("Vet", secondary=vet_animal, backref="animals")

class Enclosure(Base):
    __tablename__ = "enclosures"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    capacity = Column(Integer())
    

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    role = Column(String())
    species_specialization = Column(String(), nullable=True) # for vets


class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    visit_date = Column(Date)

# redundant
# class Vet (Base):
#    __tablename__ = "vets"
#    id = Column(Integer(), primary_key=True)
#    name = Column(String())
   


engine = create_engine("sqlite:///zoo.db")
Base.metadata.create_all(engine)