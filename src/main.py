from fastapi import FastAPI

from model import Contact
 
app = FastAPI()
 
@app.get("/")

def read_root():

    return {"message": "Welcome to FastAPI!"}
 
@app.get("/contacts")

def get_contacts():

    contacts = Contact.select()

    return {"contacts": [contact.__data__ for contact in contacts]}
 
@app.post("/contacts")

def add_contact(name: str, email: str, phone: str):

    contact = Contact(name=name, email=email, phone=phone)

    contact.save()

    return {"message": "Contact added successfully."}
 
@app.put("/contacts/{id}")

def update_contact(id: int, name: str, email: str, phone: str):

    contact = Contact.get(Contact.id == id)

    contact.name = name

    contact.email = email

    contact.phone = phone

    contact.save()

    return {"message": "Contact updated successfully."}
 
@app.delete("/contacts/{id}")

def delete_contact(id: int):

    contact = Contact.get(Contact.id == id)

    contact.delete_instance()

    return {"message": "Contact deleted successfully."}
