**API Documentation**

**1. User Authentication**
- [POST] `/login`
  - **Request Body:**
    - `staffID` (integer)
  - **Response:**
    - `status` (string): "success" or "failure"
    - `name` (string): Name of the staff member (if login is successful)
    - `role` (string): Role of the staff member (if login is successful)
    - `shift` (integer): Shift of the staff member (if login is successful)

**2. Staff Management**
- [POST] `/signup`
  - **Request Body:**
    - `name` (string)
    - `role` (string)
    - `shift` (integer)
    - `specialty` (string)
  - **Response:**
    - `status` (string): "success" or "failure"
    - `staffID` (integer): ID of the newly created staff member (if sign up is successful)
- [GET] `/staff_list`
  - **Response:**
    - A list of all staff members in the system, including their ID, name, role, shift, and specialty
- [POST] `/edit_staff`
  - **Request Body:**
    - `staffID` (integer)
    - `newName` (string)
    - `newRole` (string)
    - `newShift` (integer)
    - `newSpecialty` (string)
  - **Response:**
    - `status` (string): "success" or "failure"
- [POST] `/remove_staff`
  - **Request Body:**
    - `staffID` (integer)
  - **Response:**
    - `status` (string): "success" or "failure"

**3. Table Management**
- [GET] `/display_tables`
  - **Response:**
    - A list of all tables in the restaurant, including their number, status (occupied or available), and the name of the guest sitting at the table (if occupied)
- [POST] `/make_table`
  - **Request Body:**
    - `tableNo` (integer)
    - `guestName` (string)
  - **Response:**
    - `status` (string): "success" or "failure"
    - `tableStatus` (integer): Status of the table after the operation (occupied or available)
    - `guestName` (string): Name of the guest sitting at the table (if the operation is successful)
- [POST] `/remove_table`
  - **Request Body:**
    - `tableNo` (integer)
  - **Response:**
    - `status` (string): "success" or "failure"

**4. Menu Management**
- [GET] `/display_menu`
  - **Response:**
    - A list of all menu items, including their ID, name, price, stock availability, and image link

**5. Order Management**
- [POST] `/add_item_to_order`
  - **Request Body:**
    - A list of items to be added to the order, each item represented as:
      - `orderId` (integer): ID of the order to which the item is being added
      - `itemId` (integer): ID of the menu item being ordered
      - `quantity` (integer): Quantity of the item being ordered
      - `staffId` (integer): ID of the staff member taking the order
      - `tableNo` (integer): Number of the table at which the order is being placed
  - **Response:**
    - `status` (string): "success" or "failure"
- [POST] `/remove_order`
  - **Request Body:**
    - `orderId` (integer): ID of the order to be removed
  - **Response:**
    - `status` (string): "success" or "failure"

**6. Order History and Payment**
- [GET] `/display_record`
  - **Response:**
    - A list of all orders, including their ID, staff ID, shift, total amount, and date
- [GET] `/display_order_status`
  - **Response:**
    - A list of all orders, including their ID and status (served, cooking, or pending)
- [POST] `/set_order_status`
  - **Request Body:**
    - `orderID` (integer): ID of the order to update
    - `newStatus` (integer): New status of the order (0: pending, 1: cooking, 2: served)
  - **Response:**
    - `status` (string): "success" or "failure"
- [POST] `/payment`
  - **Request Body:**
    - `orderID` (integer): ID of the order for which payment is being made
  - **Response:**
    - `status` (string): "success" or "failure"
    - `paymentID` (integer): ID of the payment transaction
    - `totalamount` (integer): Total amount paid for the order

**7. Ingredient Management**
- [GET] `/display_ingredients`
  - **Response:**
    - A list of all ingredients, including their ID, name, threshold amount, and current amount in stock
- [POST] `/add_ingredient`
  - **Request Body:**
    - `ingredientName` (string)
    - `amount` (integer)
    - `threshold` (integer)
    - `itemID` (integer): ID of the menu item to which the ingredient belongs
  - **Response:**
    - `status` (string): "success" or "failure"
    - `ingredientID` (integer): ID of the newly created ingredient (if addition is successful)
- [POST] `/edit_ingredient`
  - **Request Body:**
    - `ingredientID` (integer)
    - `newName` (string)
    - `newAmount` (integer)
    - `newThreshold` (integer)
  - **Response:**
    - `status` (string): "success" or "failure"
- [POST] `/remove_ingredient`
  - **Request Body:**
    - `ingredientID` (integer)
  - **Response:**
    - `status` (string): "success" or "failure"
- [POST] `/reset_ingredient_amounts`
  - **Response:**
    - `status` (string): "success" or "failure"
