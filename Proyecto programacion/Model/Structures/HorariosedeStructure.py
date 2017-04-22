# -*- coding: cp1252 -*- 
class Horariosede(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Horariosede
	'''
	#Constructor con paso de parametros 
	def __init__(self, idHorarioSede= None, idDiasHabiles= None, idSede= None, horaApertura= None, horaCierre= None):
		self.idHorarioSede = idHorarioSede 
		self.idDiasHabiles = idDiasHabiles 
		self.idSede = idSede 
		self.horaApertura = horaApertura 
		self.horaCierre = horaCierre 


	#Getters y Setters de idHorarioSede

	def getIdHorarioSede(self):
		return self.idHorarioSede
	def setIdHorarioSede(self,idHorarioSede):
		self.idHorarioSede = idHorarioSede



	#Getters y Setters de idDiasHabiles

	def getIdDiasHabiles(self):
		return self.idDiasHabiles
	def setIdDiasHabiles(self,idDiasHabiles):
		self.idDiasHabiles = idDiasHabiles



	#Getters y Setters de idSede

	def getIdSede(self):
		return self.idSede
	def setIdSede(self,idSede):
		self.idSede = idSede



	#Getters y Setters de horaApertura

	def getHoraApertura(self):
		return self.horaApertura
	def setHoraApertura(self,horaApertura):
		self.horaApertura = horaApertura



	#Getters y Setters de horaCierre

	def getHoraCierre(self):
		return self.horaCierre
	def setHoraCierre(self,horaCierre):
		self.horaCierre = horaCierre




#Autogenerado: 04/22/17 10:35:27