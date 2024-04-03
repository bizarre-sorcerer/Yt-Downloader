def create_table(db):
    cursor = db.cursor()
    query = '''create table if not exists user_data(
        id int auto_increment primary key,
        username varchar(255),
        email varchar(255),
        password varchar(255),
        history text(255)
    )'''
    cursor.execute(query)  
    db.commit()

def add_user(db, username, email, password):
    cursor = db.cursor()
    add_data_query = "INSERT INTO user_data (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(add_data_query, (username, email, password))
    db.commit()

def check_user(db, login, password):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user_data WHERE username = %s OR email = %s", (login, login))
    user_data = cursor.fetchone()

    if user_data is None:
        return [
        False,
        "Ошибка при входе: Пользователя с таким логином не существует"
        ]
    elif user_data[3] != password:
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
    cursor.execute("UPDATE user_data SET history = CONCAT(COALESCE(history, ''), ' ' %s) WHERE id = %s", (url, user_id))  
    db.commit()

def change_user_password(db, user_id, new_password):
    cursor = db.cursor()
    cmd = '''update user_data set password = %s where id = %s'''
    cursor.execute(cmd, (new_password, user_id))
    db.commit()

def get_user_id(db, column_name, value):
    cursor = db.cursor()

    if column_name == 'username':
        cursor.execute("SELECT id FROM user_data WHERE username = %s", (value,))
    elif column_name == 'email':
        cursor.execute("SELECT id FROM user_data WHERE email = %s", (value,))
    else:
        print("Invalid login type. Use 'username' or 'email'.")
        return None
        
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
