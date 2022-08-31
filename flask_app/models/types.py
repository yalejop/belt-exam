from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Type:
    
    def __init__(self, data):
        self.id = data['id']
        self.type_name = data['type_name']
        self.description = data['description']
        self.price = data['price']
    
    @classmethod
    def get_all_types(cls):
        query = "SELECT * FROM ice_creams_types;"
        results = connectToMySQL('gelato_store_project').query_db(query)
        types = []
        for type in results:
            types.append(cls(type))
        return types