import os
import unittest

from app import apple, db
import flask_migrate
from app.models import User

TEST_DB = 'test'
PATH_TO_DATABASE = os.path.join(os.path.abspath(os.path.curdir), TEST_DB + ".slite")
START_USER_RECORDS = 0

class testUser(unittest.TestCase):

    def setUp(self):
        apple.config['TESTING'] = True
        apple.config['CSRF_ENABLED'] = False
        apple.config['DEBUG'] = False
        apple.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + PATH_TO_DATABASE
        #apple.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/' + TEST_DB
        with apple.app_context():
            flask_migrate.upgrade()

    def tearDown(self):
        os.remove(PATH_TO_DATABASE)

    def test_should_added_new_random_user(self):
        current_users_count = User.query.count()
        self.assertEqual(current_users_count, START_USER_RECORDS)
        random_user = User.add_random_user()
        users_count = User.query.count()
        self.assertEqual(users_count, START_USER_RECORDS + 1)

if __name__ == "__main__":
    unittest.main()