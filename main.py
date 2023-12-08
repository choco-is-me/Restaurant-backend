from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import sqlite3

app = Flask("SOA")
api = Api(app)


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
            cursor.execute("INSERT INTO Guest (GuestID, Name, TableNo) VALUES (?, ?, ?)",
                           (args['GuestID'], args['Name'], args['TableNo']))
            conn.commit()
            conn.close()
            return make_response(jsonify({
                "message": f"The table number: {args['TableNo']} have been successfully booked for guest: {args['Name']} with the guest id: {args['GuestID']}."}),
                200)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)


class Table(Resource):
    def delete(self, GuestID):
        try:
            conn = sqlite3.connect('main.db', timeout=10)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Guest WHERE GuestID = ?", (GuestID,))
            conn.commit()
            conn.close()
            return make_response(jsonify({"message": f"Guest with id: {GuestID} has been successfully removed."}), 200)
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


class OrderFood(Resource):
    def post(self):
        return make_response(jsonify({"message": "Ordered Successfully"}), 200)


class NewTicket(Resource):
    def post(self):
        # Generates a ticket when food is ordered and updates it to the kitchen.
        return make_response(jsonify({"message": "Ticket generated!"}), 200)


class NewPayment(Resource):
    def post(self):
        # Generates a receipt based on the total price when the guest pays.
        return make_response(jsonify({"message": "Receipt generated!"}), 200)


api.add_resource(NewTable, '/api/tables/new')
api.add_resource(Table, '/api/tables/<int:GuestID>')
api.add_resource(OrderFood, '/api/food/order')
api.add_resource(NewTicket, '/api/ticket/new')
api.add_resource(NewPayment, '/api/payment/new')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
