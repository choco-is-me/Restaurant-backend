**Base URL:** http://localhost:8000

**Authentication:**

* All endpoints require authentication except for `/login` and `/display_menu`.
* To authenticate, send a POST request to `/login` with the staff ID in the request body.
* The response will contain a JSON object with a `token` field.
* Include the `token` in the `Authorization` header of all subsequent requests.

**Endpoints:**

* **`/signup`**
    * **Method:** POST
    * **Access:** Admin
    * **Request Body:**
        * `name`: The name of the staff member.
        * `role`: The role of the staff member (e.g., "waiter", "manager", "cook").
        * `shift`: The shift of the staff member (e.g., "morning", "afternoon", "evening").
        * `specialty` (optional): The specialty of the staff member (e.g., "Italian", "French", "Chinese").
    * **Response:**
        * `status`: "success" or "failure"
        * `staffID`: The ID of the newly created staff member (if successful).
* **`/staff_list`**
    * **Method:** GET
    * **Access:** Admin
    * **Response:**
        * A list of all staff members in the system, including their ID, name, role, shift, and specialty.
* **`/remove_staff`**
    * **Method:** POST
    * **Access:** Admin
    * **Request Body:**
        * `staffID`: The ID of the staff member to be removed.
    * **Response:**
        * `status`: "success" or "failure"
* **`/login`**
    * **Method:** POST
    * **Access:** All
    * **Request Body:**
        * `staffID`: The ID of the staff member.
    * **Response:**
        * `status`: "success" or "failure"
        * `name`: The name of the staff member (if successful).
        * `role`: The role of the staff member (if successful).
        * `shift`: The shift of the staff member (if successful).
        * `token`: The authentication token (if successful).
* **`/display_tables`**
    * **Method:** GET
    * **Access:** Waiter, Manager
    * **Response:**
        * A list of all dining tables in the system, including their number, status (0 for empty, 1 for occupied, 2 for reserved), and the name of the guest (if occupied).
* **`/make_table`**
    * **Method:** POST
    * **Access:** Waiter, Manager
    * **Request Body:**
        * `tableNo`: The number of the table to be reserved.
        * `guestName`: The name of the guest.
    * **Response:**
        * `status`: "success" or "failure"
        * `tableStatus`: The new status of the table (1 for occupied).
        * `guestName`: The name of the guest.
* **`/remove_table`**
    * **Method:** POST
    * **Access:** Waiter, Manager
    * **Request Body:**
        * `tableNo`: The number of the table to be removed.
    * **Response:**
        * `status`: "success" or "failure"
        * `tableNo`: The number of the table that was removed.
* **`/display_menu`**
    * **Method:** GET
    * **Access:** All
    * **Response:**
        * A list of all menu items in the system, including their ID, name, price, stock status (0 for out of stock, 1 for in stock, 2 for low stock), and image link.
* **`/add_item_to_order`**
    * **Method:** POST
    * **Access:** Waiter, Manager
    * **Request Body:**
        * A JSON array of order items, each with the following fields:
            * `orderId`: The ID of the order.
            * `itemId`: The ID of the menu item.
            * `quantity`: The quantity of the menu item to be ordered.
            * `staffId`: The ID of the staff member who is taking the order.
            * `tableNo`: The number of the table where the order is being placed.
    * **Response:**
        * `status`: "success" or "failure"
* **`/remove_order`**
    * **Method:** POST
    * **Access:** Waiter, Manager
    * **Request Body:**
        * `orderId`: The ID of the order to be removed.
    * **Response:**
        * `status`: "success" or "failure"
* **`/display_record`**
    * **Method:** GET
    * **Access:** Manager
    * **Response:**
        * A list of all orders in the system, including their ID, the ID of the staff member who took the order, the shift of the staff member, the total amount of the order, and the date the order was placed.
* **`/display_order_status`**
    * **Method:** GET
    * **Access:** All
    * **Response:**
        * A list of all orders in the system, including their ID and status (0 for not served, 1 for served, 2 for paid, 3 for completed).
* **`/set_order_status`**
    * **Method:** POST
    * **Access:** All
    * **Request Body:**
        * `orderID`: The ID of the order.
        * `newStatus`: The new status of the order (0 for not served, 1 for served, 2 for paid, 3 for completed).
    * **Response:**
        * `status`: "success" or "failure"
* **`/payment`**
    * **Method:** POST
    * **Access:** Waiter, Manager
    * **Request Body:**
        * `orderID`: The ID of the order.
    * **Response:**
        * `status`: "success" or "failure"
        * `paymentID`: The ID of the payment (if successful).
        * `totalamount`: The total amount of the payment (if successful).
* **`/display_ingredients`**
    * **Method:** GET
    * **Access:** Cook
    * **Response:**
        * A list of all ingredients in the system, including their ID, name, threshold, and amount.
* **`/edit_ingredient`**
    * **Method:** POST
    * **Access:** Cook
    * **Request Body:**
        * `ingredientID`: The ID of the ingredient to be edited.
        * `newName`: The new name of the ingredient.
        * `newAmount`: The new amount of the ingredient.
        * `newThreshold`: The new threshold of the ingredient.
    * **Response:**
        * `status`: "success" or "failure"
* **`/add_ingredient`**
    * **Method:** POST
    * **Access:** Cook
    * **Request Body:**
        * `ingredientName`: The name of the ingredient.
        * `amount`: The amount of the ingredient.
        * `threshold`: The threshold of the ingredient.
        * `itemID`: The ID of the menu item that the ingredient belongs to.
    * **Response:**
        * `status`: "success" or "failure"
        * `ingredientID`: The ID of the newly created ingredient (if successful).
* **`/remove_ingredient`**
    * **Method:** POST
    * **Access:** Cook
    * **Request Body:**
        * `ingredientID`: The ID of the ingredient to be removed.
    * **Response:**
        * `status`: "success" or "failure"
* **`/reset_ingredient_amounts`**
    * **Method:** POST
    * **Access:** Cook
    * **Response:**
        * `status`: "success"
