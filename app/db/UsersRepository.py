def add_user(db, username, email, password):
    cursor = db.cursor()
    add_data_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(add_data_query, (username, email, password))
    db.commit()

def check_user(db, login, password):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (login, login))
    users = cursor.fetchone()
    cursor.fetchall()
    cursor.close()

    if users is None:
        return [
        False,
        "Ошибка при входе: Пользователя с таким логином не существует"
        ]
    elif users[3] != password:
        return [
        False,
        "Ошибка при входе: Неправильный пароль"
        ]
        
    return [
        True,
        "Вход успешен"
    ]

def save_to_history(db, url, user_id):  
    cursor = db.cursor()
    cursor.execute("UPDATE users SET history = CONCAT(COALESCE(history, ''), ' ' %s) WHERE id = %s", (url, user_id))  
    db.commit()

def change_user_password(db, user_id, new_password):
    cursor = db.cursor()
    cmd = '''update users set password = %s where id = %s'''
    cursor.execute(cmd, (new_password, user_id))
    db.commit()

def get_user_id(db, column_name, value):
    cursor = db.cursor()

    if column_name == 'username':
        cursor.execute("SELECT id FROM users WHERE username = %s", (value,))
    elif column_name == 'email':
        cursor.execute("SELECT id FROM users WHERE email = %s", (value,))
    else:
        print("Invalid login type. Use 'username' or 'email'.")
        return None
        
    user = cursor.fetchone()
    cursor.fetchall()
    cursor.close()
    return user[0] if user else None
    
def get_user_data(db, user_id):
    cursor = db.cursor(buffered=True)
    cursor.execute("select * from users where id = %s", (user_id, ))
    user = cursor.fetchone()
    cursor.fetchall()
    cursor.close()
    return user

def store_token(db, email, token):
    cursor = db.cursor()
    cursor.execute("update users set reset_token = %s where email = %s", (token, email))
    db.commit()

def delete_users(db):
    cursor = db.cursor()
    cursor.execute("truncate table users")

def get_all_users(db):
    cursor = db.cursor()
    cursor.execute("select * from users")
    users = cursor.fetchall()
    cursor.close()
    return users
