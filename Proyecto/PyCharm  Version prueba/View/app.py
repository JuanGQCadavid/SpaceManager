from flask import Flask, render_template, request,url_for, redirect
from Controller.Reserva_Controller import reservar
from Controller.UserController import userLogin,obtenerUser

import datetime
from View import form

app = Flask(__name__)
app.debug = True



@app.route('/',methods = ['GET','POST'])
def index():
	log_in = form.loguinForm(request.form)

	if request.method == 'POST':
		user = log_in.usuario.data
		passw =  log_in.password.data
		resp = userLogin(user,passw)
		print resp;
		if resp == 1:
			return redirect(url_for('perfilU', USER = user))
		else:
			return render_template('Login.html', form = log_in, error = 'Datos Erroneos')

	return render_template('Login.html',form = log_in, error = None)


@app.route('/org/crear/<USER>',methods = ['GET','POST'])
def crearOrg(USER):
	part_One = form.crear_Org_One(request.form)

	if request.method == 'POST':


		Nombre_Org = part_One.Nombre_Org.data,
		Descripcion = part_One.Descripcion.data,
		Facebook = part_One.Facebook.data,
		Google = part_One.Google.data,
		Twitter = part_One.Twitter.data,
		LinkedIn = part_One.LinkedIn.data,
		Instagram = part_One.Instagram.data,
		Telefono = part_One.Telefono.data


		return redirect(url_for('continuar_ORG', userID = USER, Nombre_Org= Nombre_Org, Descripcion=Descripcion,Facebook = Facebook,
								Google =Google, Twitter=Twitter, LinkedIn=LinkedIn,Instagram= Instagram,Telefono = Telefono))


	return render_template('nuevaOrganizacion_1.html', USER = USER, form=part_One)

@app.route('/org/continuar_O/<userID>%<Nombre_Org>%<Descripcion>%<Facebook>%<Google>%<Twitter>%<LinkedIn>%<Instagram>%<Telefono>',methods = ['GET','POST'])
def continuar_ORG(userID,Nombre_Org,Descripcion, Facebook, Google, Twitter, LinkedIn, Instagram, Telefono):
	part_two = form.crear_Org_Two(request.form)

	if request.method == 'POST':
		tipo_enrroll = part_two.tipo_enrroll.data

		Organizacion =  part_two.Organizacion.data,
		Sede =  part_two.Sede.data,
		Bloque =  part_two.Bloque.data,
		Nivel =  part_two.Nivel.data,
		Espacio =  part_two.Espacio.data,
		Reserva =  part_two.Reserva.data

		valoresOrg = [userID, Nombre_Org, Descripcion,Facebook,Google,Twitter, LinkedIn, Instagram, Telefono,
					  tipo_enrroll,Organizacion, Sede,Bloque, Nivel,Espacio, Reserva]

		print valoresOrg


	return render_template('nuevaOrganizacion_2.html', form = part_two)


@app.route('/perfilU/<USER>',methods = ['GET'])
def perfilU(USER):
	return render_template('perfil.html', userList = obtenerUser(USER))







@app.route('/reservar/<idOrgCreador>$<idOrgContador>$<idSede>', methods = ['GET','POST'])
def reservarVista(idOrgCreador,idOrgContador,idSede):
	from_Reservar = form.from_Reservar(request.form)

	if request.method == 'POST':


		if from_Reservar.Lunes.data == None:
			lunes = True
		else:
			lunes = False

		if from_Reservar.Martes.data == None:
			martes = True
		else:
			martes = False

		if from_Reservar.Miercoles.data == None:
			miercoles = True
		else:
			miercoles = False
		if from_Reservar.Jueves.data == None:
			jueves = True
		else:
			jueves = False
		if from_Reservar.Viernes.data == None:
			viernes = True
		else:
			viernes = False
		if from_Reservar.Sabado.data == None:
			sabado = True
		else:
			sabado = False
		if from_Reservar.Domingo.data == None:
			domingo = True
		else:
			domingo = False

		return redirect(url_for('espacios_Disponibles',idOrgCreador=idOrgCreador, idOrgContador= idOrgContador,idSede = idSede, horaInicio = from_Reservar.Hora_Inicio.data,horahoraFin = from_Reservar.Hora_Fin.data,
								lunes = lunes,martes = martes, miercoles = miercoles, jueves = jueves,viernes = viernes,
								sabado = sabado, domingo = domingo))




	return render_template('Reservar.html', form = from_Reservar)



@app.route('/reservar/espacios_disponibles/<idOrgCreador>%<idOrgContador>%<idSede>%<horaInicio>%<horahoraFin>%<lunes>$<martes>$<miercoles>$<jueves>$<viernes>$<sabado>$<domingo>$', methods = ['GET','POST'])
def espacios_Disponibles(idOrgCreador,idOrgContador,idSede,horaInicio,horahoraFin,lunes,martes, miercoles, jueves,viernes, sabado, domingo):

	if request.method == 'GET':
		print '--------------------'
		print request.args.get('dias')
		print '--------------------'

	horaInicio = datetime.timedelta(hours=int(horaInicio), minutes=0, seconds=0)
	horahoraFin = datetime.timedelta(hours=int(horahoraFin), minutes=0, seconds=0)


	disponibles = reservar(idOrgCreador, idOrgContador, idSede, None, None, horaInicio, horahoraFin, lunes, martes, miercoles, jueves, viernes,sabado ,domingo)



	return render_template('reservaResultados.html',disponibles = disponibles, lunes = lunes,martes =martes,miercoles =miercoles,
						   jueves = jueves,viernes= viernes,sabado =sabado,domingo=domingo)


def mo():
	pass

if __name__ == '__main__':
	app.run()