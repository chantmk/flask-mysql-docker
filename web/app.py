from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = '3306'
mysql = MySQL(app)
@app.route('/')
def hello_world() :
    return 0

if __name__ == '__main__' :
    app.run(debug=True)