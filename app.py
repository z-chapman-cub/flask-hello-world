import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
  
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab10db_60s2_user:NyfDB7KMgh2UYpg6bU4Udx668ao7ZeaZ@dpg-d49mmv9e2q1c73dn6j40-a/lab10db_60s2")
    conn.close()
    return "Database Connection Successful"