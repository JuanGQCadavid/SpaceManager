from flask import Flask, render_template, request
from Controller.Reserva_Controller import reservar
import datetime

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	return render_template('Login.html')


@app.route('/reservar')
def reservarVista():
	return render_template('Reservar.html')

@app.route('/reservar/espacios_disponibles')
def espacios_Disponibles():

	horaInicio = datetime.timedelta(hours=15, minutes=0, seconds=0)
	horahoraFin = datetime.timedelta(hours=16, minutes=0, seconds=0)

	lunes = True
	martes = False
	miercoles = False
	jueves = True
	viernes = False
	sabado = False
	domingo = True

	disponibles = reservar('jquiro12', 1, 1, None, None, horaInicio, horahoraFin, lunes, martes, miercoles, jueves, viernes,sabado ,domingo)



	return render_template('reservaResultados.html',disponibles = disponibles, lunes = lunes,martes =martes,miercoles =miercoles,
						   jueves = jueves,viernes= viernes,sabado =sabado,domingo=domingo)

if __name__ == '__main__':
	app.run()