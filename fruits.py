from flask import abort, make_response

from config import db
from models import Fruit, fruits_schema, fruit_schema


def read_all():
    fruits= Fruit.query.all()
    return fruits_schema.dump(fruits)


def create(fruit):
    new_fruit = fruit_schema.load(fruit, session=db.session)
    db.session.add(new_fruit)
    db.session.commit()
    return fruit_schema.dump(new_fruit), 201


def read_one(fruit_id):
    fruit = Fruit.query.get(fruit_id)

    if fruit is not None:
        return fruit_schema.dump(fruit)
    else:
        abort(404, f"Fruit with ID {fruit_id} not found")


def update(fruit_id, fruit):
    existing_fruit = Fruit.query.get(fruit_id)

    if existing_fruit:
        update_fruit = fruit_schema.load(fruit, session=db.session)
        existing_fruit.fname = update_fruit.fname
        existing_fruit.lname = update_fruit.lname
        db.session.merge(existing_fruit)
        db.session.commit()
        return fruit_schema.dump(existing_fruit), 201
    else:
        abort(404, f"Fruit with ID {fruit_id} not found")


def delete(fruit_id):
    existing_fruit = Fruit.query.get(fruit_id)

    if existing_fruit:
        db.session.delete(existing_fruit)
        db.session.commit()
        return make_response(f"{fruit_id} successfully deleted", 200)
    else:
        abort(404, f"Fruit with ID {fruit_id} not found")
