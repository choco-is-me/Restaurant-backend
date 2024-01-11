**API Documentation**

**Base URL:** http://localhost:8000

**Authentication:**

* All endpoints that require authentication will require a valid JWT token in the `Authorization` header.
* To obtain a JWT token, you can use the `/login` endpoint.

**Staff Management:**

* **`/signup`**:
    * **Method:** POST
    * **Request Body:**
        * `name`: The name of the staff member.
        * `role`: The role of the staff member (e.g., "Waiter", "Manager", "Cook").
        * `shift`: The shift of the staff member (e.g., "Morning", "Afternoon", "Evening").
        * `specialty`: The specialty of the staff member (e.g., "Cooking", "Serving", "Cleaning").
    * **Response:**
        * `status`: "success" or "failure"
        * `staffID`: The ID of the newly created staff member.
* **`/staff_list`**:
    * **Method:** GET
    * **Response:**
        * A list of all staff members in the system.
* **`/edit_staff`**:
    * **Method:** POST
    * **Request Body:**
        * `staffID`: The ID of the staff member to be edited.
        * `newName`: The new name of the staff member.
        * `newRole`: The new role of the staff member.
        * `newShift`: The new shift of the staff member.
        * `newSpecialty`: The new specialty of the staff member.
    * **Response:**
        * `status`: "success" or "failure"
* **`/remove_staff`**:
    * **Method:** POST
    * **Request Body:**
        * `staffID`: The ID of the staff member to be removed.
    * **Response:**
        * `status`: "success" or "failure"

**Login:**

* **`/login`**:
    * **Method:** POST
    * **Request Body:**
        * `staffID`: The ID of the staff member.
    * **Response:**
        * `status`: "success" or "failure"
        * `name`: The name of the staff member.
        * `role`: The role of the staff member.
        * `shift`: The shift of the staff member.
        * `JWT Token`: A valid JWT token that can be used to authenticate subsequent requests.

**Table Management:**

* **`/display_tables`**:
    * **Method:** GET
    * **Response:**
        * A list of all tables in the system, along with their current status and the name of the guest sitting at the table (if any).
* **`/make_table`**:
    * **Method:** POST
    * **Request Body:**
        * `tableNo`: The number of the table to be created.
        * `guestName`: The name of the guest who will be sitting at the table.
    * **Response:**
        * `status`: "success" or "failure"
        * `tableStatus`: The new status of the table.
        * `guestName`: The name of the guest who will be sitting at the table.
* **`/remove_table`**:
    * **Method:** POST
    * **Request Body:**
        * `tableNo`: The number of the table to be removed.
    * **Response:**
        * `status`: "success" or "failure"

**Menu Management:**

* **`/display_menu`**:
    * **Method:** GET
    * **Response:**
        * A list of all items on the menu, along with their prices, current stock levels, and an image link.

**Order Management:**

* **`/add_item_to_order`**:
    * **Method:** POST
    * **Request Body:**
        * An array of objects, each containing the following properties:
            * `orderId`: The ID of the order to which the item is being added.
            * `itemId`: The ID of the item being added to the order.
            * `quantity`: The quantity of the item being added to the order.
            * `staffId`: The ID of the staff member who is adding the item to the order.
            * `tableNo`: The number of the table at which the order is being placed.
    * **Response:**
        * `status`: "success" or "failure"
* **`/remove_order`**:
    * **Method:** POST
    * **Request Body:**
        * `orderId`: The ID of the order to be removed.
    * **Response:**
        * `status`: "success" or "failure"

**Order History:**

* **`/display_record`**:
    * **Method:** GET
    * **Response:**
        * A list of all orders that have been placed, along with the total amount of each order, the date the order was placed, and the ID of the staff member who took the order.

**Order Status:**

* **`/display_order_status`**:
    * **Method:** GET
    * **Response:**
        * A list of all orders that have been placed, along with their current status.
* **`/set_order_status`**:
    * **Method:** POST
    * **Request Body:**
        * `orderID`: The ID of the order whose status is being changed.
        * `newStatus`: The new status of the order.
    * **Response:**
        * `status`: "success" or "failure"

**Payment:**

* **`/payment`**:
    * **Method:** POST
    * **Request Body:**
        * `orderID`: The ID of the order for which payment is being made.
    * **Response:**
        * `status`: "success" or "failure"
        * `paymentID`: The ID of the payment.
        * `totalamount`: The total amount of the payment.

**Ingredient Management:**

* **`/display_ingredients`**:
    * **Method:** GET
    * **Response:**
        * A list of all ingredients in the system, along with their current amounts, threshold levels, and the item they belong to.
* **`/add_ingredient`**:
    * **Method:** POST
    * **Request Body:**
        * `ingredientName`: The name of the ingredient to be added.
        * `amount`: The amount of the ingredient to be added.
        * `threshold`: The threshold level for the ingredient.
        * `itemID`: The ID of the item that the ingredient belongs to.
    * **Response:**
        * `status`: "success" or "failure"
        * `ingredientID`: The ID of the newly created ingredient.
* **`/edit_ingredient`**:
    * **Method:** POST
    * **Request Body:**
        * `ingredientID`: The ID of the ingredient to be edited.
        * `newName`: The new name of the ingredient.
        * `newAmount`: The new amount of the ingredient.
        * `newThreshold`: The new threshold level for the ingredient.
    * **Response:**
        * `status`: "success" or "failure"
* **`/remove_ingredient`**:
    * **Method:** POST
    * **Request Body:**
        * `ingredientID`: The ID of the ingredient to be removed.
    * **Response:**
        * `status`: "success" or "failure"

**Reset Ingredient Amounts:**

* **`/reset_ingredient_amounts`**:
    * **Method:** POST
    * **Response:**
        * `status`: "success" or "failure"
