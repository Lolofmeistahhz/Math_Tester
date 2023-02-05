from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length


class Test_form(FlaskForm):
    answer1 = StringField('answer1',validators=[DataRequired()])
    answer2 = StringField('answer2',validators=[DataRequired()])
    answer3 = StringField('answer3',validators=[DataRequired()])
    answer4 = StringField('answer4',validators=[DataRequired()])
    answer5 = StringField('answer5',validators=[DataRequired(),Length(max=20)])
    answer6 = StringField('answer6',validators=[DataRequired()])
    answer7 = StringField('answer7',validators=[DataRequired()])
    button = SubmitField('Завершить тестирование',validators=[DataRequired()],id="test_but")

    def __init__(self, *args, **kwargs):
        super(Test_form, self).__init__(*args, **kwargs)


class LoginForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Вход')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, *kwargs)

class regForm(FlaskForm):
    surname = StringField('surname', validators=[DataRequired(),Length(max=50)])
    name = StringField('name', validators=[DataRequired(),Length(max=50)])
    patronomyc = StringField('patronomyc', validators=[DataRequired(),Length(max=50)])
    school = StringField('school', validators=[DataRequired(),Length(max=120)])
    s_class = StringField('s_class', validators=[DataRequired(),Length(max=10)])
    s_teacher = StringField('s_teacher',validators=[DataRequired(),Length(max=60)])
    login = StringField('login', validators=[DataRequired(),Length(min=6,max=20)])
    password = PasswordField('password', validators=[DataRequired(),Length(min=6,max=20)])
    submit = SubmitField('Регистрация', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(regForm, self).__init__(*args, **kwargs)