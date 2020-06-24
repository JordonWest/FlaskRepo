from peewee import *
import os
db = SqliteDatabase("mydatabase.sqlite3")


class BaseModel(Model):
    class Meta:
        database = db


class Food(BaseModel):
    name = CharField(null=False)


db.connect()
db.create_tables([Food], safe=True)
