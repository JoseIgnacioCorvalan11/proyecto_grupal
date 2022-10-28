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
        self.veterinario = data['veterinario']
        self.mascota = data['mascota']
        self.medicamento = data['medicamento']



    @classmethod
    def save(cls, data):
        query = "INSERT INTO Atencion( tratamiento, fecha, created_at, updated_at, veterinario, mascota, medicamento) VALUES ( %(tratamiento)s, %(fecha)s, NOW(), NOW(), %(veterinario)s, %(mascota)s, %(medicamento)s  );"
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
    def get_all(cls):
        query = "select a.id, m.nombre as nombre_mascota,  concat(u.nombre,' ', u.apellido_p) as veterinario, u.identificacion as id_vet, a.tratamiento, d.descripcion as medicamento, concat(o.nombre, ' ', o.apellido_p) as dueño from atencion a join mascotas m on a.mascota=m.id join usuarios u on a.veterinario=u.identificacion join medicamentos d on a.medicamento=d.id join usuarios o on o.identificacion = m.dueño;"
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query)
        atenciones = []
        for atencion in results:
            atenciones.append((atencion))
        return atenciones
