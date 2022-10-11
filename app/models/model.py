from flask.json import JSONEncoder
from app import connection


class Proprietarios(connection.Model):
    id=connection.Column(connection.Integer, primary_key=True)
    name=connection.Column(connection.String(45))
    oportunidade_venda=connection.Column(connection.Boolean)


class Carros(connection.Model):

    id=connection.Column(connection.Integer, primary_key=True)
    modelo=connection.Column(connection.String(45))
    cor=connection.Column(connection.String(45))
    proprietario_id=connection.Column(connection.Integer)

#   def __init__(self, name, oportunidade_venda):
#     self.name = name
#     self.oportunidade_venda = oportunidade_venda


# class PropEnconder(JSONEncoder):
#   def default(self, obj):
#     if isinstance(obj, Proprietarios):
#       return obj.__dict__
#     return super(
#       PropEnconder,
#       self
#     ).default(obj)
