from flask import Flask, session
from models import User

def is_login():
    return 'login' in session

def try_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        session['login'] = username
        return True
    return False

def try_logout():
    session.pop('login', None)
    return True