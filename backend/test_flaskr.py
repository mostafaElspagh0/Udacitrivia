import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import Question, Category
from config import DatabaseUri


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        self.app = create_app()
        self.database_uri = DatabaseUri()
        self.database_uri.name = "trivia_test"
        self.app.config['SQLALCHEMY_DATABASE_URI'] = str(self.database_uri)
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['current_category'], None)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    def test_questions_return_404_when_cant_find_question(self):
        res = self.client().get('/questions?page=100')
        self.assertEqual(res.status_code, 404)

    def test_get_categories(self):
        default_res = (b'{"categories":{"1":"Science","2":"Art","3":"Geography","4":"History",'
                       b'"5":"Entertainment","6":"Sports"}}\n')

        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, default_res)

    def test_get_categories_questions_return_404(self):
        res = self.client().get('/categories/30/questions')
        self.assertEqual(res.status_code, 404)

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
