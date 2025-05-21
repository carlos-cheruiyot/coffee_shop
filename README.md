#  Coffee Shop OOP System

A Python-based object-oriented simulation of a coffee shop's ordering system. This project models customers, coffees, and their orders, and allows querying relationships and statistics about purchases.



##  Features

- Object-oriented design using `Customer`, `Coffee`, and `Order` classes.
- Validation for all inputs (name lengths, price range, etc.)
- Relationship methods to retrieve:
  - All orders for a customer or coffee
  - All coffees ordered by a customer
  - All customers who ordered a particular coffee
- Aggregate methods to:
  - Count number of orders for a coffee
  - Calculate average price for a coffee
  - Determine the top-spending customer on a specific coffee
- Easy-to-read, maintainable code that follows Python best practices.



##  Technologies Used

- Python 
- Pipenv for dependency and environment management
- Pytest for automated unit testing


---

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd coffee_shop

## Install dependencies using Pipenv:
pipenv install
pipenv shell


## Run the test suite:
pytest