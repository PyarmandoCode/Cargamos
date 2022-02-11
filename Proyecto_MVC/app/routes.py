from flask import render_template
#todo importando la aplicacion y la conexion a la base de datos
from app import app,db
#todo importando el modelo = tabla
from app.models import Grupos

@app.route('/')
def index():
    #todo el objeto grupo almacena todos los registros de la tabla
    #todo select * from grupos
    gps= Grupos.query.all()
    template_name="index.html"
    return render_template(template_name,grupos=gps)


    


