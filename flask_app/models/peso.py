import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Peso:
    def __init__( self , data ):
        self.id = data['id']
        self.descripcion = data['peso']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __iter__(self):
        return self

    @staticmethod
    def validar_peso(formulario):
        valido = True
        if len(formulario['peso']) > 0:
            flash("El peso es mayor a 0")
            valido = False
        return valido


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO peso( id ,peso, created_at, updated_at) VALUES( %(id)s, %(peso)s, NOW(), NOW() );"
        return connectToMySQL(os.environ.get("mybd")).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE peso SET id = %(id)s, peso = %(peso)s, updated_at = NOW();"
        return connectToMySQL(os.environ.get("mybd")).query_db( query, data )

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM peso;"
        results = connectToMySQL(os.environ.get("mybd")).query_db(query, data)
        pesos = []
        for peso in results:
            pesos.append(cls(peso))
        return pesos
