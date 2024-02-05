## Restaurant Management System API Documentation

### Introduction

This API provides a RESTful interface for managing a restaurant. It allows users to perform various operations, such as managing staff, tables, menus, orders, and ingredients.

### Prerequisites

* Python 3.6 or higher
* Flask
* Flask-SQLAlchemy
* Flask-RESTful
* Flask-Cors
* PostgreSQL

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/restaurant-management-system.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Import PostgreSQL database and user:

Server password: admin

4. Update the `app.config` in `app.py` with your database connection details:

    ```
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/Restaurant'
    ```

### Usage

1. Start the development server:

    ```
    python app.py
    ```

2. Open your browser and navigate to `http://yourIP/swagger/`. This will open the Swagger UI, where you can explore the API endpoints and their documentation.

3. In Front-end side:

Navigate to App.jsx and modify this line: Axios.defaults.baseURL = "your backend IP";

4. Run ```npm install``` first to install all the dependency. Then run ```npm run web``` to run the web app.

5. Voilà! Enjoy tweaking the Restaurant System web app with ease.

### API Endpoints

#### 1. Staff Management

* **POST /signup**

    **Description:** Create a new staff member.

    **Request Body:**

    ```
    {
        "name": "John Doe",
        "role": "Waiter",
        "shift": 1,
        "specialty": "Italian Cuisine"
    }
    ```

    **Response:**

    ```
    {
        "status": "success",
        "staffID": 1
    }
    ```

* **GET /staff_list**

    **Description:** Get a list of all staff members.

    **Response:**

    ```
    [
        {
            "staffId": 1,
            "name": "John Doe",
            "role": "Waiter",
            "shift": 1,
            "specialty": "Italian Cuisine"
        },
        ...
    ]
    ```

* **POST /edit_staff**

    **Description:** Edit an existing staff member.

    **Request Body:**

    ```
    {
        "staffID": 1,
        "newName": "Jane Doe",
        "newRole": "Manager",
        "newShift": 2,
        "newSpecialty": "French Cuisine"
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

* **POST /remove_staff**

    **Description:** Remove an existing staff member.

    **Request Body:**

    ```
    {
        "staffID": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

#### 2. Login

* **POST /login**

    **Description:** Login a staff member.

    **Request Body:**

    ```
    {
        "staffID": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success",
        "name": "John Doe",
        "role": "Waiter",
        "shift": 1
    }
    ```

#### 3. Table Management

* **GET /display_tables**

    **Description:** Get a list of all tables and their status.

    **Response:**

    ```
    [
        {
            "tableNo": 1,
            "tableStatus": 1,
            "guestName": "John Smith"
        },
        ...
    ]
    ```

* **POST /make_table**

    **Description:** Create a new table.

    **Request Body:**

    ```
    {
        "tableNo": 1,
        "guestName": "John Smith"
    }
    ```

    **Response:**

    ```
    {
        "status": "success",
        "tableStatus": 1,
        "guestName": "John Smith"
    }
    ```

* **POST /remove_table**

    **Description:** Remove an existing table.

    **Request Body:**

    ```
    {
        "tableNo": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

#### 4. Menu Management

* **GET /display_menu**

    **Description:** Get a list of all menu items.

    **Response:**

    ```
    [
        {
            "itemID": 1,
            "name": "Pizza",
            "price": 10,
            "inStock": 1
        },
        ...
    ]
    ```

#### 5. Order Management

* **POST /add_item_to_order**

    **Description:** Add an item to an existing order.

    **Request Body:**

    ```
    [
        {
            "orderId": 1,
            "itemId": 1,
            "quantity": 2,
            "staffId": 1,
            "tableNo": 1
        }
    ]
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

* **POST /remove_order**

    **Description:** Remove an existing order.

    **Request Body:**

    ```
    {
        "orderId": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

#### 6. Record Management

* **GET /display_record**

    **Description:** Get a list of all orders and their details.

    **Response:**

    ```
    [
        {
            "orderId": 1,
            "staffId": 1,
            "shift": 1,
            "totalAmount": 20,
            "date": "2023-01-29T23:10:33"
        },
        ...
    ]
    ```

#### 7. Order Status Management

* **GET /display_order_status**

    **Description:** Get a list of all orders and their status.

    **Response:**

    ```
    [
        {
            "orderID": 1,
            "orderStatus": 1
        },
        ...
    ]
    ```

* **POST /set_order_status**

    **Description:** Set the status of an existing order.

    **Request Body:**

    ```
    {
        "orderID": 1,
        "newStatus": 2
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

#### 8. Order Details Management

* **POST /get_order_details**

    **Description:** Get the details of an existing order.

    **Request Body:**

    ```
    {
        "orderID": 1
    }
    ```

    **Response:**

    ```
    [
        {
            "itemName": "Pizza",
            "quantity": 2,
            "totalamount": 20
        }
    ]
    ```

#### 9. Payment Management

* **POST /payment**

    **Description:** Make a payment for an existing order.

    **Request Body:**

    ```
    {
        "orderID": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success",
        "paymentID": 1,
        "totalamount": 20
    }
    ```

#### 10. Ingredient Management

* **GET /display_ingredients**

    **Description:** Get a list of all ingredients.

    **Response:**

    ```
    [
        {
            "ingredientID": 1,
            "name": "Flour",
            "threshold": 10,
            "amount": 20,
            "itemID": 1
        },
        ...
    ]
    ```

* **POST /add_ingredient**

    **Description:** Add a new ingredient.

    **Request Body:**

    ```
    {
        "ingredientName": "Sugar",
        "amount": 50,
        "threshold": 20,
        "itemID": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success",
        "ingredientID": 6
    }
    ```

* **POST /edit_ingredient**

    **Description:** Edit an existing ingredient.

    **Request Body:**

    ```
    {
        "ingredientID": 1,
        "newName": "Salt",
        "newAmount": 30,
        "newThreshold": 15
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

* **POST /remove_ingredient**

    **Description:** Remove an existing ingredient.

    **Request Body:**

    ```
    {
        "ingredientID": 1
    }
    ```

    **Response:**

    ```
    {
        "status": "success"
    }
    ```

* **POST /reset_ingredient_amounts**

    **Description:** Reset the amounts of all ingredients to 20.

    **Response:**

    ```
    {
        "status": "success"
    }
    ```
