from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    questions = db.relationship('Question', backref='test', lazy=False)

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

    def to_dict(self):
        return dict(id=self.id,
                    fname=self.fname,
                    lname=self.lname,
                    email=self.email,
                    responses=[response.to_dict() for response in self.responses]
                    )

class Response(db.Model):
    __tablename__ = 'responses'

    id = db.Column(db.Integer, primary_key=True)
    question = db.relationship('Question')
    answer = db.relationship('Answer')
    
    def to_dict(self):
        return dict(id=self.id,
                    question=self.question.to_dict(),
                    answer=self.answer.to_dict()
                    )

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answers = db.relationship('Answer', backref='question', lazy=False)

    def to_dict(self):
        return dict(
            id=self.id,
            question=self.question,
            answers=[answer.to_dict() for answer in self.answers()]
            )

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
    is_correct = db.Column(db.Boolean)

    def to_dict(self):
        return dict(
            id=self.id,
            answer=self.answer,
            is_correct=self.is_correct
            )
