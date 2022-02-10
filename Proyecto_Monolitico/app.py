from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#todo conectado a la base de datos de MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bdcargamos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#todo creando el modelo de productos que se convertira en una tabla
#todo este proceso se llama migracion

class Productos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre_producto=db.Column(db.Text)
    precio=db.Column(db.Integer)
    state=db.Column(db.Boolean,default=True)
    picture=db.Column(db.Text)
    
#todo creando los objetos de Base de datos    
db.create_all()    
    


@app.route('/')
def index():
    #todo Select * from productos
    #todo queryset - motor de consultas
    productos=Productos.query.all()
    template_name="index.html"
    return render_template(template_name,prod=productos)

@app.route('/admin')
def administrador():
    template_name="administrador.html"
    return render_template(template_name)



app.run(debug=True)    

