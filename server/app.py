from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)
db.init_app(app)


api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('price', type=int, required=True, help='Price is required')
parser.add_argument('pizza_id', type=int, required=True, help='Pizza ID is required')
parser.add_argument('restaurant_id', type=int, required=True, help='Restaurant ID is required')


from flask import make_response
from flask_restful import Resource

class Home(Resource):
    def get(self):
        response_dict = {
            "message": "Welcome to Miriam's Pizza Restaurant",
        }

        return make_response(response_dict, 200)


class RestaurantsResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        
        formatted_restaurants = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
        
        return jsonify(formatted_restaurants)


class RestaurantByIdResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)

        if restaurant:
            pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas]

            formatted_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas
            }

            return jsonify(formatted_data)
        else:
            return {"error": "Restaurant not found"}, 404



    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            
            return '', 204
        else:
            return {"error": "Restaurant not found"}, 404


class PizzasResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        
        formatted_pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
        
        return jsonify(formatted_pizzas)
    


class RestaurantPizzasResource(Resource):
    def post(self):
        args = parser.parse_args()
        price = args['price']
        pizza_id = args['pizza_id']
        restaurant_id = args['restaurant_id']
        
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        
        if not (pizza and restaurant):
            return {"errors": ["Pizza or Restaurant not found"]}, 404
        
        try:
            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
            db.session.add(restaurant_pizza)
            db.session.commit()
            
            formatted_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            
            return jsonify(formatted_data)
        except Exception as e:
            db.session.rollback()
            return {"errors": ["validation errors"]}, 400

# Add resources to the API with routes
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantByIdResource, '/restaurants/<int:restaurant_id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run()
