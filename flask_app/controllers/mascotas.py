import imp
import os
from flask_app.models.mascota import Mascota
from flask import flash, redirect, render_template, request, session
from flask_app import app

@app.route("/mascotas_administrador")
def mascotas_admin(id, nombre, tipo_mascota, sexo, raza, dueño):
    data = {
        id : id,
        nombre : nombre,
        tipo_mascota : tipo_mascota,
        sexo : sexo,
        raza : raza,
        dueño : dueño
    }
    data_mascota_admin = data
    return render_template("atenciones.html", data_mascota_admin=data_mascota_admin)

@app.route("/mascotas")
def mascota_usuario(nombre, dueño):
    data ={
        nombre : nombre,
        dueño : dueño
    }
    data_usuario_mascota = data
    return render_template("index.html", data_usuario_mascota=data_usuario_mascota)