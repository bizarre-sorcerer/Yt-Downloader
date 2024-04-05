from flask import Flask, render_template, request, session, redirect, url_for
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from scripts.extractor import extractVideoData
from scripts.filter_formats import filterFormats
from scripts.start_mysql import start_mysql
from scripts.send_email import *
from data_base.db_logic import *
import mysql.connector
import multiprocessing

app = Flask(__name__)
app.secret_key = 'eaa2cc52a16507cf194e4f0c'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/download', methods=["POST"])
def download():
  videoUrl = request.form["video_url"]
  
  videoData = extractVideoData(videoUrl)
  title = videoData["title"]
  formats = filterFormats(videoData["formats"])
  thumbnail = videoData["thumbnail"]

  if "logged_in" in session:
    user_id = session["user_id"]
    session['history'] += videoUrl
    save_to_history(db, videoUrl, user_id)

  return render_template(
    'download.html',
    title=title,
    formats=formats,
    thumbnail=thumbnail
  )

@app.route('/profile', methods=["POST", "GET"])
def get_profile_info(): 
    password = hide_password(session['password']) 
    history = session['history'].split()

    return render_template(
        'profile.html',
        username = session['username'],
        email = session['email'],
        password = password,
        history = history
    )

@app.route('/recovery', methods=['POST', 'GET'])
def password_recovery():
    if request.method == "GET":
        return render_template('password_recovery.html')
    elif request.method == "POST":
        email = request.form["email"] 
        session['email'] = email

        token = generate_token(email)
        store_token(db, email, token)
        send_email(email, token)
        
        return redirect(url_for('login'))
    
@app.route('/change_password', methods={"POST", "GET"})
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    elif request.method == "POST":
        email = request.form['email']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            user_id = get_user_id(db, column_name='email', value=email)
            change_user_password(db, user_id, new_password)

            return redirect(url_for('main_page'))
        return render_template('change_password.html')

@app.route('/sign-up', methods=['POST', 'GET'])
def registration():
  if request.method == "GET":
    return render_template("sign-up.html")
  
  elif request.method == "POST":
    username = request.form["username"]
    email = request.form["email"]
    password = request.form['password']
    add_user(db, username, email, password)

    add_userData_toSession(username)

    return redirect(url_for("main_page"))

@app.route('/sign-in', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("sign-in.html")
  
    elif request.method == "POST":
        # Может быть либо именем либо почтой
        username = request.form["login"]  
        password = request.form['password']     
        is_valid_user = check_user(db, username, password)

    if is_valid_user[0]:       
        add_userData_toSession(username)
        return redirect(url_for("main_page"))
    else: 
        return render_template(
           'sign-in.html',
            login_error = is_valid_user[1]      
        )
        
@app.route('/log-out')
def logout():
    session.clear()
    return redirect(url_for('main_page'))

def add_userData_toSession(login):
    if '@' not in login:
        session['user_id'] = get_user_id(db, column_name='username', value=login)
    else: 
        session['user_id'] = get_user_id(db, column_name='email', value=login)
    
    user_data = get_user_data(db, session['user_id'])
    print(session['user_id'])

    session['logged_in'] = True
    session['username'] = user_data[1]
    session['email'] = user_data[2]
    session['password'] = user_data[3]
    
    if not user_data[4]:
        session['history'] = ''
    else:
        session['history'] = user_data[4]

def hide_password(password):
  result = ""

  for i in range(len(password)):
    result += "*"

  return result

if __name__ == '__main__':
    p = multiprocessing.Process(target=start_mysql)
    p.start()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ytdownloader_data"
    )
    
    app.run(host='0.0.0.0', port='5000', debug=True)

