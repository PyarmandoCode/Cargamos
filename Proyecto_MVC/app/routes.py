from re import A
from flask import render_template
#todo importando la aplicacion y la conexion a la base de datos
from app import app,db
#todo importando el modelo = tabla
from app.models import Grupos,Alumnos

@app.route('/')
def index():
    #todo el objeto grupo almacena todos los registros de la tabla
    #todo select * from grupos
    gps= Grupos.query.all()
    template_name="index.html"
    return render_template(template_name,grupos=gps)

@app.route('/alumnos')
def alumnos():
    #todo el objeto grupo almacena todos los registros de la tabla
    #todo select * from grupos
    alumnos= Alumnos.query.all()
    template_name="alumnos.html"
    return render_template(template_name,al=alumnos)
    


