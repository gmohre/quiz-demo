import json
import unittest
from flask import Flask
from flask_testing import TestCase

from quiz import create_app, models
EGG_ASSESSMENT = {
    'fname': 'jon',
    'lname': 'ham',
    'email': 'jon@breakfast.ham',
}
EGG_TEST = {
    'name': "Eggs Test",
    'questions': [{
        'question':'How many eggs in a dozen?',
        'answers': [
            {'answer':'3', 'is_correct': False},
            {'answer':'4', 'is_correct': False},
            {'answer':'5', 'is_correct': False},
            {'answer':'12', 'is_correct': True}
        ],
    }],
    'duration': 60*60
}
class QuizTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app = create_app(
            test_config={
                'TESTING':True,
                'SQLALCHEMY_DATABASE_URI':'sqlite:///quiz-test.db',
                'SQLALCHEMY_TRACK_MODIFICATIONS': False})
        return app

    def _create_test(self, test_data):
        return self.client.post("/api/test/", json=test_data)

    def _create_assessment(self, assessment_data, test):
        assessment_data.update({'test_id':test['id']})
        return self.client.post("/api/assessment/", json=assessment_data)

    def _create_response(self, assessment, question, answer):
        response_data = {'assessment': assessment['id'], 'question': question['id'], 'answer': answer['id']}
        return self.client.post("/api/response/", json=response_data)

    def test_create_test(self):
        response = self._create_test(EGG_TEST)
        assert response.status_code == 201

    def test_create_assessment(self):
        test = self._create_test(EGG_TEST).json
        res = self._create_assessment(EGG_ASSESSMENT, test)
        assert res.status_code == 201

    def test_respond_to_assessment(self):
        test = self._create_test(EGG_TEST).json
        res = self._create_assessment(EGG_ASSESSMENT, test)
        assessment = res.json
        for question in test['questions']:
            response = self._create_response(assessment, question, question['answers'][0])
            assert response.status_code == 201

    def setUp(self):
        models.db.create_all()

    def tearDown(self):

        models.db.session.remove()
        models.db.drop_all()

if __name__ == '__main__':
    unittest.main()
