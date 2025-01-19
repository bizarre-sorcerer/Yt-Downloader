from flask import session

def add_userData_toSession(request):  
    username = request.form["username"]
    email = request.form["email"]
    password = request.form['password']

    session['logged_in'] = True
    session['username'] = username
    session['email'] = email
    session['password'] = password
