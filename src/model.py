from peewee import *
from database import conn
 
class Contact(Model):
    name = CharField()
    email = CharField()
    phone = CharField()
 
    class Meta:
        database = conn

conn.create_tables([Contact])