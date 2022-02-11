from app import db

class Grupos(db.Model):
    codgrupo=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_grupo=db.Column(db.String(50))
    estado=db.Column(db.Integer)
    
    
