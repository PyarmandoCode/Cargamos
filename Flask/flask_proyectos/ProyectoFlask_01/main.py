#todo importando la libreria de Flask
from flask import Flask,render_template

#todo creando el proyecto
app=Flask(__name__)

#todo creando mi primera ruta
@app.route('/')
def index():
    return render_template("index.html")
    
#todo ejecutando el servidor        
app.run(port="8080",debug=True)    



