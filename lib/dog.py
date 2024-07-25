from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine) # create the classes to the db

def save(session, dog):
    session.add(dog) # dog is created in the db
    session.commit() #apply the changes to the db

def get_all(session):
    return session.query(Dog).all() #get all objects in the dog table

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()