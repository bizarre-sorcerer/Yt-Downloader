import mysql.connector

def connect_to_db():
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ytdownloader_data"
  )
  return db

def add_user(username, email, password):
  db = connect_to_db()
  cursor = db.cursor()

  add_data_query = "INSERT INTO user_data (username, email, password) VALUES (%s, %s, %s)"
  cursor.execute(add_data_query, (username, email, password))

  db.commit()
  db.close()

def check_user(login, password):
  return True