from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cargamos2022@localhost/bdcargamos'
db = SQLAlchemy(app)

@app.route('/')
def index():
    template_name="index.html"
    return render_template(template_name)


app.run(debug=True)    

