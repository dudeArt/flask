from app import app, db, models
from flask import render_template, flash, redirect
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
					title = 'Main Page')

@app.route('/profile/<int:id>')
def profile(id):
	user = models.User.query.filter_by(id = id).first()
	return render_template('profile.html',
						title = 'Profile',
						user = user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = models.User.query.filter_by(nick = str(form.nick.data), password = str(form.password.data)).first()
		if user:
			flash('User ' + str(user.nick) + ' has successfully logged in.')
			return redirect('/profile/' + str(user.id))
		else:
			flash('User with login ' + str(form.nick.data) + ' does not exist.')
			return redirect('/')
	flash('Data has been input incorrectly.')
	return render_template('login.html',
							title = 'Log In',
							form = form)

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
	form = LoginForm()
	if form.validate_on_submit():
		user = models.User(nick = unicode(str(form.nick.data), "utf-8"), password = unicode(str(form.password.data), "utf-8"))
		db.session.add(user)
		if db.session.commit():
			flash("User " + str(user.nick) + " has benn successfully added.")
		else:
			flash("Error while adding user " + str(user.nick))
		return redirect('/')
	return render_template('reg.html',
						title = 'Registration',
						form = form)


