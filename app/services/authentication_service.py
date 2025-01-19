from db.UsersRepository import *

def createUser(request):
    username = request.form["username"]
    email = request.form["email"]
    password = request.form['password']
    add_user(get_db(), username, email, password)