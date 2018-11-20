from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from dbconnect import connection
from MySQLdb import escape_string as thwart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ShshhhYouCannotTellAnyone'
Bootstrap(app)

class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

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
		c, conn = connection()
		x = c.execute("SELECT * FROM users WHERE username = \"%s\"" % (thwart(username)))
		if int(x) > 0:
			flash("username already taken...please choose another...")
			return render_template('signup.html', form=form)
		else :
			c.execute("INSERT INTO users (username, email, password) VALUES (\"%s\",\" %s\", \"%s\")" % (thwart(username), thwart(email), thwart(password)))	
		conn.commit()
		c.close()
		conn.close()
		return render_template('dashboard.html')
	return render_template('signup.html', form=form)

if __name__=='__main__':
	app.run(debug=True)