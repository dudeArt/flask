from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required, Length

class LoginForm(Form):
	nick = TextField('nick', validators = [Required(), Length(min = 1, max = 21, message = "Too long")])
	password = PasswordField('password', validators = [Required(), Length(min = 1, max = 21, message = "Too long")])
	remember_me = BooleanField('remember_me', default = False)
