from wtforms import Form 
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import  EmailField

class loguinForm(Form):
	usuario = StringField('Usuario:')
	password = PasswordField('Correo Electronico:')
