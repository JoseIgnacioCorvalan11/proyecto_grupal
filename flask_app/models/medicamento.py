import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Medicamento:
    def __init__( self , data ):
        self.id = data['id']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __iter__(self):
        return self

    @staticmethod
    def validar_descripcion(formulario):
        valido = True
        if len(formulario['descripcion']) < 10:
            flash("tu descripcion debe tener al menos 10 caracteres")
            valido = False
        return valido


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Medicamentos( id ,descripcion, created_at, updated_at) VALUES( %(id)s, %(descripcion)s, NOW(), NOW() );"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE Medicamentos SET id = %(id)s, descripcion = %(descripcion)s, updated_at = NOW();"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def get_all(cls, data):
        print(data, "esto esta en el data medico")
        query = "SELECT * FROM Medicamentos;"
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)
        print("QUE HAY AQUI?", results)
        medicamentos = []
        for medicamento in results:  # type: ignore
            medicamentos.append(cls(medicamento))
        return medicamentos


