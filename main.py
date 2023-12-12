from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import sqlite3

app = Flask("SOA")
api = Api(app)


class Login(Resource):
    def get(self, StaffID):
        try:
            conn = sqlite3.connect('main.db', timeout=10)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Staff WHERE StaffID = ?", (StaffID,))
            staff_info = cursor.fetchone()
            conn.close()
            if staff_info is not None:
                return make_response(
                    jsonify({"message": f"Welcome {staff_info[1]}, ROLE: {staff_info[2]}, Ready to work your shift: {staff_info[3]}."}), 200)
            else:
                return make_response(jsonify({"message": f"No staff found with id: {StaffID}."}), 404)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)


class NewTable(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('GuestID', required=True)
        parser.add_argument('Name', required=True)
        parser.add_argument('TableNo', required=True)
        args = parser.parse_args()

        try:
            conn = sqlite3.connect('main.db', timeout=10)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Guest (Name, TableNo) VALUES (?, ?)",
                           (args['Name'], args['TableNo']))
            conn.commit()
            conn.close()
            return make_response(jsonify({
                "message": f"The table number: {args['TableNo']} have been successfully booked for guest: {args['Name']}."}),
                200)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)

    def get(self, GuestID):
        try:
            conn = sqlite3.connect('main.db', timeout=10)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Guest WHERE GuestID = ?", (GuestID,))
            guest_info = cursor.fetchone()
            conn.close()
            if guest_info is not None:
                return make_response(
                    jsonify({"GuestID": guest_info[0], "Name": guest_info[1], "TableNo": guest_info[2]}), 200)
            else:
                return make_response(jsonify({"message": f"No guest found with id: {GuestID}."}), 404)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)


class ShowMenu(Resource):
    def post(self):
        try:
            conn = sqlite3.connect('main.db', timeout=10)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Menu")
            menu_items = cursor.fetchall()
            conn.close()
            if menu_items is not None:
                # Create a list of dictionaries, each representing a menu item
                menu_list = [{"ItemID": item[0], "Name": item[1], "Price": item[2], "InStock": item[3]} for item in menu_items]
                return make_response(jsonify(menu_list), 200)
            else:
                return make_response(jsonify({"message": "No items found in the menu."}), 404)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)


class OrderItem(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ItemID', required=True, action='append')
        parser.add_argument('Quantity', required=True, action='append')
        parser.add_argument('GuestID', required=True)  # Add this line
        args = parser.parse_args()

        try:
            conn = sqlite3.connect('main.db', timeout=10)
            cursor = conn.cursor()

            for item_id, quantity in zip(args['ItemID'], args['Quantity']):
                cursor.execute("SELECT Price FROM Menu WHERE ItemID = ?", (item_id,))
                price = cursor.fetchone()
                if price is not None:
                    total_amount = price[0] * int(quantity)
                    cursor.execute("INSERT INTO OrderDetails (GuestID, ItemID, Quantity, TotalAmount, OrderStatus) VALUES (?, ?, ?, ?, ?)",
                                   (args['GuestID'], item_id, quantity, total_amount, 0))  # Modify this line
                else:
                    return make_response(jsonify({"message": f"No item found with id: {item_id}."}), 404)

            conn.commit()
            conn.close()
            return make_response(jsonify({"message": "Order details have been successfully added."}), 200)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)


class NewTicket(Resource):
    def post(self):
        # Generates a ticket when food is ordered and updates it to the kitchen.
        return make_response(jsonify({"message": "Ticket generated!"}), 200)


class NewPayment(Resource):
    def post(self):
        # Generates a receipt based on the total price when the guest pays.
        return make_response(jsonify({"message": "Receipt generated!"}), 200)


api.add_resource(Login, '/api/login/<int:StaffID>')
api.add_resource(NewTable, '/api/tables/new')
api.add_resource(NewTable, '/api/tables/<int:GuestID>')
api.add_resource(ShowMenu, '/api/menu')
api.add_resource(OrderItem, '/api/food/order')
api.add_resource(NewTicket, '/api/ticket/new')
api.add_resource(NewPayment, '/api/payment/new')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
