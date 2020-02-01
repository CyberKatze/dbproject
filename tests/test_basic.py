import unittest
from flask import current_app
from app import create_app
from database import connect, get_db


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_db_exists(self):
        db = get_db()
        self.assertFalse(db is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])