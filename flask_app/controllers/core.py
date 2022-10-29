import os
from flask_app.models.usuario import Usuario
from flask_app.models.medicamento import Medicamento
from flask_app.models.mascota import Mascota
from flask_app.models.atencion import Atencion
from flask import flash, redirect, render_template, request, session, make_response
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
            
            medicamentos=Medicamento.get_all()
            mascotas=Mascota.get_all_mascotas()
            atenciones=Atencion.get_all()
            return render_template("atenciones.html", medicamentos=medicamentos, mascotas=mascotas, atenciones=atenciones)
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
            dueños=Usuario.get_by_tipo(3)
            mascotas=Mascota.get_all()
            return render_template("mascotas.html", dueños=dueños, mascotas=mascotas)
        else:
            flash("No tienes los accesos", "error")
            return redirect("/")
    else:
        return redirect("/")

@app.route("/medicamentos")
def medicamentos():
    if 'mail' in session:
        if session['tipo'] <2:
            medicamentos=Medicamento.get_all()
            return render_template("medicamentos.html", medicamentos=medicamentos)
        else:
            flash("No tienes los accesos", "error")
            return redirect("/")
    else:
        return redirect("/")

@app.route("/inicio")
def inicio():
    if 'mail' in session:
        atenciones=Atencion.get_all()
        atencionesd=Atencion.get_all_by_user(session['id'])
        return render_template("index.html", atenciones=atenciones, atencionesd=atencionesd)
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
    session['apellido_p']=usuario.get('apellido_p')
    session['tipo']=usuario.get('tipo_usuario')
    return redirect("/inicio")
    
@app.route("/cerrar_session")
def cerrar_session():
    session.clear()
    return redirect ("/")
