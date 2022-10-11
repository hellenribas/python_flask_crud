from flask import Flask, make_response, jsonify, request
import mysql.connector
from mvc_flask import FlaskMVC


app = Flask(__name__)
FlaskMVC(app)
config = {
        'user': 'carford',
        'password': 'carford123',
        'host': '192.168.112.2',
        'port': '3306',
        'database': 'carford_db'
    }

connection = mysql.connector.connect(**config)


@app.route('/carros', methods=['GET'])
def hello():
    cursor = connection.cursor()
    query = 'SELECT * FROM carros'
    cursor.execute(query)
    carros = cursor.fetchall()
    print('hello')
    print(carros)
    return make_response(
        jsonify(
            mensagem='Lista de carros',
            dados=carros
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
