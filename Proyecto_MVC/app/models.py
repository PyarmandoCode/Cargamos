from app import db

class Grupos(db.Model):
    codgrupo=db.Column(db.String(3),primary_key=True)
    nombre_grupo=db.Column(db.String(50))
    estado=db.Column(db.Integer)
    
    
