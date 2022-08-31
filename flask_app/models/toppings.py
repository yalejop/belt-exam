from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Topping:
    
    def __init__(self,data):
        self.id = data['id']
        self.topping_name = data['topping_name']
        self.price = data['price']
        
        self.on_ice_cream = []
        
        
    @classmethod
    def get_all_toppings(cls):
        query = "SELECT toppings.id, topping_name, price FROM toppings LEFT JOIN ice_creams_has_toppings ON ice_creams_has_toppings.topping_id = toppings.id LEFT JOIN ice_creams ON ice_creams_has_toppings.ice_cream_id = ice_creams.id;" #LEFT JOIN 
        results = connectToMySQL('gelato_store_project').query_db(query) #Lista de diccionarios
        toppings = []
        for topping in results:
            toppings.append(cls(topping)) #cls(receta) -> Instancia de receta, Agregamos la instancia a mi lista de recetas
        return toppings
    
    @classmethod
    def get_topping_with_ice_creams( cls , data ):
        query = "SELECT * FROM toppings LEFT JOIN ice_creams_has_toppings ON ice_creams_has_toppings.topping_id = toppings.id LEFT JOIN ice_creams ON ice_creams_has_toppings.ice_cream_id = ice_creams.id WHERE toppings.id = %(id)s;"
        results = connectToMySQL('gelato_store_project').query_db( query , data )
        # los resultados serán una lista de objetos topping (aderezo) con el helado adjunto a cada fila 
        topping = cls( results[0] )
        for row_from_db in results:
            # ahora parseamos los datos topping para crear instancias de aderezos y agregarlas a nuestra lista
           ice_cream_data = {
               "id" : row_from_db["ice_creams.id"],
               "name" : row_from_db["name"],
               "bun" : row_from_db["bun"],
               "calories" : row_from_db["calories"],
               "created_at" : row_from_db["toppings.created_at"],
               "updated_at" : row_from_db["toppings.updated_at"]
           }
           topping.on_burgers.append( burger.Burger( burger_data ) )
        return topping