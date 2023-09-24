from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
api = Api(app)


engine = create_engine('your_database_uri_here')
Session = sessionmaker(bind=engine)


parser = reqparse.RequestParser()
parser.add_argument('price', type=int, required=True, help='Price is required')
parser.add_argument('pizza_id', type=int, required=True, help='Pizza ID is required')
parser.add_argument('restaurant_id', type=int, required=True, help='Restaurant ID is required')


class RestaurantsResource(Resource):
    def get(self):
        session = Session()
        restaurants = session.query(Restaurant).all()
        session.close()
        
        formatted_restaurants = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
        
        return jsonify(formatted_restaurants)


class RestaurantResource(Resource):
    def get(self, restaurant_id):
        session = Session()
        restaurant = session.query(Restaurant).get(restaurant_id)
        
        if restaurant:
            pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas]
            
            formatted_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas
            }
            
            session.close()
            return jsonify(formatted_data)
        else:
            session.close()
            return {"error": "Restaurant not found"}, 404

    def delete(self, restaurant_id):
        session = Session()
        restaurant = session.query(Restaurant).get(restaurant_id)
        
        if restaurant:
            session.query(RestaurantPizza).filter_by(restaurant_id=restaurant.id).delete()
            session.delete(restaurant)
            session.commit()
            session.close()
            
            return '', 204
        else:
            session.close()
            return {"error": "Restaurant not found"}, 404


class PizzasResource(Resource):
    def get(self):
        session = Session()
        pizzas = session.query(Pizza).all()
        session.close()
        
        formatted_pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
        
        return jsonify(formatted_pizzas)


class RestaurantPizzasResource(Resource):
    def post(self):
        args = parser.parse_args()
        price = args['price']
        pizza_id = args['pizza_id']
        restaurant_id = args['restaurant_id']
        
        session = Session()
        
        pizza = session.query(Pizza).get(pizza_id)
        restaurant = session.query(Restaurant).get(restaurant_id)
        
        if not (pizza and restaurant):
            session.close()
            return {"errors": ["Pizza or Restaurant not found"]}, 404
        
        try:
            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
            session.add(restaurant_pizza)
            session.commit()
            
            formatted_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            
            session.close()
            return jsonify(formatted_data)
        except Exception as e:
            session.rollback()
            session.close()
            return {"errors": ["validation errors"]}, 400

# Add resources to the API with routes
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantResource, '/restaurants/<int:restaurant_id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run()
