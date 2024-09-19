from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from faker import Faker
from models import Animal, Enclosure

engine = create_engine("sqlite:///lib/zoo.db")
Session = sessionmaker(bind=engine)
session = Session()

# init Faker
fake = Faker()

# Enclosure instances
enclosures = [
    Enclosure(name="Desert", capacity=20),
    Enclosure(name="Savannah", capacity=30),
    Enclosure(name="Forest", capacity=50),
    Enclosure(name="Aqua", capacity=25),
]

