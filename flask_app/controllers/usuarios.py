import os
from flask_app.models.usuario import Usuario
from flask import flash, redirect, request, session
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)

@app.route("/agregar_usuario", methods=["POST"])
def agregar_usuario():
    
    if not Usuario.validate_user(request.form):
        return redirect('/administracion')

    if Usuario.get_by_mail(request.form['mail']):
        flash(f"El correo {request.form['mail']} ya esta registrado", "error")
        return redirect('/administracion')
    
    hash_pass = bcrypt.generate_password_hash(request.form['contraseña'])
    
    data = {
        "identificacion": request.form["identificacion"],
        "nombre": request.form["nombre"],
        "apellidoP" : request.form["apellidoP"],
        "apellidoM" : request.form["apellidoM"],
        "tipo" : request.form["tipo"],
        "telefono" : request.form["telefono"],
        "mail" : request.form["mail"],
        "contraseña" : hash_pass
    }
    Usuario.save(data)
    flash(f"exito al agregar el usuario {data['nombre']}", "success")
    return redirect("/administracion")

@app.route("/modificar_usuario/<id>", methods=["POST"])
def modificar_usuario(id):

    if not User.validate_update(request.form):
        return redirect('/user/account')
    
    email_data=User.email_bbdd(request.form['mail'])
    
    if email_data==False:
        print("no hay usuarios con ese correo")
    elif session['mail']==email_data['email']:
        print("No quiere modificar su correo")
    else:
        flash(f"El correo {request.form['mail']} ya esta registrado", "error")
        return redirect('/user/account')
    data = {
        "id":id,
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "mail" : request.form["mail"]
    }
    User.update(data)
    flash(f"exito al modificar el usuario {data['nombre']}", "success")
    return redirect("/administracion")

@app.route("/eliminar/<id>")
def eliminar(id):
    
    if 'mail' in session:
        Usuario.delete(id)
        flash("Usuario eliminado exitosamente","success")
        return redirect("/administracion")
    else:
        return redirect("/")

   
