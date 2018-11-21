from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo
from dbconnect import connection
from MySQLdb import escape_string as thwart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ShshhhYouCannotTellAnyone'
Bootstrap(app)

class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password')])

class ForgotPasswordForm(FlaskForm):
		username = StringField('username')
		password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
		confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password')])


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == "POST" and form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		c, conn = connection()
		x = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username),))
		if int(x) == 1 :
			x = c.fetchone()
			if str(password) == x[2] :
				c.close()
				conn.close()
				return render_template('dashboard.html')
			else :
				flash("incorrect password...")
				return render_template('login.html', form=form)
		else :
			flash("inavalid username...")
			return render_template('login.html', form=form)
	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm(request.form)
	if request.method== "POST" and form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		password = form.password.data
		confirm_password = form.confirm_password.data
		c, conn = connection()
		x = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username)))
		if int(x) > 0:
			flash("username already taken...please choose another...")
			return render_template('signup.html', form=form)
		else :
			c.execute("INSERT INTO users (username, email, password, confirm_password) VALUES (\"%s\",\" %s\", \"%s\", \"%s\")" % (thwart(username), thwart(email), thwart(password), thwart(confirm_password)))
		conn.commit()
		c.close()
		conn.close()
		return render_template('dashboard.html')
	return render_template('signup.html', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
	form = ForgotPasswordForm()
	if request.method== "POST" and form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		confirm_password = form.confirm_password.data
		c, conn = connection()
		x = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username)))
		if int(x) > 0:
			flash("Set new password..")
			return render_template('forgot_password.html', form=form)
		else :
			c.execute("INSERT INTO users (username, email, password, confirm_password) VALUES (\"%s\",\" %s\", \"%s\", \"%s\")" % (thwart(username), thwart(email), thwart(password), thwart(confirm_password)))
		conn.commit()
		c.close()
		conn.close()
		return render_template('login.html')
	return render_template('forgot_password.html', form=form)


@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/leaderboard')
def leaderboard():
	return render_template('leaderboard.html')

@app.route('/quiz1')
def quiz1():
	return render_template('quiz1.html')

@app.route('/quiz2')
def quiz2():
	return render_template('quiz2.html')

@app.route('/quiz3')
def quiz3():
	return render_template('quiz3.html')

@app.route('/quiz4')
def quiz4():
	return render_template('quiz4.html')

if __name__=='__main__':
	app.run(debug=True)
