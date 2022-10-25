import os

from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.regex import EMAIL_REGEX


class Usuario:
    def __init__( self , data ):
        self.identificacion = data['identificacion']
        self.nombre = data['nombre']
        self.apellidoP = data['apellidoP']
        self.apellidoM = data['apellidoM']
        self.telefono = data['telefono']
        self.mail = data['mail']
        self.contraseña = data['contraseña']
        self.tipo_usuario = data['tipo_usuario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( identificacion, nombre , apellidoP, apellidoM, telefono, mail, contraseña, tipo_usuario, created_at, updated_at ) VALUES ( %(nombre)s , %(nombre)s , %(apellidoP)s , %(apellidoM)s , %(telefono)s , %(mail)s , %(contraseña)s, %(tipo_usuario)s , NOW() , NOW() );"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )
    
    @classmethod
    def update(cls, data ):
        query = "UPDATE usuarios SET nombre=%(nombre)s , apellidoP=%(apellidoP)s , apellidoM=%(apellidoM)s ,  mail= %(mail)s, updated_at=NOW() where identificacion =%(identificacion)s"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def delete(cls, id ):
        query = "DELETE from usuarios WHERE identificacion = %(identificacion)s;"
        data={
            'id':id
        }
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * from usuarios where identificacion = %(identificacion)s;"
        data={
            'id':id
        }
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)
        print(results)
        if not results:
            return False
        id_data = results [0]
        return id_data


    @classmethod
    def validate_user(cls, data):
        is_valid = True
        if len((data['nombre'])) < 2:
            flash("Debes ingresar minino 3 letras en el nombre.", "error")
            is_valid = False
        if len(data['apellidoP']) < 2:
            flash("Debes ingresar minino 3 letras en el apellido.", "error")
            is_valid = False
        if len(data['apellidoM']) < 2:
            flash("Debes ingresar minino 3 letras en el apellido.", "error")
            is_valid = False
        if len(data['contraseña']) < 8:
            flash("Debes ingresar al menos 8 caracteres en la contraseña.", "error")
            is_valid = False
        if data['contraseña'] != data['confirm_contraseña'] :
            flash("Las contraseñas deben ser iguales", "error")
            is_valid = False
        if not EMAIL_REGEX.match(data['mail']):
            flash("Formato de correo incorrecto", "error")
            is_valid = False
        
        return is_valid

    # Metodo para validar registro login
    @classmethod
    def validate_login(cls, data):
        is_valid = True
        if len(data['contraseña']) <1 :
            flash("Debes ingresar la contraseña.", "error")
            is_valid = False
        if len(data['mail']) <1 :
            flash("Debes ingresar el correo.", "error")
            is_valid = False
        
        return is_valid

    # Metodo para validar la actualizacion
    @classmethod
    def validate_update(cls, data):
        print("llega al validador")
        is_valid = True
        if len((data['nombre'])) < 2:
            flash("Debes ingresar minino 3 letras en el nombre.", "error")
            is_valid = False
        if len(data['apellido']) < 2:
            flash("Debes ingresar minino 3 letras en el apellido.", "error")
            is_valid = False
        if not EMAIL_REGEX.match(data['mail']):
            flash("Formato de correo incorrecto", "error")
            is_valid = False
       
        return is_valid