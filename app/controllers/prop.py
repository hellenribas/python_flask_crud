from crypt import methods
from app import app
from models.model import Proprietarios
from flask import render_template, request

@app.route('/proprietarios', methods=['GET'])
def getProp():
    proprietarios=Proprietarios.query.all()
    render_template('index.html', list=proprietarios)
    return 'ola, mundo'

@app.route('/proprietarios', methods=['POST'])
def createProp():
    name = request.form.get('name')
    have_car = request.form.get('have_car')
    new_prop = PROP(name, oportunidade_venda=have_car)
