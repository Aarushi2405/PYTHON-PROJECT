from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length, EqualTo
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
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email.'), Length(max=50)])
	security_question = StringField('(Security question) Who is your favorite cartoon character?', validators=[InputRequired(), Length(max=100)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password')])

class ForgotPasswordForm(FlaskForm):
	username = StringField('username')
	security_question = StringField('(Security question) Who is your favorite cartoon character?')
	new_password = PasswordField('new password', validators=[InputRequired(), Length(min=8, max=80)])
	confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('new_password', message='Field must be equal to new password.')])

class QuizForm(FlaskForm):
	quiz = RadioField(choices=[], validators=[InputRequired()])

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == "POST" and form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		c, conn = connection()
		row = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username),))
		if int(row) == 1 :
			row = c.fetchone()
			if str(password) == row[4] :
				c.close()
				conn.close()
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
		username = form.username.data
		email = form.email.data
		security_question = form.security_question.data
		password = form.password.data
		confirm_password = form.confirm_password.data
		c, conn = connection()
		row = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username)))
		if int(row) > 0:
			flash("username already taken...please choose another...")
			return render_template('signup.html', form=form)
		else :
			c.execute("INSERT INTO users (username, email, security_question, password, confirm_password) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (thwart(username), thwart(email), thwart(security_question), thwart(password), thwart(confirm_password)))
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
			if str(security_question) == row[3] :
				c.execute("UPDATE users SET password = \"%s\", confirm_password = \"%s\" WHERE username = \"%s\"" % (thwart(new_password), thwart(confirm_password), thwart(username)))
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
	return render_template('dashboard.html')

i = 0
correct = 0 
score = 0
x = []

@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():
	global i, correct, score, x
	x.append(time.time())
	c, conn = connection()
	form = QuizForm(request.form)
	row = c.execute("SELECT * FROM quiz1")	
	row = c.fetchall()
	form.quiz.label = row[i][1]
	form.quiz.choices = [(row[i][j], row[i][j]) for j in range(2, 6)]
	answer = form.quiz.data
	if answer == row[i][6] :
		correct+=1
	if request.method == "POST" and form.validate_on_submit():
		if i<2 :
			i+=1
			return redirect(url_for('quiz1'))
		else :
			c.close()
			conn.close()
			score=correct
			i=0
			correct=0
			return redirect(url_for('scorecard'))
	return render_template('quiz1.html', form=form)

@app.route('/scorecard')
def scorecard():
	flash("you scored %s out of 3..." % score)
	flash("you took %s seconds to complete this quiz..." % str(x[2]-x[0]))
	return render_template('scorecard.html')

if __name__=='__main__':
	app.run(debug=True)
