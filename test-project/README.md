# Mongo-Migrator Test Project

This folder contains the initial structure to test the [mongo-migrator](https://github.com/Alburrito/mongo-migrator) package.

The following dependencies are required to run the project:
- Docker
- Docker Compose
- Python 3.9 or higher
- Pipenv

**NOTE**: The instructions in this document will use Pipenv, but you can use any package manager you want.

In the following sections, you will find the instructions to set up the test environment and test all the features of the package.

## Setup of the test environment
1. Activate the environment and install dependencies:
```bash
cd test-project
# Optional, but recommended
# This will create a virtual environment in the project folder, not in the user's home directory
export PIPENV_VENV_IN_PROJECT=1
pipenv shell
pipenv install -r requirements.txt
```

2. Use the `docker-compose.yml` file to start a MongoDB instance:
```bash
docker-compose up -d
```

3. Run the setup script
```bash
python3 setup-test-db.py
```
The script will create a database called `test-db` and a collection called `test-collection` with some sample data.

4. Now the environment is ready to be tested, simulating a real project with a MongoDB database you can connect to.

5. You can also run the following commands to test the mongo-migrator package:
```bash
mongo-migrator --help
mongo-migrator --version
```

## Mongo-Migrator initial setup
1. Create the `mongo-migrator.config` file. You can use this example as a template:

```ini
[database]
host =
port =
name =
user = # Optional
password = # Optional

[migrations]
directory =
collection =
```

2. Fill the required fields with the information of the MongoDB instance and the migrations directory. You can find more information about the fields in the [mongo-migrator documentation](https://github.com/Alburrito/mongo-migrator).

3. Initialize the mongo-migrator with the following command:
```bash
mongo-migrator init
```

This will create:
- The migrations directory, with the name specified in the `mongo-migrator.config` file. This directory will contain the migration files.
- The mongo-migrator collection with the name specified in the `mongo-migrator.config` file. This collection will store the current version of the database (the version of the last migration applied). So far, the current version will be None, since no migrations have been applied yet.

## Creating new migrations

To create a new migration, you can use the following command with the title of the migration:
```bash
mongo-migrator create "Add test collection 1"
```

This will create a new migration file in the migrations directory with the following structure:
```python
"""
title: Add test collection 1
version: <timestamp>
last_version: None
"""
from pymongo.database import Database

def upgrade(db: Database):
    # Implement this method in the generated migration file
    pass

def downgrade(db: Database):
    # Implement this method in the generated migration file
    pass
```

You can implement the `upgrade` and `downgrade` methods to apply and rollback the changes in the database. The `upgrade` method will be executed when the migration is applied, and the `downgrade` method will be executed when the migration is rolled back.

For example, you can create a migration to add a new collection to the database:
```python
"""
title: Add test collection 1
version: <timestamp>
last_version: None
"""
from pymongo.database import Database

def upgrade(db: Database):
    db.create_collection("test_collection_1")

def downgrade(db: Database):
    db.drop_collection("test_collection_1")
```

## Applying and rolling back migrations

### Upgrade

To apply the migrations, you can use the following command:
```bash
mongo-migrator upgrade
```

If no arguments are provided, the command will apply all the pending migrations. If you want to apply a specific migration, you can provide the version of the migration as an argument:
```bash
mongo-migrator upgrade --version <version>
```

You can find the version by copying the first part of the migration file name or the `version` field in the migration file.

### Downgrade

To roll back the migrations, you can use the following command:
```bash
mongo-migrator downgrade
```

If no arguments are provided, the command will roll back the last migration applied. If you want to roll back a specific migration, you can provide the version of the migration as an argument:
```bash
mongo-migrator downgrade --version <version>
```

If you want to roll back all the migrations, you can use the following command:
```bash
mongo-migrator downgrade --all
```

## Checking the status of the migrations

To check the status of the migrations, you can use the following command:
```bash
mongo-migrator history
```

This will show a tree like this:
```
├── (APPLIED) 20250226182202521069 - Already applied migration
├── (CURRENT) 20250226182204092841 - Current migration (last applied)
└── (PENDING) 20250226182205577166 - Pending migration (not applied yet)
```

If the migration history is not a linear tree, the command will warn you about the inconsistencies in the migrations.
