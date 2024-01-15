**API Documentation**

**Base URL**: http://localhost:8000

**Authentication**:

* All endpoints are accessible without authentication, except for the `/signup` endpoint.
* The `/signup` endpoint requires a `staffId` in the request body.

**Endpoints**:

**1. Sign Up (POST /signup)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `name`: The name of the staff member.
    * `role`: The role of the staff member (e.g., "waiter", "manager", "cook").
    * `shift`: The shift of the staff member (e.g., "morning", "afternoon", "night").
    * `specialty`: The specialty of the staff member (e.g., "Italian cuisine", "French cuisine", "Chinese cuisine").

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
    * `staffID`: The ID of the newly created staff member

**2. Get Staff List (GET /staff_list)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * A list of staff members, each with the following information:
        * `staffId`: The ID of the staff member.
        * `name`: The name of the staff member.
        * `role`: The role of the staff member.
        * `shift`: The shift of the staff member.
        * `specialty`: The specialty of the staff member.

**3. Edit Staff (POST /edit_staff)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `staffID`: The ID of the staff member to be edited.
    * `newName`: The new name of the staff member.
    * `newRole`: The new role of the staff member.
    * `newShift`: The new shift of the staff member.
    * `newSpecialty`: The new specialty of the staff member.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**4. Remove Staff (POST /remove_staff)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `staffID`: The ID of the staff member to be removed.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**5. Login (POST /login)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `staffID`: The ID of the staff member attempting to log in.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
    * `name`: The name of the staff member who logged in.
    * `role`: The role of the staff member who logged in.
    * `shift`: The shift of the staff member who logged in.

**6. Display Tables (GET /display_tables)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * A list of tables, each with the following information:
        * `tableNo`: The number of the table.
        * `tableStatus`: The status of the table (e.g., "available", "occupied", "reserved").
        * `guestName`: The name of the guest who is currently occupying the table (if any).

**7. Make Table (POST /make_table)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `tableNo`: The number of the table to be made.
    * `guestName`: The name of the guest who will be occupying the table.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
    * `tableStatus`: The new status of the table.
    * `guestName`: The name of the guest who is now occupying the table.

**8. Remove Table (POST /remove_table)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `tableNo`: The number of the table to be removed.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
    * `tableNo`: The number of the table that was removed.

**9. Display Menu (GET /display_menu)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * A list of menu items, each with the following information:
        * `itemID`: The ID of the menu item.
        * `name`: The name of the menu item.
        * `price`: The price of the menu item.
        * `inStock`: The availability status of the menu item (e.g., "in stock", "out of stock").

**10. Add Item to Order (POST /add_item_to_order)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * An array of objects, each representing an item to be added to an order. Each object should have the following properties:
        * `orderId`: The ID of the order to which the item is being added.
        * `itemId`: The ID of the menu item being added.
        * `quantity`: The quantity of the menu item being added.
        * `staffId`: The ID of the staff member who is adding the item to the order.
        * `tableNo`: The number of the table where the order is being placed.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**11. Remove Order (POST /remove_order)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `orderId`: The ID of the order to be removed.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**12. Display Record (GET /display_record)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * A list of orders, each with the following information:
        * `orderId`: The ID of the order.
        * `staffId`: The ID of the staff member who took the order.
        * `shift`: The shift of the staff member who took the order.
        * `totalAmount`: The total amount of the order.
        * `date`: The date and time when the order was placed.

**13. Display Order Status (GET /display_order_status)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * A list of orders, each with the following information:
        * `orderID`: The ID of the order.
        * `orderStatus`: The status of the order (e.g., "new", "in progress", "completed").

**14. Set Order Status (POST /set_order_status)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `orderID`: The ID of the order whose status is being updated.
    * `newStatus`: The new status of the order.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**15. Make Payment (POST /payment)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `orderID`: The ID of the order for which payment is being made.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
    * `paymentID`: The ID of the payment.
    * `totalamount`: The total amount of the payment.

**16. Display Ingredients (GET /display_ingredients)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * A list of ingredients, each with the following information:
        * `ingredientID`: The ID of the ingredient.
        * `name`: The name of the ingredient.
        * `threshold`: The threshold quantity of the ingredient.
        * `amount`: The current quantity of the ingredient.
        * `itemID`: The ID of the menu item that the ingredient belongs to.

**17. Edit Ingredient (POST /edit_ingredient)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `ingredientID`: The ID of the ingredient to be edited.
    * `newName`: The new name of the ingredient.
    * `newAmount`: The new quantity of the ingredient.
    * `newThreshold`: The new threshold quantity of the ingredient.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**18. Add Ingredient (POST /add_ingredient)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `ingredientName`: The name of the ingredient to be added.
    * `amount`: The quantity of the ingredient to be added.
    * `threshold`: The threshold quantity of the ingredient.
    * `itemID`: The ID of the menu item that the ingredient belongs to.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
    * `ingredientID`: The ID of the newly created ingredient.

**19. Remove Ingredient (POST /remove_ingredient)**

**Request**:

* **Content-Type**: `application/json`
* **Body**:
    * `ingredientID`: The ID of the ingredient to be removed.

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"

**20. Reset Ingredient Amounts (POST /reset_ingredient_amounts)**

**Request**:

* **Content-Type**: `application/json`

**Response**:

* **Status Code**: 200 (OK)
* **Content-Type**: `application/json`
* **Body**:
    * `status`: "success" or "failure"
