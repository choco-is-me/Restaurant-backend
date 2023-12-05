from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

app = Flask("SOA")
api = Api(app)
Base = declarative_base(metadata=SQLModel.metadata)
engine = create_engine('sqlite:////Users/chocoisme/Desktop/main.sqbpro')
Session = sessionmaker(bind=engine)
session = Session()


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


api.add_resource(NewTable, '/api/tables/new')
api.add_resource(OrderFood, '/api/food/order')
api.add_resource(NewTicket, '/api/ticket/new')
api.add_resource(NewPayment, '/api/payment/new')
api.add_resource(NewRating, '/api/rating/new')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
