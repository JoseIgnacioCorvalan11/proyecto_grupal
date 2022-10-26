import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Mascota:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.tipo_mascota = data['tipo_mascota']
        self.sexo = data['sexo']
        self.raza = data['raza']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dueño = data['dueño']
    def __iter__(self):
        return self

    @staticmethod
    def validar_nombre(formulario):
        valido = True
        if len(formulario['nombre']) < 2:
            flash("El nombre de la mascota debe tener al menos 2 caracteres")
            valido = False
        return valido


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO mascotas ( id , nombre, tipo_mascota, sexo, raza, created_at, updated_at, dueño) VALUES( %(id)s, %(nombre)s, %(tipo_mascota)s, %(sexo)s, %(raza)s, NOW(), NOW(), %(dueño)s );"
        return connectToMySQL(os.environ.get("bd_veterinaria")).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE mascotas SET id = %(id)s, nombre = %(nombre)s, tipo_mascota = %(tipo_mascota)s, sexo = %(sexo)s, raza = %(raza)s, created_at = NOW(), updated_at = NOW(), dueño = %(dueño)s;"
        return connectToMySQL(os.environ.get("bd_veterinaria")).query_db( query, data )

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM mascotas;"
        results = connectToMySQL(os.environ.get("bd_veterinaria")).query_db(query, data)
        mascotas = []
        for mascota in results:
            mascotas.append(cls(mascota))
        return mascotas
