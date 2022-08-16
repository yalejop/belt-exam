from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Appointment:

    def __init__(self, data):
        self.id = data['id']
        self.tasks = data['tasks']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_appointment(formulario):
        es_valido = True
        
        if formulario['tasks'] == "":
            flash('Task debe tener algo de contenido', 'appointment')
            es_valido = False
        
        if formulario['date'] == "":
            flash('Debes escoger una fecha', 'appointment')
            es_valido = False

        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO appointments (tasks, date, status, user_id) VALUES ( %(tasks)s, %(date)s, %(status)s, %(user_id)s )"
        results = connectToMySQL('belt-exam').query_db(query, formulario)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM appointments" 
        results = connectToMySQL('belt-exam').query_db(query) #Lista de diccionarios
        appointments = []
        for appointment in results:
            appointments.append(cls(appointment)) #cls(appointments) -> Instancia de appointment, Agregamos la instancia a mi lista de appointments
        return appointments

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT * FROM appointments WHERE appointments.id = %(id)s" 
        result = connectToMySQL('belt-exam').query_db(query, formulario) 
        appointment = cls(result[0]) 
        return appointment

    @classmethod
    def update(cls, formulario):   
        query = "UPDATE appointments SET tasks = %(tasks)s, date = %(date)s, status = %(status)s WHERE id = %(id)s"
        result = connectToMySQL('belt-exam').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('belt-exam').query_db(query, formulario)
        return result