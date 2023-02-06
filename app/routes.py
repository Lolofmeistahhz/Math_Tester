import hashlib
from datetime import datetime

from flask import render_template, request, redirect, url_for, g, flash, session
from flask_login import LoginManager, login_user, current_user, logout_user
from sqlalchemy.orm import aliased

from app import app, db
from app.forms import Test_form, LoginForm, regForm
from app.models import Test, User, Test_result

Login_Manager = LoginManager(app)


@Login_Manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login',methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and user.is_authenticated:
            if user.usertype=="Администратор":
                login_user(user)
                return redirect(url_for('test_result'))
            else:
                login_user(user)
                return redirect(url_for('test_9c'))
    return render_template("login.html",FlaskForm=form,title="Авторизация")

@app.route('/register',methods=["GET", "POST"])
def register():
    form = regForm(request.form,crsf=True)
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if not user:
            u = User(surname=form.surname.data, name=form.name.data, patronomyc=form.patronomyc.data, school=form.school.data, s_class=form.s_class.data,s_teacher = form.s_teacher.data,
                     login=form.login.data, password=form.password.data,usertype="Пользователь")
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('login'))
        elif user:
            flash("Данный логин уже занят!")
            return redirect(url_for('register'))
    return render_template("register.html",FlaskForm=form,title="Регистрация")

@app.route('/test9c', methods=["GET", "POST"])
def test_9c():
    test_form = Test_form(request.form, crsf=True)
    answer = Test.query.filter_by(id=1).first()
    grade = 0
    if current_user.is_authenticated:
        testdata = db.session.query(Test_result.grade, Test.Name, Test_result.date_time).filter(
            Test_result.user == current_user.id).first()
        if not testdata:
            if test_form.validate_on_submit():
                if test_form.answer1.data == answer.Answer1:
                    grade += 1
                if test_form.answer2.data == answer.Answer2:
                    grade += 1
                if test_form.answer3.data == answer.Answer3:
                    grade += 1
                if test_form.answer4.data == answer.Answer4:
                    grade += 1
                if test_form.answer5.data == answer.Answer5:
                    grade += 1
                if test_form.answer6.data == answer.Answer6:
                    grade += 1
                if test_form.answer7.data == answer.Answer7:
                    grade += 1
                time = datetime.now()
                res = Test_result(test=1,user=current_user.id,grade=grade,date_time=time)
                db.session.add(res)
                db.session.commit()
                id = current_user.id
                hash_id = hashlib.md5(str(id).encode())
                return redirect(url_for('profile',id=hash_id,title="Личный кабинет"))
        elif testdata:
                id = current_user.id
                hash_id = hashlib.md5(str(id).encode())
                res = str(hash_id).encode()
                return redirect(url_for('profile', id=res,title="Личный кабинет"))
    else:
        return redirect(url_for('login'))
    return render_template("test9c.html",FlaskForm=test_form,answer=answer,title="Тестирование")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile/<string:id>')
def profile(id):
    user = User.query.filter_by(id=current_user.id).first()
    testdata = db.session.query(Test_result.grade,Test.Name,Test_result.date_time).filter(Test_result.user == current_user.id).order_by(Test_result.date_time.desc()).limit(1)
    return render_template('profile.html',user=user,testdata=testdata,title="Личный кабинет")

@app.route('/admin/test_result')
def test_result():
    user = User.query.filter_by(id=current_user.id).first()
    page = request.args.get('page', 1, type=int)
    pagination = db.session.query(Test_result.user, Test_result.grade, Test_result.date_time, User.name, User.surname,
                                  User.patronomyc, User.school, User.s_class, User.s_teacher).filter(
        Test_result.user == User.id).filter(Test_result.test == Test.id).order_by(Test_result.user.desc()).paginate(
        page=page, per_page=5)
    if user.usertype == "Администратор":
        return render_template('test_result.html',pagination=pagination,title="Просмотр результатов")
    elif user.usertype == "Пользователь":
        return redirect(url_for('test_9c'))

# @app.route('/add/admin/u')
# def adda():
#     u = User(surname='Камозина',name='Олеся',patronomyc='Владимировна',school='secret',s_class='secret',s_teacher='secret',login='admin_bgitu_mathtest',password='bgitu_tester',usertype="Администратор")
#     db.session.add(u)
#     db.session.commit()
#
#
# @app.route('/add/test/9c')
# def add9c():
#     data = Test(Name='Тестирование по математике 9 класс',Question1='График функции y=f(x) симметричен относительно прямой x = 5 и уравнение f(x) = 0 имеет девять различных действительных корней. Чему равна сумма всех этих корней?',Answer1=45,
#                    Question2='Известно, что a > 1, b > 1. Какая из следующих дробей является наибольшей? (В ответе укажите номер варианта ответа без скобки)',Answer2=3,
#                    Question3='Карина ехала от дома до парка сначала на маршрутном такси, затем на метро. Причём время движения на маршрутном такси равно времени движения на метро (временем перехода от маршрутного такси до метро пренебрегаем). В случае движения от дома до парка только на маршрутном такси, время движения оказалось бы в 1,5 раза больше затраченного Кариной. Во сколько раз время движения от дома до парка на метро оказалось бы больше времени движения на маршрутном такси?',Answer3=2,
#                    Question4='Среднее арифметическое двух положительных чисел на 75% больше меньшего из этих чисел. На сколько процентов оно меньше большего из этих чисел?',Answer4=30,
#                    Question5='Из тройки неповторяющихся цифр составили все возможные различные трёхзначные числа. Сумма этих чисел составила 4884. Определить взятые цифры. (В ответе укажите цифры в порядке возрастания без пробелов и запятых, например "279 и 337")',Answer5='679 и 589',
#                    Question6='Дан треугольник ABC. Из вершины B проведена биссектриса BD. BD=8√7, AB=21, DC=8. Определить периметр треугольника ABC.',Answer6=60,
#                    Question7='Пусть a и b – корни квадратного уравнения x² + x - 9 = 0 . Чему равно значение выражения 3a²+4b²+3a+4b+5 ?',Answer7=68)
#     db.session.add(data)
#     db.session.commit()