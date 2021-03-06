from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nick = db.Column(db.String(64), index = True, unique = True)
	password = db.Column(db.String(64), index = True, unique = True)
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic') #backref - imya svyazannogo polya

	def __repr__(self):
		return '<User %r>' %(self.nick)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' %(self.body)