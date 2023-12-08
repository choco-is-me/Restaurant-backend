from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
import sqlite3


app = Flask("SOA")
api = Api(app)


class TestDB(Resource):
    def get(self):
        try:
            conn = sqlite3.connect('main.db')
            conn.close()
            return make_response(jsonify({"message": "Opened database successfully"}), 200)
        except sqlite3.Error as e:
            return make_response(jsonify({"message": f"An error occurred: {e.args[0]}"}), 500)


class NewTable(Resource):
    def post(self):
        # Assigns a new table when a new guest comes in the restaurant.
        return make_response(jsonify({"message": "New table assigned!"}), 200)


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


class NewRating(Resource):
    def post(self):
        # Records the rating from the guest for the restaurant.
        return make_response(jsonify({"message": "Rating recorded!"}), 200)


api.add_resource(TestDB, '/api/testdb')
api.add_resource(NewTable, '/api/tables/new')
api.add_resource(OrderFood, '/api/food/order')
api.add_resource(NewTicket, '/api/ticket/new')
api.add_resource(NewPayment, '/api/payment/new')
api.add_resource(NewRating, '/api/rating/new')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
