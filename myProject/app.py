from flask import Flask, render_template, flash, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, IntegerField
from wtforms.validators import InputRequired, Email, Length, EqualTo, NumberRange
from dbconnect import connection
from MySQLdb import escape_string as thwart
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ShshhhYouCannotTellAnyone'
Bootstrap(app)

class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')

class RegisterForm(FlaskForm):
	name = StringField('name', validators = [InputRequired()])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email.'), Length(max=50)])
	security_question = StringField('(Security question) Who is your favorite cartoon character?', validators=[InputRequired(), Length(max=100)])
	age = IntegerField('age', validators=[InputRequired(), NumberRange(min=7, max=77, message='Age must be between 7 to 77 years.')])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password')])

class ForgotPasswordForm(FlaskForm):
	username = StringField('username')
	security_question = StringField('(Security question) Who is your favorite cartoon character?')
	new_password = PasswordField('new password', validators=[InputRequired(), Length(min=8, max=80)])
	confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('new_password', message='Field must be equal to new password.')])

class QuizForm(FlaskForm):
	quiz = RadioField(choices=[], validators=[InputRequired()])

LALALALALALALALAAL
HELLO

class EditProfileForm(FlaskForm):
	name = StringField('name', validators = InputRequired()], default = 'Janvi Chhabra')
	email = StringField('email', validators = validators=[InputRequired(), Email(message='Invalid email.'), Length(max=50)], default = 'janvi7109@gmail.com')
	security_question = StringField(('(Security question) Who is your favorite cartoon character?', validators=[InputRequired(), Length(max=100)], default = 'Shinchan')
	age = IntegerField('age', validators=[InputRequired(), NumberRange(min=7, max=77, message='Age must be between 7 to 77 years.')])
	password = PasswordField('current password', validators=[InputRequired(), Length(min=8, max=80)])
	new_password = PasswordField('new password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	session.pop('user', None)
	form = LoginForm(request.form)
	if request.method == "POST" and form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		c, conn = connection()
		row = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username),))
		if int(row) == 1 :
			row = c.fetchone()
			if str(password) == row[6] :
				c.close()
				conn.close()
				session['user'] = username
				return redirect(url_for('dashboard'))
			else :
				flash("incorrect password...")
				return render_template('login.html', form=form)
		else :
			flash("invalid username...")
			return render_template('login.html', form=form)
	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm(request.form)
	if request.method == "POST" and form.validate_on_submit():
		name = form.name.data
		username = form.username.data
		email = form.email.data
		security_question = form.security_question.data
		age = form.age.data
		password = form.password.data
		confirm_password = form.confirm_password.data
		c, conn = connection()
		row = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username)))
		if int(row) > 0:
			flash("username already taken...please choose another...")
			return render_template('signup.html', form=form)
		else :
			session['user']=username
			c.execute("INSERT INTO users (name, username, email, security_question, age, password) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", %d, \"%s\")" % (thwart(name), thwart(username), thwart(email), thwart(security_question), age, thwart(password)))
			c.execute("CREATE TABLE %s (quizname VARCHAR(20),score INTEGER(1),timing DECIMAL(7,3))" %session['user'])
			conn.commit()
			c.close()
			conn.close()
			return redirect(url_for('dashboard'))
	return render_template('signup.html', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
	form = ForgotPasswordForm()
	if request.method == "POST" and form.validate_on_submit():
		username = form.username.data
		security_question = form.security_question.data
		new_password = form.new_password.data
		confirm_password = form.confirm_password.data
		c, conn = connection()
		row = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username)))
		if int(row) == 1:
			row = c.fetchone()
			if str(security_question) == row[4] :
				c.execute("UPDATE users SET password = \"%s\" WHERE username = \"%s\"" % (thwart(new_password), thwart(username)))
				conn.commit()
				c.close()
				conn.close()
				return redirect(url_for('login'))
			else :
				flash("invalid answer to security question...")
		else :
			flash("invalid username...")
			return render_template('forgot_password.html', form=form)
	return render_template('forgot_password.html', form=form)

@app.route('/dashboard')
def dashboard():
	if 'user' in session :
		return render_template('dashboard.html')
	return "YOU MUST LOGIN!"


@app.route('/profile')
def profile():
	# c.execute("Select * from users where username = %s" session['username'])
	# x = c.fetchone()
	# return render_template('profile.html',username=("Aarushi","lalala","5"))
	if 'user' in session :
		return render_template('profile.html')
	return "YOU MUST LOGIN!"

@app.route('/edit_profile')
def edit_profile():
	if 'user' in session :
		return render_template('edit_profile.html')
	return "YOU MUST LOGIN!"

@app.route('/leaderboard')
def leaderboard():
	if 'user' in session :
		return render_template('leaderboard.html')
	return "YOU MUST LOGIN!"

@app.route('/quiz1about')
def quiz1about():
	if 'user' in session :
		return render_template('quiz1about.html')
	return "YOU MUST LOGIN!"

@app.route('/quiz2about')
def quiz2about():
	if 'user' in session :
		return render_template('quiz2about.html')
	return "YOU MUST LOGIN!"

@app.route('/quiz3about')
def quiz3about():
	if 'user' in session :
		return render_template('quiz3about.html')
	return "YOU MUST LOGIN!"

@app.route('/quiz4about')
def quiz4about():
	if 'user' in session :
		return render_template('quiz4about.html')
	return "YOU MUST LOGIN!"

i = 0
correct = 0
score = 0
x = []
start = 0
stop = 0
quizname = ''

@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():
	global i, correct, score, x, start, stop, quizname
	x.append(time.time())
	c, conn = connection()
	form = QuizForm(request.form)
	row = c.execute("SELECT * FROM quiz1")
	row = c.fetchall()
	form.quiz.label = row[i][1]
	form.quiz.choices = [(row[i][j], row[i][j]) for j in range(2, 6)]
	answer = form.quiz.data
	if answer == row[i][6] :
		correct += 1
	if request.method == "POST" and form.validate_on_submit():
		if i < 4 :
			i += 1
			return redirect(url_for('quiz1'))
		else :

			score = correct
			start = x[0]
			stop = time.time()
			quizname = 'Doraemon'
			i = 0
			correct = 0
			c.execute("Insert into %s values(%s,%d,%.3f)" %(session['user'],thwart(quizname),score,stop-start))
			conn.commit()
			x = []
			c.close()
			conn.close()
			return redirect(url_for('scorecard'))
	if 'user' in session :
		return render_template('quiz1.html', form=form)
	return "YOU MUST LOGIN!"

@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
	global i, correct, score, x, start, stop
	x.append(time.time())
	c, conn = connection()
	form = QuizForm(request.form)
	row = c.execute("SELECT * FROM quiz2")
	row = c.fetchall()
	form.quiz.label = row[i][1]
	form.quiz.choices = [(row[i][j], row[i][j]) for j in range(2, 6)]
	answer = form.quiz.data
	if answer == row[i][6] :
		correct += 1
	if request.method == "POST" and form.validate_on_submit():
		if i < 4 :
			i += 1
			return redirect(url_for('quiz2'))
		else :
			c.close()
			conn.close()
			score = correct
			start = x[0]
			stop = time.time()
			i = 0
			correct = 0
			x = []
			return redirect(url_for('scorecard'))
	if 'user' in session :
		return render_template('quiz2.html', form=form)
	return "YOU MUST LOGIN!"

@app.route('/quiz3', methods=['GET', 'POST'])
def quiz3():
	global i, correct, score, x, start, stop
	x.append(time.time())
	c, conn = connection()
	form = QuizForm(request.form)
	row = c.execute("SELECT * FROM quiz3")
	row = c.fetchall()
	form.quiz.label = row[i][1]
	form.quiz.choices = [(row[i][j], row[i][j]) for j in range(2, 6)]
	answer = form.quiz.data
	if answer == row[i][6] :
		correct += 1
	if request.method == "POST" and form.validate_on_submit():
		if i < 4 :
			i += 1
			return redirect(url_for('quiz3'))
		else :
			c.close()
			conn.close()
			score = correct
			start = x[0]
			stop = time.time()
			i = 0
			correct = 0
			x = []
			return redirect(url_for('scorecard'))
	if 'user' in session :
		return render_template('quiz3.html', form=form)
	return "YOU MUST LOGIN!"

@app.route('/quiz4', methods=['GET', 'POST'])
def quiz4():
	global i, correct, score, x, start, stop
	x.append(time.time())
	c, conn = connection()
	form = QuizForm(request.form)
	row = c.execute("SELECT * FROM quiz4")
	row = c.fetchall()
	form.quiz.label = row[i][1]
	form.quiz.choices = [(row[i][j], row[i][j]) for j in range(2, 6)]
	answer = form.quiz.data
	if answer == row[i][6] :
		correct += 1
	if request.method == "POST" and form.validate_on_submit():
		if i < 4 :
			i += 1
			return redirect(url_for('quiz4'))
		else :
			c.close()
			conn.close()
			score = correct
			start = x[0]
			stop = time.time()
			i = 0
			correct = 0
			x = []
			return redirect(url_for('scorecard'))
	if 'user' in session :
		return render_template('quiz4.html', form=form)
	return "YOU MUST LOGIN!"

@app.route('/scorecard')
def scorecard():
	flash("you scored %s out of 5..." % score)
	flash("you took %s seconds to complete this quiz..." % str(stop - start))
	c, conn = connection()
	row = c.execute("SELECT * FROM scoreboard WHERE username = \"%s\" AND quizname = \"%s\"" % (thwart(session.get('user')), thwart(quizname)))
	if int(row) > 0:
		c.execute("UPDATE scoreboard SET score = %d, timing = %.3f WHERE username = \"%s\" AND quizname = \"%s\"" % (score, (stop - start), thwart(session.get('user')), thwart(quizname)))
	else :
		c.execute("INSERT INTO scoreboard (username, quizname, score, timing) VALUES (\"%s\", \"%s\", %d, %.3f)" % (thwart(session.get('user')), thwart(quizname), score, (stop - start)))
	conn.commit()
	c.close()
	conn.close()
	if 'user' in session :
		return render_template('scorecard.html')
	return

if __name__=='__main__':
	app.run(debug=True)
