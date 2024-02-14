from datetime import datetime
from sqlalchemy.exc import OperationalError

from config import app, db
from models import Fruit

FRUITS = [
  {
    "name": "Apple",
    "weight": 500,
    "description": "Apple is one of the most nutritious and healthiest fruits. It is very rich in antioxidants and dietary fiber. Moderate consumption can not only increase satiety, but also help promote bowel movements. Apple also contains minerals such as calcium and magnesium, which can help prevent and delay bone loss and maintain bone health. It is good for young and old.\u00a0",
    "image_name": "001.jpeg"
  },
  {
    "name": "Avocado",
    "weight": 200,
    "description": "Avocado contains large amount of oleic acid, a type of monounsaturated fat that can replace saturated fat in the diet, which is very effective in reducing cholesterol levels. Avocado is also high in fiber. Its soluble fiber can remove excess cholesterol from the body, while its insoluble fiber helps keep the digestive system functioning and prevent constipation.",
    "image_name": "002.jpeg"
  }
]


def get_data_from_table(model):
    try:
        data = db.session.query(model).all()
        db.session.close()
        return data
    except OperationalError:
        return []


def create_database(db):
    db.create_all()

    for data in FRUITS:
        new_fruit = Fruit(name=data.get("name"), weight=data.get("weight"),description=data.get("description"),image_name=data.get("image_name"))
        db.session.add(new_fruit)

    db.session.commit()
    print("Created new database")


def update_database(db, existing_fruits):
    db.drop_all()
    db.create_all()
    for fruit in existing_fruits:
        db.session.merge(fruit)
    db.session.commit()
    print("Updated existing database")


with app.app_context():
    existing_fruits = get_data_from_table(Fruit)

    if not existing_fruits:
        create_database(db)
    else:
        update_database(db, existing_fruits)
