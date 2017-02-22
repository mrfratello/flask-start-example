import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tmp/app.sqlite')

CSRF_ENABLED = True
SECRET_KEY = 't38i8e+)*1aws7s7vgoq^khw=18u_j-k#6mhaj$b*gbq#(0#mv'