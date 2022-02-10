from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

#todo Creando la aplicacion
app=Flask(__name__)

#todo configurando la aplicacion con la BD
app.config.from_object(Config)

#todo conectando mi aplicacion con mi BD
db=SQLAlchemy(app)

from app import routes,models