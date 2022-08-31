from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Delivery:
    
    def __init__(self, data):
        self.id = data['id']
        self.delivery_type = data['delivery_type']
        self.price = data['price']
    
    @classmethod
    def get_all_types(cls):
        query = "SELECT * FROM ice_creams_deliveries;"
        results = connectToMySQL('gelato_store_project').query_db(query)
        deliveries = []
        for delivery in results:
            deliveries.append(cls(delivery))
        return deliveries