from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

test_questions = db.Table('test_questions',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id'), primary_key=True),
    db.Column('test_id', db.Integer, db.ForeignKey('tests.id'), primary_key=True)
)
class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    questions = db.relationship('Question', secondary=test_questions, lazy=False,
        backref=db.backref('tests', lazy=True))
    assessments = db.relationship('Assessment', backref='test', lazy=True)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    questions=[question.to_dict() for question in self.questions]
                    )


class Assessment(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    email = db.Column(db.Text)
    responses = db.relationship('Response', backref='assessment', lazy=False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
#    start_time

    def to_dict(self):
        return dict(id=self.id,
                    fname=self.fname,
                    lname=self.lname,
                    email=self.email,
                    responses=[response.to_dict() for response in self.responses],
                    test=self.test
                    )


class Response(db.Model):
    __tablename__ = 'responses'

    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'), nullable=False)
    
    def to_dict(self):
        return dict(id=self.id,
                    question=self.question.question,
                    answer=self.answer.to_dict())


class Question(db.Model):
    __tablename__ = 'questions'

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
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
    is_correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    responses = db.relationship('Response', backref='answer', lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            answer=self.answer,
            is_correct=self.is_correct
            )
    
    def __repr__(self):
        return "<Answer - {0}({1})>".format(self.answer, self.is_correct)
