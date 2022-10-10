from flask import Flask
from redis import Redis
import mysql.connector


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

config = {
        'user': 'cardford',
        'password': 'cardford123',
        'host': 'db',
        'port': '3306',
        'database': 'carford_db'
    }
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# comando = 'INSERT INTO proprietarios (nome, oportunidade_venda) VALUES ("teste", true)'

cursor.close()
connection.close()


@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
