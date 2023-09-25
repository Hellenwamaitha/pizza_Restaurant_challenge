from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

Base = declarative_base()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
   
    @validates('name')
    def validate_name_length(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than or equal to 50 characters")
        return name
    
    __table_args__ = (
        UniqueConstraint('name', name='uq_restaurant_name'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    pizzas = relationship('RestaurantPizza', back_populates='restaurant')

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants = relationship('RestaurantPizza', back_populates='pizza')

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    @validates('price')
    def validate_price(self, key, price):
        price_range = range(1, 31)  # 1 to 30 (inclusive)
        if price not in price_range:
            raise ValueError("Price must be within the range of 1 to 30")
        return price
    
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    name = db.Column(db.String(255))
    ingredients = db.Column(db.String(255))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant = relationship('Restaurant', back_populates='pizzas')
    pizza = relationship('Pizza', back_populates='restaurants')

# if __name__ == '__main__':
#     app.run()
