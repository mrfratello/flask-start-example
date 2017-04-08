# -*- coding: utf-8 -*-

import os
from flask import abort, render_template, redirect, url_for
from app import apple, db
from models import User

@apple.route('/')
def index():
    print apple.root_path
    return "".join([
        "Hello world1<br/>",
        "<a href='/users/add_random'>Добавить случайного пользователя</a>"
    ])

@apple.route('/message/<string:mess_id>')
def message(mess_id):
    avaliable_ids = ['hello', 'xyz', 'my']
    if (mess_id in avaliable_ids):
        return "It is work!"
    else:
        abort(404)

@apple.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@apple.route('/users/add_random')
def add_user():
    User.add_random_user()
    return redirect(url_for('users'))



@apple.errorhandler(404)
def page_not_found(error):
    return "Error 404", 404

