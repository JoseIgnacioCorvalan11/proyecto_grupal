import os
from flask_app.models.user import User
from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)

@app.route("/")
def index():
    if 'mail' in session:
        return redirect("/inicio")
    else:
        return render_template("login.html")


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/inicio")
def inicio():
    return render_template("index.html")
    
    
@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    if not User.validate_login(request.form):
        return redirect('/')

    usuario=User.email_bbdd(request.form['mail'])
    if not usuario:
        flash("Usuario o clave incorrecta", "error")    
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.get('password'), request.form['contraseña']):
        flash("Usuario o clave incorrecta", "error")
        return redirect("/")

    session['mail']=usuario.get('email')
    session['id']=usuario.get('id')
    session['usuario']=usuario.get('first_name')
    return redirect("/dashboard")
    
@app.route("/cerrar_session")
def cerrar_session():
    session.clear()
    return redirect ("/")

@app.route("/user/account")
def usuario_modificar():
    if 'mail' in session:
        id=session['id']
        usuario=User.get_by_id(id)
        return render_template("modificar.html", usuario=usuario)
    else:
        return redirect("/")