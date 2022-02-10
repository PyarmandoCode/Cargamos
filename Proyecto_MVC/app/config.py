# todo CLASE que nos permitira conectarnos a la BD

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bdcargamos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
