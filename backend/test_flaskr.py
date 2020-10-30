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
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('postgres@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question ={
            'question':'Test case',
            'answer': 'test_answer',
            'difficulty':'2',
            'category':'3'
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
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_get_pagnated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_404_sent_reuest_byond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')

    def test_delete_question(self):
        question = Question(question= self.new_question['question'],answer=self.new_question['answer'],difficulty = self.new_question['difficulty'],category = self.new_question['category'])
        question.insert()
        question_id = question.id

        res = self.client().delete('/questions/{}'.format(question_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],question_id)

    def test_delete_incorrect_questionid(self):
        question = Question(question= self.new_question['question'],answer=self.new_question['answer'],difficulty = self.new_question['difficulty'],category = self.new_question['category'])
        question.insert()
        question_id = int(question.id+1)

        res = self.client().delete('/question/{}'.format(question_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')

    def test_insert_new_question(self):
        questions_before_add = len(Question.query.all())
        res = self.client().post('questions',json=self.new_question)
        data = json.loads(res.data)
        questions_after_add = len(Question.query.all())
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(questions_after_add - questions_before_add==1)

    def test_fail_insert_new_question(self):
        questions_before_add = len(Question.query.all())
        res = self.client().post('questions',json={})
        data = json.loads(res.data)
        questions_after_add = len(Question.query.all())
        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
        self.assertTrue(questions_after_add == questions_before_add)

    def test_search_question(self):
        res = self.client().post('questions',json={'searchTerm':'Test case'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['questions']) >1)

    def test_get_question_by_cat(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['questions']) >1)

    def test_get_error_question_by_cat(self):
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)

    def test_play(self):
        res = self.client().post('/quizzes',json={'previous_questions': [1, 2],
                                            'quiz_category': {'type': 'test', 'id': '1'}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def fail_test_play(self):
        res = self.client().post('/quizzes',json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)








# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()