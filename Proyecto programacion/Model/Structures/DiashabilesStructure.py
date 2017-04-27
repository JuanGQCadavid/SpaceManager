# -*- coding: cp1252 -*- 
class Diashabiles(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Diashabiles
	'''
	#Constructor con paso de parametros 
	def __init__(self, idDiasHabiles= None, lunes= None, martes= None, miercoles= None, jueves= None, viernes= None, sabado= None, domingo= None):
		self.idDiasHabiles = idDiasHabiles 
		self.lunes = lunes 
		self.martes = martes 
		self.miercoles = miercoles 
		self.jueves = jueves 
		self.viernes = viernes 
		self.sabado = sabado 
		self.domingo = domingo 


	#Getters y Setters de idDiasHabiles

	def getIdDiasHabiles(self):
		return self.idDiasHabiles
	def setIdDiasHabiles(self,idDiasHabiles):
		self.idDiasHabiles = idDiasHabiles



	#Getters y Setters de lunes

	def getLunes(self):
		return self.lunes
	def setLunes(self,lunes):
		self.lunes = lunes



	#Getters y Setters de martes

	def getMartes(self):
		return self.martes
	def setMartes(self,martes):
		self.martes = martes



	#Getters y Setters de miercoles

	def getMiercoles(self):
		return self.miercoles
	def setMiercoles(self,miercoles):
		self.miercoles = miercoles



	#Getters y Setters de jueves

	def getJueves(self):
		return self.jueves
	def setJueves(self,jueves):
		self.jueves = jueves



	#Getters y Setters de viernes

	def getViernes(self):
		return self.viernes
	def setViernes(self,viernes):
		self.viernes = viernes



	#Getters y Setters de sabado

	def getSabado(self):
		return self.sabado
	def setSabado(self,sabado):
		self.sabado = sabado



	#Getters y Setters de domingo

	def getDomingo(self):
		return self.domingo
	def setDomingo(self,domingo):
		self.domingo = domingo




#Autogenerado: 04/26/17 19:26:09