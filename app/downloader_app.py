import os
import mysql.connector
from flask import Flask, g
from routes.main_routes import main_routes 

isProduction = True

app = Flask(__name__)
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

app.register_blueprint(main_routes)  

def get_db():
    # Бд для продакшена
    if 'db' not in g:
        if isProduction: 
            g.db = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST', 'mysql'),
                user=os.getenv('MYSQL_USER', 'bizarre-sorcerer'),
                password=os.getenv('MYSQL_PASSWORD', 'deftones'),
                database=os.getenv('MYSQL_DATABASE', 'ytdownloader_db')
            )            
        # Локальная бд для разработки
        else:
            g.db = mysql.connector.connect(
                host="localhost",
                user="bizarre-sorcerer",
                password="deftones",
                database="yt_downloader_db"
            )
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':        
    app.run(host='0.0.0.0', port='5000', debug=True)

