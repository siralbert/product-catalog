from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma

class Fruit(db.Model):
    __tablename__ = "fruit"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    weight = db.Column(db.Integer)
    description = db.Column(db.String())
    image_name = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class FruitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Fruit
        load_instance = True
        sqla_session = db.session
        include_relationships = True


fruit_schema = FruitSchema()
fruits_schema = FruitSchema(many=True)
