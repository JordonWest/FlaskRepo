# Jordon's CR Flask Example

This app can Read and create data, only. Not loading you up with a full CRUD (create, read, update, delete) app yet.

## How to run it..

1. Start a virtual environment.
   - `python3 -m venv claysvenv`
2. Activate the virtual environment.
   - `claysvenv/Scripts/activate`
3. Pip install dependencies.
   - `pip install -r requirements.txt`
4. Start Flask!
   - `flask run`

## Things to note

- Full stack Flask, meaning it serves it's own templates
- Uses a venv to make dependencies easily acquirable
- using a Sqlite3 database (great for development because you can just blow it away if you mess it up)

## Breakdown of app

- app.py is the root of our application, and defines the routes, as well as where they send us and what they can serve.
- templates/ holds our html files. ezpz
- mydatabase.sqlite3 is just our sqlite3 database file. Its encoded, and you can't really read it without knowing PSQL commands, so ignore it for now. Just know that it creating and holding onto what is created in models.py
- models.py creates the tables of our database. That's it.
- seed.py is seeding our database with 2 entries. That's all.
- requirements.txt is holding our requirements to be pip installed into the venv
- I'm using Peewee to interpret what's in the database and make it useable with common python logic.
