import os
from flask_app.models.usuario import Usuario
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

@app.route("/atenciones")
def atenciones():
    if 'mail' in session:
        if session['tipo'] <3:
            return render_template("atenciones.html")
        else:
            flash("No tienes los accesos", "error")
            return redirect("/")
    else:
        return redirect("/")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/mascotas")
def mascotas():
    if 'mail' in session:
        if session['tipo'] <2:
            return render_template("mascotas.html")
        else:
            flash("No tienes los accesos", "error")
            return redirect("/")
    else:
        return redirect("/")

@app.route("/inicio")
def inicio():
    if 'mail' in session:
        return render_template("index.html")
    else:
        return redirect("/")

@app.route("/administracion")
def administracion():
    if 'mail' in session:
        if session['tipo'] <2:
            usuarios=Usuario.get_all()
            return render_template("administracion.html", usuarios=usuarios)
        else:
            flash("No tienes los accesos", "error")
            return redirect("/")
    else:
        return redirect("/")
    
    
@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    if not Usuario.validate_login(request.form):
        return redirect('/')

    usuario=Usuario.get_by_mail(request.form['mail'])
    if not usuario:
        flash("Usuario o clave incorrecta", "error")    
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.get('contraseña'), request.form['contraseña']):
        flash("Usuario o clave incorrecta", "error")
        return redirect("/")

    session['mail']=usuario.get('mail')
    session['id']=usuario.get('identificacion')
    session['nombre']=usuario.get('nombre')
    session['tipo']=usuario.get('tipo_usuario')
    return redirect("/inicio")
    
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