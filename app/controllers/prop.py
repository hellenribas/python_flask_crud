from app import app
from models.model import Proprietarios
from flask import render_template

@app.route('/proprietarios', methods=['GET'])
def getProp():
    proprietarios=Proprietarios.query.all()
    render_template('index.html', list=proprietarios)
    return 'ola, mundo'

