from datetime import datetime
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Initialize API
api = Api(app)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chocoisme:choco123@localhost/chocoisme'
db = SQLAlchemy(app)


# Define models
class Staff(db.Model):
    __tablename__ = 'staff'
    staffid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    shift = db.Column(db.String)
    specialty = db.Column(db.String)


class Menu(db.Model):
    __tablename__ = 'menu'
    itemid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    instock = db.Column(db.Integer)
    staffid = db.Column(db.Integer, db.ForeignKey('staff.staffid'))


class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    ingredientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    amount = db.Column(db.Integer)
    measurement = db.Column(db.String)
    itemid = db.Column(db.Integer, db.ForeignKey('menu.itemid'))


class DiningTable(db.Model):
    __tablename__ = 'diningtable'
    tableno = db.Column(db.Integer, primary_key=True)
    tablestatus = db.Column(db.Integer)


class Guest(db.Model):
    __tablename__ = 'guest'
    guestid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    tableno = db.Column(db.Integer, db.ForeignKey('diningtable.tableno'))


class Orders(db.Model):
    __tablename__ = 'orders'
    orderid = db.Column(db.Integer, primary_key=True)
    guestid = db.Column(db.Integer, db.ForeignKey('guest.guestid'))
    orderstatus = db.Column(db.Integer)
    date = db.Column(db.String)


class OrderDetails(db.Model):
    __tablename__ = 'orderdetails'
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'), primary_key=True)
    itemid = db.Column(db.Integer, db.ForeignKey('menu.itemid'), primary_key=True)
    quantity = db.Column(db.Integer)
    totalamount = db.Column(db.Float)
    staffid = db.Column(db.Integer, db.ForeignKey('staff.staffid'))


class Payment(db.Model):
    __tablename__ = 'payment'
    paymentid = db.Column(db.Integer, primary_key=True)
    totalamount = db.Column(db.Float)
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'))


# Define API resources
class Login(Resource):
    def post(self):
        data = request.get_json()
        staff_id = data['staffID']
        staff = Staff.query.filter_by(staffid=staff_id).first()
        if staff:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failure'})


class DisplayTables(Resource):
    def get(self):
        tables = DiningTable.query.all()
        output = []
        for table in tables:
            output.append({'tableNo': table.tableno, 'tableStatus': table.tablestatus})
        return jsonify(output)


class MakeTable(Resource):
    def post(self):
        data = request.get_json()
        table_no = data['tableNo']
        guest_name = data['guestName']
        table = DiningTable.query.filter_by(tableno=table_no).first()
        if not table:
            return jsonify({'status': 'failure'})
        guest = Guest(name=guest_name, tableno=table_no)
        db.session.add(guest)
        table.tablestatus = 1
        db.session.commit()
        return jsonify({'status': 'success', 'tableStatus': table.tablestatus, 'guestId': guest.guestid})


class RemoveTable(Resource):
    def post(self):
        data = request.get_json()
        table_no = data['tableNo']
        table = DiningTable.query.filter_by(tableno=table_no).first()
        if not table:
            return jsonify({'status': 'failure'})
        if table.tablestatus == 0:
            return jsonify({'status': 'failure'})
        guest = Guest.query.filter_by(tableno=table_no).first()
        if guest:
            db.session.delete(guest)
        table.tablestatus = 0
        db.session.commit()
        return jsonify({'status': 'success', 'tableNo': table_no})


class DisplayMenu(Resource):
    def get(self):
        menu_items = Menu.query.all()
        output = []
        for item in menu_items:
            staff = Staff.query.filter_by(staffid=item.staffid).first()
            output.append({'itemID': item.itemid, 'name': item.name, 'price': item.price, 'inStock': item.instock,
                           'staffID': staff.staffid})
        return jsonify(output)


class AddItemToOrder(Resource):
    def post(self):
        data = request.get_json()
        order_id = data['orderId']
        item_id = data['itemId']
        quantity = data['quantity']
        staff_id = data['staffId']
        guest_id = data['guestId']

        item = Menu.query.filter_by(itemid=item_id).first()
        if item.instock == 2:
            return jsonify({'status': 'failure'})

        # Check if an order with the same ID already exists
        existing_order = Orders.query.filter_by(orderid=order_id).first()

        if existing_order:
            # If the order already exists, only add the item to the OrderDetails table
            order_detail = OrderDetails(orderid=order_id, itemid=item_id,
                                        quantity=quantity, totalamount=item.price * int(quantity), staffid=staff_id)
            db.session.add(order_detail)
            db.session.commit()

            return jsonify({'status': 'success', 'totalAmount': order_detail.totalamount})
        else:
            # If the order does not exist, add it to the Orders table and then add the item to the OrderDetails table
            order = Orders(orderid=order_id, guestid=guest_id, orderstatus=0,
                           date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            db.session.add(order)
            db.session.commit()

            order_detail = OrderDetails(orderid=order_id, itemid=item_id,
                                        quantity=quantity, totalamount=item.price * int(quantity), staffid=staff_id)
            db.session.add(order_detail)
            db.session.commit()

            return jsonify({'status': 'success', 'totalAmount': order_detail.totalamount})


class RemoveOrder(Resource):
    def post(self):
        data = request.get_json()
        order_id = data['orderId']
        order_details = OrderDetails.query.filter_by(orderid=order_id).all()
        payment = Payment.query.filter_by(orderid=order_id).first()
        if payment:
            db.session.delete(payment)
        for order_detail in order_details:
            db.session.delete(order_detail)
        order = Orders.query.filter_by(orderid=order_id).first()
        if order:
            db.session.delete(order)
        db.session.commit()
        return jsonify({'status': 'success'})


class DisplayRecord(Resource):
    def get(self):
        orders = Orders.query.all()
        output = []
        for order in orders:
            # Retrieve the staff ID from OrderDetails based on order ID
            order_detail = OrderDetails.query.filter_by(orderid=order.orderid).first()
            staff = Staff.query.filter_by(staffid=order_detail.staffid).first()
            payment = Payment.query.filter_by(orderid=order.orderid).first()
            output.append(
                {'orderId': order.orderid, 'staffId': staff.staffid, 'shift': staff.shift,
                 'totalAmount': payment.totalamount, 'date': order.date})
        return jsonify(output)


class DisplayOrderStatus(Resource):
    def get(self):
        orders = Orders.query.all()
        output = []
        for order in orders:
            output.append({'orderID': order.orderid, 'orderStatus': order.orderstatus})
        return jsonify(output)


class SetOrderStatus(Resource):
    def post(self):
        data = request.get_json()
        order_id = data['orderID']
        new_status = data['newStatus']
        order = Orders.query.filter_by(orderid=order_id).first()
        if not order:
            return jsonify({'status': 'failure'})
        order.orderstatus = new_status
        db.session.commit()
        return jsonify({'status': 'success'})


class MakePayment(Resource):
    def post(self):
        data = request.get_json()
        order_id = data['orderID']

        # Check if the order is served (orderstatus = 3)
        order = Orders.query.filter_by(orderid=order_id).first()
        if not order or order.orderstatus != 3:
            return jsonify({'status': 'failure', 'message': 'Order is not served yet'})

        # Calculate the total amount to be paid
        total_amount = 0
        order_details = OrderDetails.query.filter_by(orderid=order_id).all()
        for order_detail in order_details:
            total_amount += order_detail.totalamount

        # Create a new payment record
        payment = Payment(totalamount=total_amount, orderid=order_id)
        db.session.add(payment)
        db.session.commit()

        return jsonify({'status': 'success', 'paymentID': payment.paymentid, 'totalamount': total_amount})


class DisplayIngredients(Resource):
    def get(self):
        ingredients = Ingredients.query.all()
        output = []
        for ingredient in ingredients:
            output.append(
                {'ingredientID': ingredient.ingredientid, 'name': ingredient.name, 'amount': ingredient.amount,
                 'measurement': ingredient.measurement})
        return jsonify(output)


class AddIngredient(Resource):
    def post(self):
        data = request.get_json()
        name = data['name']
        amount = data['amount']
        measurement = data['measurement']
        item_id = data['itemID']

        # Check if an ingredient with the same name and item ID already exists
        existing_ingredient = Ingredients.query.filter_by(name=name, itemid=item_id).first()

        # If an existing ingredient is found, return an error
        if existing_ingredient:
            return jsonify({'status': 'failure', 'message': 'Ingredient already exists'})

        # Otherwise, create a new ingredient with the next available ID
        new_ingredient_id = db.session.query(db.func.max(Ingredients.ingredientid)).scalar() + 1
        ingredient = Ingredients(ingredientid=new_ingredient_id, name=name, amount=amount, measurement=measurement,
                                 itemid=item_id)
        db.session.add(ingredient)
        db.session.commit()

        # Update the instock variable in the Menu table
        menu_item = Menu.query.filter_by(itemid=item_id).first()
        if menu_item:
            menu_item.instock = 1
            db.session.commit()

        return jsonify({'status': 'success', 'ingredientID': ingredient.ingredientid})


class EditIngredient(Resource):
    def post(self):
        data = request.get_json()
        ingredient_id = data['ingredientID']
        new_name = data['newName']
        new_amount = data['newAmount']
        new_measurement = data['newMeasurement']
        ingredient = Ingredients.query.filter_by(ingredientid=ingredient_id).first()
        if not ingredient:
            return jsonify({'status': 'failure'})
        ingredient.name = new_name
        ingredient.amount = new_amount
        ingredient.measurement = new_measurement
        db.session.commit()

        # Update the instock variable in the Menu table
        menu_item = Menu.query.filter_by(itemid=ingredient.itemid).first()
        if menu_item:
            if ingredient.amount == 0:
                menu_item.instock = 2
            else:
                menu_item.instock = 1
            db.session.commit()

        return jsonify({'status': 'success'})


class RemoveIngredient(Resource):
    def post(self):
        data = request.get_json()
        ingredient_id = data['ingredientID']
        ingredient = Ingredients.query.filter_by(ingredientid=ingredient_id).first()
        if not ingredient:
            return jsonify({'status': 'failure'})
        db.session.delete(ingredient)
        db.session.commit()

        # Update the instock variable in the Menu table
        menu_item = Menu.query.filter_by(itemid=ingredient.itemid).first()
        if menu_item:
            menu_item.instock = 2
            db.session.commit()

        return jsonify({'status': 'success'})


# Add resources to API
api.add_resource(Login, '/login')  # All
api.add_resource(DisplayTables, '/display_tables')  # Waiter, Manager
api.add_resource(MakeTable, '/make_table')  # Waiter, Manager
api.add_resource(RemoveTable, '/remove_table')  # Waiter, Manager
api.add_resource(DisplayMenu, '/display_menu')  # Waiter, Manager
api.add_resource(AddItemToOrder, '/add_item_to_order')  # Waiter, Manager
api.add_resource(RemoveOrder, '/remove_order')  # Waiter, Manager
api.add_resource(DisplayRecord, '/display_record')  # Manager
api.add_resource(DisplayOrderStatus, '/display_order_status')  # All
api.add_resource(SetOrderStatus, '/set_order_status')  # All
api.add_resource(MakePayment, '/payment')  # Waiter, Manager
api.add_resource(DisplayIngredients, '/display_ingredients')  # Cook
api.add_resource(EditIngredient, '/edit_ingredient')  # Cook
api.add_resource(AddIngredient, '/add_ingredient')  # Cook
api.add_resource(RemoveIngredient, '/remove_ingredient')  # Cook

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
