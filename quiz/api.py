from flask import Blueprint, jsonify, request

from quiz.models import db, Test, Answer, Question

api = Blueprint('api', __name__)

@api.route('/test/<int:test_id>/')
def get_test(test_id):
    test = Test.query.get(test_id)
    return jsonify(test.to_dict())

@api.route('/assessment/', methods=('POST',))
def create_assessment():
    data = request.get_json()
    assessment = Assessment(
        fname=data['fname'],
        lname=data['lname'],
        email=data['email'])
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
                is_correct=answer['is_correct']
            )
            answers.append(answer)
        q = Question(
                question=q['question'],
                answers=answers)
        questions.append(q)

    test = Test(name=data['name'], questions=questions)
    db.session.add(test)
    db.session.commit()
    return jsonify(test.to_dict()), 201

@api.route('/response/', methods=('POST',))
def create_response():
    data = request.get_json()
    assessment = Assessment.query.get(id=data['assessment'])
    question = Question.query.get(id=data['question'])
    answer = Answer.query.get(id=data['answer'])
    test_response = Response(
        assessment=assessment,
        question=question,
        answer=answer)
    db.session.add(test_response)
    db.session.commit()
    return jsonify(test_response.to_dict()), 201
