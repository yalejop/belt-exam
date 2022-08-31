
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Ice_cream:

    def __init__(self, data):
        self.id = data['id']
        self.quantity = data['quantity']
        self.ice_cream_type = data['ice_cream_type']
        self.ice_cream_size = data['ice_cream_size']
        self.ice_cream_delivery = data['ice_cream_delivery']
        self.toppings = []
        
    # def get_all_types(cls):
    #     query = "SELECT toppings.id, topping_name, price FROM toppings LEFT JOIN ice_creams_has_toppings ON ice_creams_has_toppings.topping_id = toppings.id LEFT JOIN ice_creams ON ice_creams_has_toppings.ice_cream_id = ice_creams.id;" #LEFT JOIN 
    #     results = connectToMySQL('gelato_store_project').query_db(query) #Lista de diccionarios
    #     toppings = []
    #     for topping in results:
    #         toppings.append(cls(topping)) #cls(receta) -> Instancia de receta, Agregamos la instancia a mi lista de recetas
    #     return toppings