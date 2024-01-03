## Introduction

This document provides a comprehensive description of the API endpoints for the Flask application. The application is designed to manage various aspects of a restaurant, including staff login, table management, menu display, order management, payment processing, ingredient management, and reporting. The API endpoints are designed to be user-friendly and intuitive, enabling front-end developers to easily integrate them into the application's user interface.

## API Endpoints

### 1. Login

**Endpoint:** `/login`

**Method:** POST

**Request Body:**

```
{
  "staffID": "<staff_id>"
}
```

**Response:**

```
{
  "status": "success",
  "name": "<staff_name>",
  "role": "<staff_role>",
  "shift": "<staff_shift>"
}
```

**Description:**

This endpoint allows staff members to log in to the system using their staff ID. Upon successful login, the endpoint returns the staff member's name, role, and shift.

### 2. Display Tables

**Endpoint:** `/display_tables`

**Method:** GET

**Response:**

```
[
  {
    "tableNo": "<table_number>",
    "tableStatus": "<table_status>",
    "guestName": "<guest_name>"
  },
  ...
]
```

**Description:**

This endpoint retrieves the status of all tables in the restaurant. It provides information about the table number, table status (occupied or vacant), and the name of the guest currently seated at the table, if any.

### 3. Make Table

**Endpoint:** `/make_table`

**Method:** POST

**Request Body:**

```
{
  "tableNo": "<table_number>",
  "guestName": "<guest_name>"
}
```

**Response:**

```
{
  "status": "success",
  "tableStatus": "<table_status>",
  "guestName": "<guest_name>"
}
```

**Description:**

This endpoint allows staff members to create a new table reservation. It updates the table status to occupied and associates the table with the specified guest name.

### 4. Remove Table

**Endpoint:** `/remove_table`

**Method:** POST

**Request Body:**

```
{
  "tableNo": "<table_number>"
}
```

**Response:**

```
{
  "status": "success",
  "tableNo": "<table_number>"
}
```

**Description:**

This endpoint allows staff members to remove a table reservation. It updates the table status to vacant and disassociates the guest from the table.

### 5. Display Menu

**Endpoint:** `/display_menu`

**Method:** GET

**Response:**

```
[
  {
    "itemID": "<item_id>",
    "name": "<item_name>",
    "price": "<item_price>",
    "inStock": "<item_stock_status>"
  },
  ...
]
```

**Description:**

This endpoint retrieves the menu items available in the restaurant. It provides information about the item ID, item name, item price, and the stock status of the item (in stock or out of stock).

### 6. Add Item to Order

**Endpoint:** `/add_item_to_order`

**Method:** POST

**Request Body:**

```
[
  {
    "orderId": "<order_id>",
    "itemId": "<item_id>",
    "quantity": "<quantity>",
    "staffId": "<staff_id>",
    "tableNo": "<table_number>"
  },
  ...
]
```

**Response:**

```
{
  "status": "success"
}
```

**Description:**

This endpoint allows staff members to add items to an existing order. It requires the order ID, item ID, quantity, staff ID, and table number. Upon successful addition, the endpoint returns a success status.

### 7. Remove Order

**Endpoint:** `/remove_order`

**Method:** POST

**Request Body:**

```
{
  "orderId": "<order_id>"
}
```

**Response:**

```
{
  "status": "success"
}
```

**Description:**

This endpoint allows staff members to remove an existing order. It requires the order ID. Upon successful removal, the endpoint returns a success status.

### 8. Display Record

**Endpoint:** `/display_record`

**Method:** GET

**Response:**

```
[
  {
    "orderId": "<order_id>",
    "staffId": "<staff_id>",
    "shift": "<staff_shift>",
    "totalAmount": "<total_amount>",
    "date": "<order_date>"
  },
  ...
]
```

**Description:**

This endpoint retrieves a record of all orders placed in the restaurant. It provides information about the order ID, staff ID, staff shift, total amount of the order, and the date when the order was placed.

### 9. Display Order Status

**Endpoint:** `/display_order_status`

**Method:** GET

**Response:**

```
[
  {
    "orderId": "<order_id>",
    "orderStatus": "<order_status>"
  },
  ...
]
```

**Description:**

This endpoint retrieves the status of all orders placed in the restaurant. It provides information about the order ID and the current status of the order.

### 10. Set Order Status

**Endpoint:** `/set_order_status`

**Method:** POST

**Request Body:**

```
{
  "orderId": "<order_id>",
  "newStatus": "<new_status>"
}
```

**Response:**

```
{
  "status": "success"
}
```

**Description:**

This endpoint allows staff members to update the status of an existing order. It requires the order ID and the new status to be set. Upon successful update, the endpoint returns a success status.

### 11. Make Payment

**Endpoint:** `/payment`

**Method:** POST

**Request Body:**

```
{
  "orderId": "<order_id>"
}
```

**Response:**

```
{
  "status": "success",
  "paymentID": "<payment_id>",
  "totalAmount": "<total_amount>"
}
```

**Description:**

This endpoint allows staff members to process payments for orders. It requires the order ID. Upon successful payment, the endpoint returns a success status, the payment ID, and the total amount paid.

### 12. Display Ingredients

**Endpoint:** `/display_ingredients`

**Method:** GET

**Response:**

```
[
  {
    "ingredientID": "<ingredient_id>",
    "name": "<ingredient_name>",
    "threshold": "<ingredient_threshold>",
    "amount": "<ingredient_amount>"
  },
  ...
]
```

**Description:**

This endpoint retrieves a list of all ingredients used in the restaurant. It provides information about the ingredient ID, ingredient name, ingredient threshold, and the current amount of the ingredient in stock.

### 13. Add Ingredient

**Endpoint:** `/add_ingredient`

**Method:** POST

**Request Body:**

```
{
  "ingredientName": "<ingredient_name>",
  "amount": "<ingredient_amount>",
  "threshold": "<ingredient_threshold>",
  "itemID": "<item_id>"
}
```

**Response:**

```
{
  "status": "success",
  "ingredientID": "<ingredient_id>"
}
```

**Description:**

This endpoint allows cooks to add new ingredients to the inventory. It requires the ingredient name, initial quantity, threshold quantity, and the item ID associated with the ingredient. Upon successful addition, the endpoint returns a success status and the newly created ingredient ID.

### 14. Edit Ingredient

**Endpoint:** `/edit_ingredient`

**Method:** POST

**Request Body:**

```
{
  "ingredientID": "<ingredient_id>",
  "newName": "<new_ingredient_name>",
  "newAmount": "<new_ingredient_amount>",
  "newThreshold": "<new_ingredient_threshold>"
}
```

**Response:**

```
{
  "status": "success"
}
```

**Description:**

This endpoint allows cooks to edit the details of an existing ingredient. It requires the ingredient ID, the new ingredient name, the new quantity, and the new threshold quantity. Upon successful update, the endpoint returns a success status.

### 15. Remove Ingredient

**Endpoint:** `/remove_ingredient`

**Method:** POST

**Request Body:**

```
{
  "ingredientID": "<ingredient_id>"
}
```

**Response:**

```
{
  "status": "success"
}
```

**Description:**

This endpoint allows cooks to remove an existing ingredient from the inventory. It requires the ingredient ID. Upon successful removal, the endpoint returns a success status.

### 16. Reset Ingredient Amounts

**Endpoint:** `/reset_ingredient_amounts`

**Method:** POST

**Response:**

```
{
  "status": "success"
}
```

**Description:**

This endpoint allows cooks to reset the quantity of all ingredients in the inventory to 20 units. Upon successful reset, the endpoint returns a success status.

## Conclusion

This API documentation provides a comprehensive overview of the endpoints available in the Flask application. It enables front-end developers to understand the functionality of each endpoint, the required request body format, and the expected response format. By utilizing this documentation, front-end developers can seamlessly integrate these endpoints into the user interface, creating a user-friendly and efficient restaurant management system.
