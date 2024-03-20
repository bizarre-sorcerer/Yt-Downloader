def add_user(db, username, email, password):
  cursor = db.cursor()
  add_data_query = "INSERT INTO user_data (username, email, password) VALUES (%s, %s, %s)"
  cursor.execute(add_data_query, (username, email, password))
  db.commit()

def check_user(db, login, password):
  cursor = db.cursor()
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

def save_to_history(db, url, user_id):
  cursor = db.cursor()
  cursor.execute("UPDATE user_data SET history = CONCAT(history, ', ', %s) WHERE id = %s", (url, user_id))  
  db.commit()

def get_user_id(db, username):
  cursor = db.cursor()
  cursor.execute("SELECT id FROM user_data WHERE username = %s", (username, ))
  user = cursor.fetchone()
  return user[0] if user else None
  
def get_user_data(db, user_id):
  cursor = db.cursor()
  cursor.execute("select * from user_data where id = %s", (user_id, ))
  user_data = cursor.fetchone()
  return user_data

def delete_user_data(db):
  cursor = db.cursor()
  cursor.execute("truncate table user_data")
