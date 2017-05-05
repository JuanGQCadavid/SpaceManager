# -*- coding: cp1252 -*- 
class HorarioSede(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion HorarioSede
	'''
	#Constructor con paso de parametros 
	def __init__(self, idDiasHabiles= None, idSede= None, idOrgUsuarioCreador= None, idOrgContador= None, horaApertura= None, horaCierre= None):
		self.idDiasHabiles = idDiasHabiles 
		self.idSede = idSede 
		self.idOrgUsuarioCreador = idOrgUsuarioCreador 
		self.idOrgContador = idOrgContador 
		self.horaApertura = horaApertura 
		self.horaCierre = horaCierre 


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



	#Getters y Setters de idOrgUsuarioCreador

	def getIdOrgUsuarioCreador(self):
		return self.idOrgUsuarioCreador
	def setIdOrgUsuarioCreador(self,idOrgUsuarioCreador):
		self.idOrgUsuarioCreador = idOrgUsuarioCreador



	#Getters y Setters de idOrgContador

	def getIdOrgContador(self):
		return self.idOrgContador
	def setIdOrgContador(self,idOrgContador):
		self.idOrgContador = idOrgContador



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




#Autogenerado: Fri May  5 10:01:52 2017