import mysql.connector

def connect_to_db():
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ytdownloader_data"
  )
  return db

def add_user(username, password):
  db = connect_to_db()
  cursor = db.cursor()

  add_data_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
  cursor.execute(add_data_query, (username, password))

  db.commit()
  db.close()
