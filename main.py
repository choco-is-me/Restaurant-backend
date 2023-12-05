from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class NewTable(Resource):
    def post(self):
        # Assigns a new table when a new guest comes in the restaurant.
        pass

class OrderFood(Resource):
    def post(self):
        # Displays the menu for the customer to order.
        pass

class Confirm(Resource):
    def post(self):
        # Confirms the food ordered in the menu.
        pass

class NewTicket(Resource):
    def post(self):
        # Generates a ticket when food is ordered and updates it to the kitchen.
        pass

class Serve(Resource):
    def post(self):
        # Confirms that the food has been served to the guest.
        pass

class NewPayment(Resource):
    def post(self):
        # Generates a receipt based on the total price when the guest pays.
        pass

class NewRating(Resource):
    def post(self):
        # Records the rating from the guest for the restaurant.
        pass

api.add_resource(NewTable, '/api/tables/new')
api.add_resource(OrderFood, '/api/food/order')
api.add_resource(Confirm, '/api/food/confirm')
api.add_resource(NewTicket, '/api/ticket/new')
api.add_resource(Serve, '/api/food/serve')
api.add_resource(NewPayment, '/api/payment/new')
api.add_resource(NewRating, '/api/rating/new')

if __name__ == '__main__':
    app.run(debug=True)
