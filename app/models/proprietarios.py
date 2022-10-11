from flask.json import JSONEncoder

class Proprietarios(object):

  def __init__(self, name, oportunidade_venda):
    self.name = name
    self.oportunidade_venda = oportunidade_venda


class PropEnconder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Proprietarios):
      return obj.__dict__
    return super(
      PropEnconder,
      self
    ).default(obj)
