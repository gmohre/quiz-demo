import json
from flask import Blueprint, jsonify, request
from hashlib import md5

from quiz.models import db, Test, Assessment, Question, Answer, Response

api = Blueprint('api', __name__)

@api.route('/test/<int:test_id>/', methods=('GET',))
def get_test(test_id):
    test = Test.query.get(test_id)
    return jsonify(test.to_dict())

@api.route('/assessment/<string:user_hash>/', methods=('POST',))
def continue_assessment(user_hash):
    return Assessment.query.get(user_hash=user_hash)

@api.route('/assessment/', methods=('POST',))
def create_assessment():
    data = request.get_json()
    user_hash = md5()
    user_hash.update(json.dumps(data).encode())
    assessment = Assessment(
        fname=data['fname'],
        lname=data['lname'],
        email=data['email'],
        test_id=data['test_id'],
        user_hash=user_hash.hexdigest())
    db.session.add(assessment)
    db.session.commit()
    return jsonify(assessment.to_dict()), 201

@api.route('/test/', methods=('POST',))
def create_test():
    data = request.get_json()
    questions = []

    for q in data['questions']:
        answers = []
        for answer in q['answers']:
            answer = Answer(
                answer=answer['answer'],
                is_correct=answer.get('is_correct'))
            answers.append(answer)

        q = Question(
            question=q['question'],
            answers=answers)
        questions.append(q)

    duration = data['duration']

    test = Test(name=data['name'], questions=questions, duration=duration)
    db.session.add(test)
    db.session.commit()
    return jsonify(test.to_dict()), 201

@api.route('/response/', methods=('POST',))
def create_response():
    data = request.get_json()
    assessment = Assessment.query.get(data['assessment'])
    question = Question.query.get(data['question'])
    answer = Answer.query.get(data['answer'])
    test_response = Response(
        assessment=assessment,
        question=question,
        answer=answer)
    db.session.add(test_response)
    db.session.commit()
    return jsonify(test_response.to_dict()), 201

