from wtforms import Form 
from wtforms import StringField, TextField
from wtforms.fields.html5 import  EmailField
class comentForm(Form):
	usuario = StringField('Usuario:')
	email = EmailField('Correo Electronico:')
	comentario = TextField('Comentario: ')
