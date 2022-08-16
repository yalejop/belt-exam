from flask_app.config.mysqlconnection import connectToMySQL

import re #importamos expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#crear una expresion regular para verificar que tengamos el email con el formato correcto

from flask import flash

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = 'INSERT INTO users(first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
        result = connectToMySQL('belt-exam').query_db(query, formulario)
        return result 
    
    @staticmethod
    def valida_usuario(formulario):
        
        es_valido = True

        #validar que mi nombre tenga mas de 2 caracteres
        if formulario['first_name'] == "":
            flash('Nombre debe tener algo de contenido', 'registro')
            es_valido = False
        elif len(formulario['first_name']) < 3:
            flash('Nombre debe de tener al menos 3 caracteres', 'registro')
            es_valido = False

        if formulario['last_name'] == "":
            flash('Apellido debe tener algo de contenido', 'registro')
            es_valido = False
        elif len(formulario['last_name']) < 3:
            flash('Apellido debe de tener al menos 3 caracteres', 'registro')
            es_valido = False

        if not EMAIL_REGEX.match(formulario['email']):
            flash('Email Invalido', 'registro')
            es_valido = False

        if len(formulario['password']) < 8:
            flash('Contraseña debe tener al menos 6 caracteres', 'registro')
            es_valido = False

        if formulario['password'] != formulario['confirm_password']:
            flash('Contraseña no coinciden', 'registro')
            es_valido = False

        #Consultar si YA existe el correo
        query = 'SELECT * FROM users WHERE email = %(email)s'
        result = connectToMySQL('belt-exam').query_db(query, formulario)
        if len(result) >= 1:
            flash('E-mail registrado Previamente', 'registro')
            es_valido = False
        
        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        result = connectToMySQL('belt-exam').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            user = cls(result[0])
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        result = connectToMySQL('belt-exam').query_db(query, formulario)
        user = cls(result[0])
        return user
            