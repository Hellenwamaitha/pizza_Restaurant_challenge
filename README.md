# pizza_Restaurant_challenge
# FLask application

###  Table of Contents :

- [Introduction](#introduction)
- [Technologies Used](#technologies_used)
- [Project Structure](#project_structure)
- [Models](#models)
  - [Restaurant](#restaurant)
  - [Pizza](#pizza)
  - [RestaurantPizza](#restaurantpizza)
- [Validations](#validations)
- [Routes](#routes)
  - [GET /restaurants](#get-restaurants)
  - [GET /restaurants/:id](#get-restaurantsid)
  - [DELETE /restaurants/:id](#delete-restaurantsid)
  - [GET /pizzas](#get-pizzas)
  - [POST /restaurant_pizzas](#post-restaurant_pizzas)
- [Contributions](#contributions)
- [License](#License)
- [Author info](#author)

  

## Introduction

In this *challenge*, you will build a Flask API for managing Pizza Restaurants, Pizzas, and their associations. This API will provide endpoints to perform various operations related to these entities.

## Technology Used

This challenge was mainly based on

    Python
    Flask
    RESTful API
    SQLALchemy
    
## Project Structure
 
 The project contains the following folders and files:

    myenv
    Server
    Instance file
    migration file
    app.py file
    debug.py file
    models.py file
    seed.py file
    Lincense 
    Readme.md file

## Models

You need to create the following models:

### Restaurant

- Attributes:
  - `id` (Integer, Primary Key)
  - `name` (String, Unique, Not Null, Max Length: 50)
  - `address` (String, Not Null, Max Length: 255)

- Relationships:
  - A Restaurant has many Pizzas through RestaurantPizza.

### Pizza

- Attributes:
  - `id` (Integer, Primary Key)
  - `name` (String, Not Null, Max Length: 50)
  - `ingredients` (String, Not Null, Max Length: 255)

- Relationships:
  - A Pizza has many Restaurants through RestaurantPizza.

### RestaurantPizza

- Attributes:
  - `id` (Integer, Primary Key)
  - `price` (Float, Not Null)

- Relationships:
  - A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.

## Validations

- Add the following validations to the models:

### RestaurantPizza Model

- `price` must have a value between 1 and 30.

### Restaurant Model

- `name` must have a length less than 50 characters.
- `name` must be unique.

## Routes

Set up the following routes for your API:

***GET /restaurants**

- Returns JSON data in the format:
  ```json
  [
    {
      "id": 1,
      "name": "pizza name",
      "address": "address"
    },
    {
      "id": 2,
      "name": "pizza name",
      "address": "address"
    }
  ]
  ```
  If the Restaurant does not exist, returns JSON data with the appropriate HTTP status code:

```
{
  "error": "Restaurant not found"
}
```
**DELETE /restaurants/:id**

If the Restaurant exists, it should be removed from the database, along with any RestaurantPizzas that are associated with it.

After deleting the Restaurant, returns an empty response body with the appropriate HTTP status code.

If the Restaurant does not exist, returns JSON data with the appropriate HTTP status code:
```
{
  "error": "Restaurant not found"
}
GET /pizzas
```
Returns JSON data in the format:
```
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```
**POST /restaurant_pizzas**

This route should create a new RestaurantPizza that is associated with an existing Pizza and Restaurant.

It should accept an object with the following properties in the body of the request:
```
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```
If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza:
```
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```
If the RestaurantPizza is not created successfully, return the following JSON data, along with the appropriate HTTP status code:
```
{
  "errors": ["validation
  ```
## Contributions
  Contributions  are welcome! If you'd like to contribute, please follow these steps:

    Fork the repository.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them.
    Push your changes to your fork.
    Create a pull request to the main repository.

Please ensure your code follows good coding practices and includes proper documentation.

## License

This project is licensed under the MIT License. 2023
     Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE..


## Author's Info

Hellen Wamaitha For questions or contributions email: [hellen.irungu@student.moringaschool.com]