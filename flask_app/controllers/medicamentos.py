import os
from flask_app.models.medicamento import Medicamento
from flask import flash, redirect, render_template, request, session
from flask_app import app

@app.route("/medicamentos")
def medicamentos(data, id, descripcion):
    if not Medicamento.validar_descripcion(request.form):
        return redirect("/medicamentos")
    data = {
        id : id ,
        descripcion : descripcion
    }
    data_medicamentos = data
    return render_template('medicamentos.html', data_medicamentos=data_medicamentos)

