from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Create restaurants
    restaurant1 = Restaurant(name="Cjs", address="123 Main St")
    restaurant2 = Restaurant(name="Kilimanjaro", address="400 Ronald St")
    restaurant3 = Restaurant(name="Kwetu dishes", address="300 Hellen St")
    restaurant4 = Restaurant(name="Paradise", address="100 Tee St")
    restaurant5 = Restaurant(name="Loffy", address="430 Elm St")
    restaurant6 = Restaurant(name="Milly fish grill", address="09 All St")
    restaurant7 = Restaurant(name="Hellen meat hub", address="456 Cape St")
    restaurant8 = Restaurant(name="Meat and dinner", address="456 Town St")
    
    # Create pizza
    pizza1 = Pizza(name="Margherita Pizza", ingredients="Tomato sauce, mozzarella cheese, fresh basil leaves, olive oil, salt")
    pizza2 = Pizza(name="Pepperoni Pizza", ingredients="Pepperoni, Cheese, mozzarella cheese, pepperoni slices")
    pizza3 = Pizza(name="Hawaiian Pizza", ingredients="Tomato sauce, mozzarella cheese, ham or Canadian bacon, pineapple")
    pizza4 = Pizza(name="Supreme Pizza", ingredients="Tomato sauce, mozzarella cheese, pepperoni, sausage, bell peppers")
    pizza5 = Pizza(name="BBQ Chicken Pizza", ingredients="Barbecue sauce (instead of tomato sauce), mozzarella cheese, grilled chicken")

    # Add objects to the session and commit
    db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5, restaurant6, restaurant7, restaurant8])
    db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
    db.session.commit()

    # Create restaurant pizzas
    restaurant_pizza1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=22)
    restaurant_pizza2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=30)
    restaurant_pizza3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza2, price=25)

    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()
