#todo importando la libreria de Flask
from flask import Flask,render_template

#todo creando el proyecto
app=Flask(__name__)

data_cargamos=[
    {"nombre":"Alicia","apellido":"Guerrero"},
    {"nombre":"Carlos","apellido":"Aguilar"},
    {"nombre":"Ingrid","apellido":"Guerrero"},
    {"nombre":"Javier","apellido":"Catalan"},
    {"nombre":"Lhordes","apellido":"Catln"},
]

#todo creando mi primera ruta
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cargamos')
def cargamos():
    return render_template("cargamos.html",alumnos=data_cargamos)

@app.route('/acercade')
def acercade():
    return render_template("acercade.html")

    
#todo ejecutando el servidor        
app.run(debug=True)    



