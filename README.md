# ZooDom

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [CRUD Operations](#crud-operations)
- [Contributing](#contributing)
- [License](#license)

## Introduction

ZooDom is a command-line application designed to help manage animals, enclosures, staff, and visitors in a zoo. The application provides an easy-to-use interface for performing CRUD (Create, Read, Update, Delete) operations on various entities within the zoo, streamlining the management process.

## Features

- **Manage Animals**: Create, list, find by ID, and delete animals.
- **Manage Enclosures**: Manage enclosures for animals.
- **Manage Staff**: Keep track of staff details and responsibilities.
- **Manage Visitors**: Monitor visitor information and activities.
- **Data Persistence**: All data is stored in a SQLite database for easy retrieval and management.

## Technologies Used

- **Python**: Programming language used to build the application.
- **SQLAlchemy**: ORM (Object Relational Mapper) for database interactions.
- **Alembic**: Lightweight database migration tool used with SQLAlchemy.
- **SQLite**: Lightweight database for data storage.
- **Click**: Command-line interface toolkit for building command-line applications.

## Installation

To set up the ZooDom locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/zoo-management-system.git
   cd zoo-dom
   ```
2. **Install the required packages**:
   ```bash
   pipenv install
   ```
3. **Enter virtual environment(optional, but recommended**:
   ```bash
   pipenv shell
   ```

## Usage

To run ZooDom, execute the following command in your terminal:

```bash
pipenv run python cli.py run
```

Follow the prompts in the command line to manage animals, enclosures, staff, and visitors.

## CRUD Operations

Here are the available CRUD operations for managing animals:

### Create Animal

- Enter animal name, species, age, and enclosure ID.

### Read Animals

- List all animals.
- Find an animal by ID.

### Delete Animal

- Remove an animal from the database.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please open an issue or submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

Powered by franklinegift@gmail.com
