import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

test_questions = db.Table('test_questions',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('test_id', db.Integer, db.ForeignKey('test.id'), primary_key=True)
)
class Test(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    questions = db.relationship('Question', secondary=test_questions, lazy=False,
        backref=db.backref('tests', lazy=True))
    assessments = db.relationship('Assessment', backref='test', lazy=True)
    duration = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            duration=self.duration,
            name=self.name,
            questions=[question.to_dict() for question in self.questions])


class Assessment(db.Model):
    """
    An instance of a user taking a test
    """
    __tablename__ = 'assessment'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    email = db.Column(db.Text)
    responses = db.relationship('Response', backref='assessment', lazy=False)
    start_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    user_hash = db.Column(db.Text)

    def to_dict(self):
        return dict(id=self.id,
            fname=self.fname,
            lname=self.lname,
            email=self.email,
            responses=[response.to_dict() for response in self.responses],
            test=self.test.to_dict())


class Response(db.Model):
    __tablename__ = 'responses'

    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)

    def to_dict(self):
        return dict(id=self.id,
                    question=self.question.question,
                    answer=self.answer.to_dict())


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answers = db.relationship('Answer', backref='question', lazy=True)
    responses = db.relationship('Response', backref='question',lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            question=self.question,
            answers=[answer.to_dict() for answer in self.answers]
            )

    def __repr__(self):
        return "<Question - {}>".format(self.question)


class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
    is_correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    responses = db.relationship('Response', backref='answer', lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            answer=self.answer,
            is_correct=self.is_correct
            )

    def __repr__(self):
        return "<Answer - {0}({1})>".format(self.answer, self.is_correct)
