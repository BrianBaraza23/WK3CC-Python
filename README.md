# WK3CC-Python - Restaurant Review System

Date Created: 3 September 2023

## Description

Welcome to the Restaurant Review System, a Python application built using SQLAlchemy for managing restaurant reviews. This system allows you to work with three main models: `Restaurant`, `Review`, and `Customer`. In this program you can check out a list of available restaurants, find out the reviews given by each customer and see the reviews a customer has given to each restaurant.


## Author

Brian Baraza

## Technologies Used

- Python
- SQLAlchemy

## Installation

To use this application, you need to have the following prerequisites:

- Python 3.7+
- SQLAlchemy
- SQLite (for local development)


Follow these steps to set up the project:

1. Clone this repository to your local machine.
2. Install the required packages using pip:

   ```
   pip install SQLAlchemy 
   ```

3. Run the database migration to create the initial tables:

   ```
   python migrate.py
   ```

4. Use the `seeds.py` file to populate the database with sample data:

   ```
   python seeds.py
   ```

## Usage

### Object Relationship Methods

#### Review Class

- `Review.customer()`: Returns the `Customer` instance associated with this review.
- `Review.restaurant()`: Returns the `Restaurant` instance associated with this review.

#### Restaurant Class

- `Restaurant.reviews()`: Returns a collection of all the reviews for this restaurant.
- `Restaurant.customers()`: Returns a collection of all the customers who reviewed this restaurant.

#### Customer Class

- `Customer.reviews()`: Returns a collection of all the reviews left by this customer.
- `Customer.restaurants()`: Returns a collection of all the restaurants reviewed by this customer.

### Aggregate and Relationship Methods

#### Customer Class

- `Customer.full_name()`: Returns the full name of the customer in Western style (first name + last name).
- `Customer.favorite_restaurant()`: Returns the restaurant instance with the highest star rating from this customer.
- `Customer.add_review(restaurant, rating)`: Adds a new review for the specified restaurant with the given rating.
- `Customer.delete_reviews(restaurant)`: Removes all reviews left by this customer for the specified restaurant.

#### Review Class

- `Review.full_review()`: Returns a formatted string with review details.

#### Restaurant Class

- `Restaurant.fanciest() (class method)`: Returns the restaurant instance with the highest price.
- `Restaurant.all_reviews()`: Returns a list of strings with all the reviews for this restaurant, formatted as follows:

   ```
   [
     "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
     "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
   ]
   ```


## License

This project is licensed under the MIT License.

## Contact Information

For any inquiries or assistance, please reach out to:

- Mobile: +254729812144
- Email: barazabrian87@gmail.com

Enjoy using the Restaurant Review System!