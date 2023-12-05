from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api

app = Flask("SOA") # Changed the first parameter to the app directory
api = Api(app)


class NewTable(Resource):
    def post(self):
        # Assigns a new table when a new guest comes in the restaurant.
        return make_response(jsonify({"message": "New table assigned!"}), 200)


class OrderFood(Resource):
    def post(self):
        # Displays the menu for the customer to order.
        return make_response(jsonify({"message": "Menu displayed!"}), 200)


class Confirm(Resource):
    def post(self):
        # Confirms the food ordered in the menu.
        return make_response(jsonify({"message": "Order confirmed!"}), 200)


class NewTicket(Resource):
    def post(self):
        # Generates a ticket when food is ordered and updates it to the kitchen.
        return make_response(jsonify({"message": "Ticket generated!"}), 200)


class Serve(Resource):
    def post(self):
        # Confirms that the food has been served to the guest.
        return make_response(jsonify({"message": "Food served!"}), 200)


class NewPayment(Resource):
    def post(self):
        # Generates a receipt based on the total price when the guest pays.
        return make_response(jsonify({"message": "Receipt generated!"}), 200)


class NewRating(Resource):
    def post(self):
        # Records the rating from the guest for the restaurant.
        return make_response(jsonify({"message": "Rating recorded!"}), 200)


api.add_resource(NewTable, '/api/tables/new')
api.add_resource(OrderFood, '/api/food/order')
api.add_resource(Confirm, '/api/food/confirm')
api.add_resource(NewTicket, '/api/ticket/new')
api.add_resource(Serve, '/api/food/serve')
api.add_resource(NewPayment, '/api/payment/new')
api.add_resource(NewRating, '/api/rating/new')

if __name__ == "__main__":
    app.run(port=8000, debug=True) # Changed the port to 8000
