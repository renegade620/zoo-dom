import click
from db.models import Session, Animal, Enclosure, Staff, Visitor
from datetime import datetime

session = Session()

@click.group()
def cli():
    """ZooDom"""
    pass

def display_menu(options):
    for i, option in enumerate(options, 1):
        click.echo(f"{i}. {option}")
    choice = click.prompt("Enter your choice", type=int)
    return choice

def crud_funcs(model_class, name):
    while True:
        choice = display_menu([f"Create {name}", f"List all {name}s", f"Find {name} by ID", f"Delete {name}", "View rlated objects", "Back to Main Menu"])

        if choice == 1:
            if model_class == Animal:
                create_animal()
            elif model_class == Enclosure:
                create_enclosure()
            elif model_class == Staff:
                create_staff()
            elif model_class == Visitor:
                create_visitor()
        elif choice == 2:
            instances = model_class.get_all(session)
            for inst in instances:
                click.echo(str(inst))
        elif choice == 3:
            id = click.prompt("Enter ID", type=int)
            inst = model_class.find_by_id(session, id)
            if inst:
                click.echo(str(inst))
            else:
                click.echo(f"{name} not found")
        elif choice == 4:
            id = click.prompt("Enter ID to delete", type=int)
            if model_class.delete(session, id):
                click.echo(f"{name} deleted successfully!")
            else:
                click.echo(f"{name} not found!")
        elif choice == 5:
            id = click.prompt("Enter ID", type=int)
            inst = model_class.find_by_id(session, id)
            if inst:
                if hasattr(inst, "animals"):
                    click.echo("Related animals:")
                    for animal in inst.animals:
                        click.echo(str(animal))
                elif hasattr(inst, "enclosures"):
                    click.echo(f"Enclosure: {inst.enclosures}")
                elif hasattr(inst, "staff"):
                    click.echo("Reated Staff")
                    for staff in inst.staff:
                        click.echo(str(staff))
                else:
                    click.echo("No related objects found")
            else:
                click.echo(f"{name} not found")
        elif choice == 6:
            break # exit

# create methods
def create_animal():
    name = click.prompt("Enter animal name")
    species = click.prompt("Enter species")
    age = click.prompt("Enter age", type=int)
    enclosure_id = click.prompt("Enter Enclosure ID", type=int)
    enclosure = Enclosure.find_by_id(session, enclosure_id)
    if enclosure:
        animal = Animal.create(session, name, species, age, enclosure)
        click.echo(f"Animal {animal} has been created!")
    else:
        click.echo("Enclosure not found")

def create_enclosure():
    name = click.prompt("Enter enclosure name")
    capacity = click.prompt("Enter capacity", type=int)
    enclosure = Enclosure.create(session, name, capacity)
    click.echo(f"Created enclosure: {enclosure}")

def create_staff():
    name = click.prompt("Enter staff name")
    role = click.prompt("Enter role")
    staff = Staff.create(session, name, role)
    click.echo(f"Staff {staff} has been created!")

def create_visitor():
    name = click.prompt("Enter visitor name", type=str)
    visit_date = click.prompt("Enter visit date (YYYY-MM-DD)", type=str)
    try:
        visit_date = datetime.strptime(visit_date, "%Y-%m-%d").date()
        visitor = Visitor.create(session, name, visit_date)
        click.echo(f"Visitor {visitor} has been created!")
    except ValueError:
        click.echo("Invalid date format")

@cli.command()
def run():
    """Run ZooDom"""
    while True:
        choice = display_menu(["Manage Animals", "Manage Enclosures", "Manage Staff", "Manage Visitors", "Exit"])

        if choice == 1:
            crud_funcs(Animal, "animal")
        elif choice == 2:
            crud_funcs(Enclosure, "enclosure")
        elif choice == 3:
            crud_funcs(Staff, "staff")
        elif choice == 4:
            crud_funcs(Visitor, "visitor")
        elif choice == 5:
            click.echo("Goodbye!")
            break

if __name__ == "__main__":
    cli()