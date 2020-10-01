from flask import Flask
import mysql.connector

app = Flask(__name__)

def connect() :
    config = {'user':'root', 'password':'root', 'port':'3306', 'database':'db','host':'mysql'}
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    return db, cursor



def add_timestamp() :
    db, cursor = connect()
    cursor.execute('INSERT INTO time_table (time_stamp) VALUES (CURRENT_TIMESTAMP)')
    db.commit()
     
def get_timestamp() :
    db, cursor = connect()
    cursor.execute('SELECT * FROM time_table')
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


@app.route('/')
def hello_world() :
    add_timestamp()
    return str(get_timestamp())

if __name__ == '__main__' :
    app.run(host='0.0.0.0')