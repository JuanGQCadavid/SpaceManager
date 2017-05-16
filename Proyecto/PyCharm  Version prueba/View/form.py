from wtforms import Form 
from wtforms import StringField, RadioField, PasswordField,DateField, IntegerField
from wtforms.fields.html5 import  EmailField

class loguinForm(Form):
	usuario = StringField('Usuario:')
	password = PasswordField('Correo Electronico:')


class crear_Org_One(Form):
	Nombre_Org = StringField('nombre Org:')
	Descripcion = StringField(' Descripcion:')
	Facebook = StringField('Facebook:')
	Google = StringField('Google:')
	Twitter = StringField('Twitter:')
	LinkedIn = StringField('LinkedIn:')
	Instagram = StringField('Instagram:')
	Telefono = StringField('Telefono:')

class crear_Org_Two(Form):
	tipo_enrroll = RadioField(u'Tipo de Enrrol', choices=[('Invitacion', 'Invitacion'),
														   ('Solicitud', 'Solicitud'),
														   ('Libre', 'Libre')])

	Organizacion = RadioField(u'Organizacion', choices= [ ('Organizacion', 'Organizacion')])
	Sede = RadioField(u'Sede', choices=[('Sede', 'Sede')])
	Bloque = RadioField(u'Bloque', choices=[('Bloque', 'Bloque')])
	Nivel = RadioField(u'Nivel', choices=[('Nivel', 'Nivel')])
	Espacio = RadioField(u'Espacio', choices=[('Espacio', 'Espacio')])
	Reserva = RadioField(u'Reserva', choices=[('Reserva', 'Reserva')])


class from_Reservar(Form):
	Fecha_Inicio = DateField('Fecha_Inicio')
	Fecha_Fin = DateField('Fecha_Fin')
	Hora_Inicio = IntegerField('Hora_Inicio')
	Hora_Fin = IntegerField('Hora_Fin')

	Lunes = RadioField(u'Lunes', choices=[('Lunes', 'Lunes')])
	Martes = RadioField(u'Martes', choices=[('Martes', 'Martes')])
	Miercoles = RadioField(u'Miercoles', choices=[('Miercoles', 'Miercoles')])
	Jueves = RadioField(u'Jueves', choices=[('Jueves', 'Jueves')])
	Viernes = RadioField(u'Viernes', choices=[('Viernes', 'Viernes')])
	Sabado = RadioField(u'Sabado', choices=[('Sabado', 'Sabado')])
	Domingo = RadioField(u'Domingo', choices=[('Domingo', 'Domingo')])
