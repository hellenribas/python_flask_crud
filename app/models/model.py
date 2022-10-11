from flask.json import JSONEncoder
from app import connection

class Proprietarios(connection.Model):
    __tablename__ = "proprietarios"

    id=connection.Column(connection.Integer, primary_key=True)
    name=connection.Column(connection.String(45))
    oportunidade_venda=connection.Column(connection.Boolean)

class Carros(connection.Model):

    id=connection.Column(connection.Integer, primary_key=True)
    modelo=connection.Column(connection.String(45))
    cor=connection.Column(connection.String(45))
    proprietario_id=connection.Column(connection.Integer)

connection.create_all()
