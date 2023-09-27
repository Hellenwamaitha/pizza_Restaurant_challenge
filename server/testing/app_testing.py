import unittest
import json
from app import app, db, Restaurant, Pizza, RestaurantPizza

class TestApp(unittest.TestCase):

    def setUp(self):
        
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
       
        db.session.remove()
        db.drop_all()

    def test_get_restaurants(self):
       
        response = self.app.get('/restaurants')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_single_restaurant(self):
       
        restaurant = Restaurant(name="Test Restaurant", address="Test Address")
        db.session.add(restaurant)
        db.session.commit()

       
        response = self.app.get(f'/restaurants/{restaurant.id}')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['name'], 'Test Restaurant')

    def test_get_single_restaurant_not_found(self):
        
        response = self.app.get('/restaurants/999')  
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Restaurant not found')

    def test_get_pizzas(self):
       
        response = self.app.get('/pizzas')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_create_restaurant_pizza(self):
       
        restaurant = Restaurant(name="Test Restaurant", address="Test Address")
        pizza = Pizza(name="Test Pizza", ingredients="Test Ingredients")
        db.session.add(restaurant)
        db.session.add(pizza)
        db.session.commit()

        
        response = self.app.post('/restaurant_pizzas', json={
            "price": 10.99,
            "pizza_id": pizza.id,
            "restaurant_id": restaurant.id
        })
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], pizza.id)
        self.assertEqual(data['name'], 'Test Pizza')

if __name__ == '__main__':
    unittest.main()
