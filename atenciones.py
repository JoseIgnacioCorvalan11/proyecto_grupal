import imp
import os
from flask_app.models.atencion import Atencion
from flask import flash, redirect, render_template, request, session
from flask_app import app

@app.route("/atenciones_veterinario")
def atencion(data, id, tratamiento, fecha, peso, mascota):
    data = {
        id: id,
        tratamiento : tratamiento,
        fecha: request.form['fecha'],
        peso : peso,
        mascota : mascota
    }
    data_atencion = data
    return render_template("atenciones.html", data_atencion=data_atencion)

@app.route("/atenciones_usuario")
def atencion_usuario(data, id, tratamiento):
    data = {
        id : id,
        tratamiento : tratamiento
    }
    data_atencion_cliente = data
    return render_template("index.html", data_atencion_cliente=data_atencion_cliente)