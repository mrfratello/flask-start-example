import os
import unittest

from app import apple, db
from flask_migrate import upgrade, downgrade

TEST_DB = 'test'

class testUser(unittest.TestCase):

    def setUp(self):
        apple.config['TESTING'] = True
        apple.config['CSRF_ENABLED'] = False
        apple.config['DEBUG'] = False
        # basedir = os.path.abspath(os.path.curdir)
        # apple.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        apple.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/' + TEST_DB
        with apple.app_context():
            upgrade()

    def tearDown(self):
        with apple.app_context():
            downgrade(revision='base')
        # db.drop_all()

    def test_should_true(self):
        self.assertEqual(0, 0)


if __name__ == "__main__":
    unittest.main()