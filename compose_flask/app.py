from flask import Flask
from redis import Redis
import mysql.connector


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

config = {
        'user': 'carford',
        'password': 'carford123',
        'host': 'db',
        'port': '3306',
        'database': 'carford_db'
    }
connection = mysql.connector.connect(**config)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)