# imports
from sqlalchemy import Date, create_engine
from sqlalchemy import ForeignKey, Column, Integer, String, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///zoo.db")
Session = sessionmaker(bind=engine)

# joint tables
staff_animal = Table(
    "staff_animal",
    Base.metadata,
    Column("staff_id", Integer, ForeignKey("staff.id")),
    Column("animal_id", Integer, ForeignKey("animals.id")),
)

visitor_animal = Table(
    "visitor_animal",
    Base.metadata,
    Column("visitor_id", Integer, ForeignKey("visitors.id")),
    Column("animal_id", Integer, ForeignKey("animals.id")),
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
    enclosure_id = Column(Integer(), ForeignKey("enclosures.id"))  # Foreign Key

    # Relationships
    enclosure = relationship("Enclosure", backref=backref("animals"))
    staff = relationship("Staff", secondary=staff_animal, backref="animals")
    visitors = relationship("Visitor", secondary=visitor_animal, backref="animals")
    # vets = relationship("Vet", secondary=vet_animal, backref="animals")

    def __repr__(self):
        return f"Animal(id={self.id}, name='{self.name}', species='{self.species}', age={self.age}, enclosure='{self.enclosure.name if self.enclosure else 'None'}')"

    @property
    def adult_or_child(self):
        return "Child" if self.age < 2 else "Adult"

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def delete(cls, session, id):
        animal = cls.find_by_id(session, id)
        if animal:
            session.delete(animal)
            session.commit()
            return "Animal Deleted Successfully"
        return "Animal does not exist!"

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()


class Enclosure(Base):
    __tablename__ = "enclosures"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    capacity = Column(Integer())

    def __repr__(self):
        return f"Enclosure(id={self.id}, name='{self.name}', capacity={self.capacity})"

    @property
    def space_available(self):
        return self.capacity - len(self.animals)

    @classmethod
    def create(cls, session, name, capacity):
        enclosure = cls(name=name, capacity=capacity)
        session.add(enclosure)
        session.commit()
        return enclosure

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def delete(cls, session, id):
        enclosure = cls.find_by_id(session, id)
        if enclosure:
            session.delete(enclosure)
            session.commit()
            return "Enclosure Deleted Successfully"
        return "Enclosure does not exist!"

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    role = Column(String())
    species_specialization = Column(String(), nullable=True)  # for vets

    @classmethod
    def create(cls, session, name, role):
        staff = cls(name=name, role=role)
        session.add(staff)
        session.commit()
        return staff

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def delete(cls, session, id):
        staff = cls.find_by_id(session, id)
        if staff:
            session.delete(staff)
            session.commit()
            return "Staff Deleted Successfully"
        return "Staff does not exist!"

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by_id(id=id).first()


class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    visit_date = Column(Date)

    @classmethod
    def create(cls, session, name, visit_date):
        visitor = cls(name=name, visit_date=visit_date)
        session.add(visitor)
        session.commit()
        return visitor

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def delete(cls, session, id):
        visitor = cls.find_by_id(session, id)
        if visitor:
            session.delete(visitor)
            session.commit()
            return "Visitor Deleted Successfully"
        return "Visitor does not exist!"

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by_id(id=id).first()


# redundant
# class Vet (Base):
#    __tablename__ = "vets"
#    id = Column(Integer(), primary_key=True)
#    name = Column(String())


Base.metadata.create_all(engine)
