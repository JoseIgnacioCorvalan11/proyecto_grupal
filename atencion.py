import os

from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Atencion:
    def __init__( self , data ):
        self.id = data['id']
        self.tratamiento = data['tratamiento']
        self.fecha = data['fecha']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.peso = data['peso']
        self.veterinario = data['veterinario']
        self.mascota = data['mascota']



    @classmethod
    def save(cls, data):
        query = "INSERT INTO Atencion( id, tratamiento, fecha, created_at, updated_at) VALUES ( %(id)s, %(tratamiento)s, %(fecha)s, NOW(), NOW() );"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE Atencion SET id = %(id)s, tratamiento = %(tratamiento)s, fecha = %(fecha)s, updated_at = NOW();,peso = %(peso)s ,mascota = %(mascota)s;"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE from Atencion WHERE id = %(id)s;"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)

    @classmethod
    def get_all(cls, data):
        print(data, "esto esta en la data de atencion")
        query = "SELECT * FROM Atencion;"
        results =connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)
        print(results, "esto esta en results")
        atenciones = []
        for atencion in results:  # type: ignore
            atenciones.append(cls(atencion))
        return atenciones