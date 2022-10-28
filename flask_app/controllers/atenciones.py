import imp
import os
from flask_app.models.atencion import Atencion
from flask import flash, redirect, render_template, request, session
from flask_app import app

@app.route("/agregar_atencion", methods=["POST"])
def agregar_atencion():
    
    data = {
        "fecha": request.form['fecha'],
        "veterinario" : request.form['veterinario'],
        "mascota" : request.form['mascota'],
        "tratamiento" : request.form['tratamiento'],
        "medicamento" : request.form['medicamento']
    }
    print(data)
    Atencion.save(data)
    flash("exito al agregar la atencion", "success")
    return redirect("/atenciones")

@app.route("/eliminar_atencion/<id>")
def eliminar_atencion(id):
    if 'mail' in session:
        print(id)
        Atencion.delete(id)
        flash("Atencion eliminada exitosamente","success")
        return redirect("/atenciones")
    else:
        return redirect("/")
