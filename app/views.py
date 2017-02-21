import os
from flask import abort, g
from app import apple

@apple.route('/')
def index():
    print apple.root_path
    return "Hello world1"

@apple.route('/message/<string:mess_id>')
def message(mess_id):
    avaliable_ids = ['hello', 'xyz', 'my']
    if (mess_id in avaliable_ids):
        return "It is work!"
    else:
        abort(404)


@apple.errorhandler(404)
def page_not_found(error):
    return "Error 404", 404


