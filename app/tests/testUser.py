import os
import unittest

from app import apple, db
import flask_migrate

TEST_DB = 'test'
PATH_TO_DATABASE = os.path.join(os.path.abspath(os.path.curdir), TEST_DB + ".slite")

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

    def test_should_true(self):
        self.assertEqual(0, 0)


if __name__ == "__main__":
    unittest.main()