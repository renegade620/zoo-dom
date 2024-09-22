from sqlalchemy.orm import sessionmaker
from faker import Faker
from db.models import Animal, Enclosure, Staff, Visitor, engine

import random

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
session.add_all(enclosures)
session.commit()

# Animal instances
species = ["Lion", "Leopard", "Cheetah", "Elephant", "Giraffe", "Buffalo", "Snake", "Lizard", "Tortoise", "Fox", "Jackal", "Coyote"]

for _ in range(60):
    animal = Animal(
        name=fake.first_name(),
        species=random.choice(species),
        age=random.randint(1, 25),
        enclosure=random.choice(enclosures)
    )
    session.add(animal)

# Staff
roles = ["Vet", "Guide", "Receptionist", "Manager", "Supervisor", "Feeder"]
species_specializations = ["Big Animals", "Small Animals", "Reptiles", "Aquatic Animals"]

for _ in range(20):
    role = random.choice(roles)
    species_specialization = random.choice(species_specializations) if role == "Vet" else None

    staff = Staff(
        name=fake.name(),
        role=role,
        species_specialization=species_specialization
    )
    session.add(staff)

# Visitors
for _ in range(100):
    visitor = Visitor(
        name=fake.name(),
        visit_date=fake.date_this_month()
    )
    session.add(visitor)

session.commit()

import ipdb; ipdb.set_trace()