# -*- coding: cp1252 -*- 
class Reserva(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Reserva
	'''
	#Constructor con paso de parametros 
	def __init__(self, idReserva= None, idEspacio= None, idUsuario= None, idDiasReserva= None, fechaInicio= None, fechaFin= None, horaInicio= None, horaFin= None):
		self.idReserva = idReserva 
		self.idEspacio = idEspacio 
		self.idUsuario = idUsuario 
		self.idDiasReserva = idDiasReserva 
		self.fechaInicio = fechaInicio 
		self.fechaFin = fechaFin 
		self.horaInicio = horaInicio 
		self.horaFin = horaFin 


	#Getters y Setters de idReserva

	def getIdReserva(self):
		return self.idReserva
	def setIdReserva(self,idReserva):
		self.idReserva = idReserva



	#Getters y Setters de idEspacio

	def getIdEspacio(self):
		return self.idEspacio
	def setIdEspacio(self,idEspacio):
		self.idEspacio = idEspacio



	#Getters y Setters de idUsuario

	def getIdUsuario(self):
		return self.idUsuario
	def setIdUsuario(self,idUsuario):
		self.idUsuario = idUsuario



	#Getters y Setters de idDiasReserva

	def getIdDiasReserva(self):
		return self.idDiasReserva
	def setIdDiasReserva(self,idDiasReserva):
		self.idDiasReserva = idDiasReserva



	#Getters y Setters de fechaInicio

	def getFechaInicio(self):
		return self.fechaInicio
	def setFechaInicio(self,fechaInicio):
		self.fechaInicio = fechaInicio



	#Getters y Setters de fechaFin

	def getFechaFin(self):
		return self.fechaFin
	def setFechaFin(self,fechaFin):
		self.fechaFin = fechaFin



	#Getters y Setters de horaInicio

	def getHoraInicio(self):
		return self.horaInicio
	def setHoraInicio(self,horaInicio):
		self.horaInicio = horaInicio



	#Getters y Setters de horaFin

	def getHoraFin(self):
		return self.horaFin
	def setHoraFin(self,horaFin):
		self.horaFin = horaFin




#Autogenerado: 04/11/17 21:18:43