from flask import render_template, request, session, redirect, url_for, g
from app.downloader_app import app
from app.services.authentication_service import *  
from app.utils.session_utils import *


@app.route('/sign-up', methods=['POST', 'GET'])
def registration():
  if request.method == "GET":
    return render_template("sign-up.html")
  
  elif request.method == "POST":
    createUser(request)
    add_userData_toSession(request)

    return redirect(url_for("main_page"))


@app.route('/sign-in', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("sign-in.html")
  
    elif request.method == "POST":
        # Может быть либо именем либо почтой
        username = request.form["login"]  
        password = request.form['password']     
        is_valid_user = check_user(get_db(), username, password)

    if is_valid_user[0]:       
        add_userData_toSession(username)
        return redirect(url_for("main_page"))
    else: 
        return render_template(
           'sign-in.html',
            login_error = is_valid_user[1]      
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


@app.route('/log-out')
def logout():
    session.clear()
    return redirect(url_for('main_page'))


@app.route('/change_password', methods={"POST", "GET"})
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    elif request.method == "POST":
        email = request.form['email']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            user_id = get_user_id(get_db(), column_name='email', value=email)
            change_user_password(get_db(), user_id, new_password)

            return redirect(url_for('main_page'))
        return render_template('change_password.html')