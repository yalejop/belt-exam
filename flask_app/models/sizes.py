from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Size:
    
    def __init__(self, data):
        self.id = data['id']
        self.size_name = data['size_name']
        self.description = data['description']
        self.price = data['price']
    
    @classmethod
    def get_all_sizes(cls):
        query = "SELECT * FROM ice_creams_sizes;"
        results = connectToMySQL('gelato_store_project').query_db(query)
        sizes = []
        for size in results:
            sizes.append(cls(size))
        return sizes