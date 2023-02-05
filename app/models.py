from flask_login import UserMixin, login_manager

from app import db, app


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(500), nullable=False)
    Question1 = db.Column(db.String(500), nullable=False)
    Answer1 = db.Column(db.String(20), nullable=False)
    Question2 = db.Column(db.String(500), nullable=False)
    Answer2 = db.Column(db.String(20), nullable=False)
    Question3 = db.Column(db.String(500), nullable=False)
    Answer3 = db.Column(db.String(20), nullable=False)
    Question4 = db.Column(db.String(500), nullable=False)
    Answer4 = db.Column(db.String(20), nullable=False)
    Question5 = db.Column(db.String(500), nullable=False)
    Answer5 = db.Column(db.String(20), nullable=False)
    Question6 = db.Column(db.String(500), nullable=False)
    Answer6 = db.Column(db.String(20), nullable=False)
    Question7 = db.Column(db.String(500), nullable=False)
    Answer7 = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Test {}>'.format(self.id)


class Test_result(db.Model):
    __tablename__ = 'test_result'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    grade = db.Column(db.Integer)
    date_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<Test_result {}>'.format(self.id)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    patronomyc = db.Column(db.String(50), nullable=True)
    school = db.Column(db.String(120), nullable=False)
    s_class = db.Column(db.String(10), nullable=False)
    s_teacher = db.Column(db.String(60), nullable=False)
    login = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    usertype = db.Column(db.String(20),nullable= False)

    def __repr__(self):
        return '<User {}>'.format(self.id)

    # class Test10C(db.Model):
    #     id = db.Column(db.Integer,primary_key=True)
    #     Answer1 = db.Column(db.Text)
    #     Answer2 = db.Column(db.Text)
    #     Answer3 = db.Column(db.Text)
    #     Answer4 = db.Column(db.Text)
    #     Answer5 = db.Column(db.Text)
    #     Answer6 = db.Column(db.Text)
    #     Answer7 = db.Column(db.Text)
    #     max_grade = db.Column(db.Integer)
    #
    #     def __repr__(self):
    #         return '<Test10C {}>'.format(self.id)
    #
    # class Test11C(db.Model):
    #     id = db.Column(db.Integer,primary_key=True)
    #     Answer1 = db.Column(db.Text)
    #     Answer2 = db.Column(db.Text)
    #     Answer3 = db.Column(db.Text)
    #     Answer4 = db.Column(db.Text)
    #     Answer5 = db.Column(db.Text)
    #     Answer6 = db.Column(db.Text)
    #     Answer7 = db.Column(db.Text)
    #     max_grade = db.Column(db.Integer)

    def __repr__(self):
        return '<Test11C {}>'.format(self.id)


with app.app_context():
    db.create_all()

