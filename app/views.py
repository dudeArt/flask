from app import app
from flask import render_template, flash, redirect
from forms import LoginForm

users = [
	{'nick': 'Dude', 'name': 'Dudka Artem Vadimovich'},
	{'nick': 'max', 'name': 'Piqulin Maxim Romanovich'}
]

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
					title = 'Main Page')

@app.route('/profile/<nick>')
def profile(nick):
	user = None
	for el in users:
		if el['nick'] == nick:
			user = el
			break
	return render_template('profile.html',
						title = 'Profile',
						user = user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect('/profile/' + str(form.nick.data))
	flash('Data has been input incorrectly.')
	return render_template('login.html',
							title = 'Log In',
							form = form)
