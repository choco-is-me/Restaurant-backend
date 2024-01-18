from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/postgres'
db = SQLAlchemy(app)
CORS(app)


# Define models
class Staff(db.Model):
    __tablename__ = 'staff'
    staffid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    shift = db.Column(db.Integer)
    specialty = db.Column(db.String)


class Menu(db.Model):
    __tablename__ = 'menu'
    itemid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    instock = db.Column(db.Integer)


class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    ingredientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    amount = db.Column(db.Integer)
    threshold = db.Column(db.Integer)
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
    date = db.Column(db.Date)


class OrderDetails(db.Model):
    __tablename__ = 'orderdetails'
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'), primary_key=True)
    itemid = db.Column(db.Integer, db.ForeignKey('menu.itemid'), primary_key=True)
    quantity = db.Column(db.Integer)
    totalamount = db.Column(db.Integer)
    staffid = db.Column(db.Integer, db.ForeignKey('staff.staffid'))


class Payment(db.Model):
    __tablename__ = 'payment'
    paymentid = db.Column(db.Integer, primary_key=True)
    totalamount = db.Column(db.Integer)
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'))


# Define API resources

class SignUp(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        name = data['name']
        role = data['role']
        shift = data['shift']
        specialty = data['specialty']

        max_staff_id = db.session.query(db.func.max(Staff.staffid)).first()[0]
        new_staff_id = max_staff_id + 1

        staff = Staff(staffid=new_staff_id, name=name, role=role, shift=shift, specialty=specialty)
        db.session.add(staff)
        db.session.commit()

        return jsonify({'status': 'success', 'staffID': new_staff_id})


class GetStaffList(Resource):
    @staticmethod
    def get():
        staffs = Staff.query.all()
        output = []
        for staff in staffs:
            output.append({'staffId': staff.staffid, 'name': staff.name, 'role': staff.role,
                           'shift': staff.shift, 'specialty': staff.specialty})
        return jsonify(output)


class EditStaff(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        staff_id = data['staffID']
        new_name = data['newName']
        new_role = data['newRole']
        new_shift = data['newShift']
        new_specialty = data['newSpecialty']

        staff = Staff.query.filter_by(staffid=staff_id).first()
        if not staff:
            return jsonify({'status': 'failure'})

        staff.name = new_name
        staff.role = new_role
        staff.shift = new_shift
        staff.specialty = new_specialty
        db.session.commit()

        return jsonify({'status': 'success'})


class RemoveStaff(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        staff_id = data['staffID']
        staff = Staff.query.filter_by(staffid=staff_id).first()
        if not staff:
            return jsonify({'status': 'failure'})
        db.session.delete(staff)
        db.session.commit()
        return jsonify({'status': 'success'})


class Login(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        staff_id = data['staffID']
        staff = Staff.query.filter_by(staffid=staff_id).first()
        if staff:
            response = jsonify({'status': 'success', 'name': staff.name, 'role': staff.role, 'shift': staff.shift})
        else:
            response = jsonify({'status': 'failure'})

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


class DisplayTables(Resource):
    @staticmethod
    def get():
        tables = DiningTable.query.all()
        output = []
        for table in tables:
            guest = Guest.query.filter_by(tableno=table.tableno).first()
            guest_name = guest.name if guest else None
            output.append({'tableNo': table.tableno, 'tableStatus': table.tablestatus, 'guestName': guest_name})
        return jsonify(output)


class MakeTable(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        table_no = data['tableNo']
        guest_name = data['guestName']
        table = DiningTable.query.filter_by(tableno=table_no).first()
        if not table:
            return jsonify({'status': 'failure'})

        if table.tablestatus == 1:
            return jsonify({'status': 'failure', 'message': 'Table is already occupied'})

        guest = Guest(name=guest_name, tableno=table_no)
        db.session.add(guest)
        table.tablestatus = 1
        db.session.commit()
        return jsonify({'status': 'success', 'tableStatus': table.tablestatus, 'guestName': guest.name})


class RemoveTable(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        table_no = data['tableNo']
        table = DiningTable.query.filter_by(tableno=table_no).first()
        if not table:
            return jsonify({'status': 'failure'})
        if table.tablestatus == 2:
            return jsonify({'status': 'failure'})
        guest = Guest.query.filter_by(tableno=table_no).first()
        if guest:
            db.session.delete(guest)
        table.tablestatus = 2
        db.session.commit()
        return jsonify({'status': 'success', 'tableNo': table_no})


class DisplayMenu(Resource):
    @staticmethod
    def get():
        menu_items = Menu.query.all()
        output = []
        for item in menu_items:
            output.append({'itemID': item.itemid, 'name': item.name, 'price': item.price,
                           'inStock': item.instock})
        return jsonify(output)


class AddItemToOrder(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        for item in data:
            order_id = item['orderId']
            item_id = item['itemId']
            quantity = item['quantity']
            staff_id = item['staffId']
            table_no = item['tableNo']

            guest = Guest.query.filter_by(tableno=table_no).first()
            if not guest:
                return jsonify({'status': 'failure', 'message': 'Guest not found for table'})
            guest_id = guest.guestid

            item = Menu.query.filter_by(itemid=item_id).first()
            ingredient_list = Ingredients.query.filter_by(itemid=item_id).all()

            if item.instock == 2:
                return jsonify({'status': 'failure', 'message': 'Item is not available'})

            insufficient_ingredient = False
            for ingredient in ingredient_list:
                if (ingredient.amount < ingredient.threshold * int(quantity)
                        and ingredient.threshold * int(quantity) > ingredient.amount):
                    insufficient_ingredient = True
                    break

            if insufficient_ingredient:
                return jsonify({'status': 'failure', 'message': 'One or more ingredients are insufficient'})

            else:
                for ingredient in ingredient_list:
                    if ingredient.amount < ingredient.threshold:
                        return jsonify({'status': 'failure', 'message': 'One or more ingredients are insufficient'})
                    else:
                        ingredient.amount -= ingredient.threshold * int(quantity)

            existing_order = Orders.query.filter_by(orderid=order_id).first()

            if existing_order:
                order_detail = OrderDetails(orderid=order_id, itemid=item_id,
                                            quantity=quantity, totalamount=item.price * int(quantity), staffid=staff_id)
                db.session.add(order_detail)
                db.session.commit()
            else:
                order = Orders(orderid=order_id, guestid=guest_id, orderstatus=0,
                               date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                db.session.add(order)
                db.session.commit()

                order_detail = OrderDetails(orderid=order_id, itemid=item_id,
                                            quantity=quantity, totalamount=item.price * int(quantity), staffid=staff_id)
                db.session.add(order_detail)
                db.session.commit()

        db.session.commit()
        return jsonify({'status': 'success'})


class RemoveOrder(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        order_id = data['orderId']
        order_details = OrderDetails.query.filter_by(orderid=order_id).all()
        payment = Payment.query.filter_by(orderid=order_id).first()
        if payment:
            db.session.delete(payment)
            db.session.commit()
        for order_detail in order_details:
            db.session.delete(order_detail)
            db.session.commit()
        order = Orders.query.filter_by(orderid=order_id).first()
        if order:
            db.session.delete(order)
            db.session.commit()

        return jsonify({'status': 'success'})


class DisplayRecord(Resource):
    @staticmethod
    def get():
        orders = Orders.query.all()
        output = []
        for order in orders:
            order_detail = OrderDetails.query.filter_by(orderid=order.orderid).first()
            staff = Staff.query.filter_by(staffid=order_detail.staffid).first()
            payment = Payment.query.filter_by(orderid=order.orderid).first()
            output.append(
                {'orderId': order.orderid, 'staffId': staff.staffid, 'shift': staff.shift,
                 'totalAmount': payment.totalamount, 'date': order.date.isoformat()}
            )
        return jsonify(output)


class DisplayOrderStatus(Resource):
    @staticmethod
    def get():
        orders = Orders.query.all()
        output = []
        for order in orders:
            output.append({'orderID': order.orderid, 'orderStatus': order.orderstatus})
        return jsonify(output)


class SetOrderStatus(Resource):
    @staticmethod
    def post():
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
    @staticmethod
    def post():
        data = request.get_json()
        order_id = data['orderID']

        order = Orders.query.filter_by(orderid=order_id).first()
        if not order or order.orderstatus != 3:
            return jsonify({'status': 'failure', 'message': 'Order is not served yet'})

        total_amount = 0
        order_details = OrderDetails.query.filter_by(orderid=order_id).all()
        for order_detail in order_details:
            total_amount += order_detail.totalamount

        payment = Payment(totalamount=total_amount, orderid=order_id)
        db.session.add(payment)
        db.session.commit()

        return jsonify({'status': 'success', 'paymentID': payment.paymentid, 'totalamount': total_amount})


class DisplayIngredients(Resource):
    @staticmethod
    def get():
        ingredients = Ingredients.query.all()
        output = []
        for ingredient in ingredients:
            output.append(
                {'ingredientID': ingredient.ingredientid, 'name': ingredient.name,
                 'threshold': ingredient.threshold, 'amount': ingredient.amount, 'itemID': ingredient.itemid})
        return jsonify(output)


class AddIngredient(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        ingredient_name = data['ingredientName']
        amount = data['amount']
        threshold = data['threshold']
        item_id = data['itemID']

        existing_ingredient = Ingredients.query.filter_by(name=ingredient_name, itemid=item_id).first()
        if existing_ingredient:
            return jsonify({'status': 'failure', 'message': 'Ingredient already exists'})

        max_ingredient_id = db.session.query(db.func.max(Ingredients.ingredientid)).first()[0]
        new_ingredient_id = max_ingredient_id + 1

        ingredient = Ingredients(ingredientid=new_ingredient_id, name=ingredient_name,
                                 amount=amount, threshold=threshold, itemid=item_id)
        db.session.add(ingredient)
        db.session.commit()

        return jsonify({'status': 'success', 'ingredientID': new_ingredient_id})


class EditIngredient(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        ingredient_id = data['ingredientID']
        new_name = data['newName']
        new_amount = data['newAmount']
        new_threshold = data['newThreshold']

        ingredient = Ingredients.query.filter_by(ingredientid=ingredient_id).first()
        item_id = ingredient.itemid

        existing_ingredient = Ingredients.query.filter_by(name=new_name, itemid=item_id).first()
        if existing_ingredient:
            return jsonify({'status': 'failure', 'message': 'Ingredient already exists'})

        if not ingredient:
            return jsonify({'status': 'failure'})
        if int(new_amount) < 0 or int(new_threshold) < 0:
            return jsonify({'status': 'failure', 'message': 'Amount and threshold must be non-negative'})

        ingredient.name = new_name
        ingredient.amount = new_amount
        ingredient.threshold = new_threshold
        db.session.commit()

        if ingredient.amount < ingredient.threshold:
            item = Menu.query.filter_by(itemid=ingredient.itemid).first()
            item.instock = 2
            db.session.commit()

        return jsonify({'status': 'success'})


class RemoveIngredient(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        ingredient_id = data['ingredientID']
        ingredient = Ingredients.query.filter_by(ingredientid=ingredient_id).first()
        if not ingredient:
            return jsonify({'status': 'failure'})
        db.session.delete(ingredient)

        # Re-arrange ingredient IDs
        ingredients = Ingredients.query.filter(Ingredients.ingredientid > ingredient_id).all()
        for ingredient in ingredients:
            ingredient.ingredientid -= 1
        db.session.commit()

        return jsonify({'status': 'success'})


class ResetIngredientAmounts(Resource):
    @staticmethod
    def post():
        ingredients = Ingredients.query.all()
        for ingredient in ingredients:
            ingredient.amount = 20
        db.session.commit()
        return jsonify({'status': 'success'})


api.add_resource(SignUp, '/signup')  # Admin
api.add_resource(GetStaffList, '/staff_list')  # Admin
api.add_resource(EditStaff, '/edit_staff')  # Admin
api.add_resource(RemoveStaff, '/remove_staff')  # Admin
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
api.add_resource(ResetIngredientAmounts, '/reset_ingredient_amounts')  # Cook

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
