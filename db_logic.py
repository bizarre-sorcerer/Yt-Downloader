import mysql.connector
from flask import jsonify

def add_user(cursor, username, email, password):
  add_data_query = "INSERT INTO user_data (username, email, password) VALUES (%s, %s, %s)"
  cursor.execute(add_data_query, (username, email, password))

def check_user(cursor, login, password):
  cursor.execute("SELECT * FROM user_data WHERE username = %s", (login,))
  user_data = cursor.fetchone()

  if user_data is None:
    return [
      False,
      "User not found"
    ]

  elif user_data[3] != password:
    return [
      False,
      "Incorrect password"
    ]
      
  return [
    True,
    "Successfully signed in"
  ]

def save_history(cursor, url, user_id):
  cursor.execute("UPDATE user_data SET history = %s WHERE id = %s", (url, user_id))

