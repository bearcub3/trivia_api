import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.sample_question = {
            'question': 'is this test question?',
            'answer': 'True',
            'difficulty': 1,
            'category': 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    DONE
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_pagination(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_delete_question_with_sucess(self):
        prev_questions = Question.query.all()

        res = self.client().delete('/questions/38')
        data = json.loads(res.data)

        after_questions = Question.query.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(prev_questions) - len(after_questions) == 1)

    def test_question_search_with_results(self):
        res = self.client().post('/questions/search',
                                 json={'searchTerm': 'What'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['questions']), 7)
        self.assertIsNone(data['current_category'])

    def test_question_search_without_results(self):
        res = self.client().post('/questions/search',
                                 json={'searchTerm': 'BTS'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertIsNone(data['current_category'])

    def test_create_new_question(self):
        prev_questions = Question.query.all()

        res = self.client().post('/questions', json=self.sample_question)
        data = json.loads(res.data)

        after_questions = Question.query.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(after_questions) - len(prev_questions) == 1)

    def test_retrieve_question_by_category(self):
        res = self.client().get('/categories/4/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['questions']), 3)
        self.assertEqual(data['total_questions'], 3)
        self.assertTrue(data['current_category'] == 'History')

    def test_404_error_unable_to_retrieve_question(self):
        res = self.client().get('/categories/8/questions')

        self.assertEqual(res.status_code, 404)

    def test_get_random_quiz(self):
        res = self.client().post(
            '/play', json={'previous_questions': [16, 19], 'quiz_category': {'type': 'Art', 'id': 2}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertEqual(data['question']['category'], 2)
        self.assertNotEqual(data['question']['id'], 16)
        self.assertNotEqual(data['question']['id'], 19)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
