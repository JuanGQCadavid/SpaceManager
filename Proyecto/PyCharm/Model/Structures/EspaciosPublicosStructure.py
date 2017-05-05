# -*- coding: cp1252 -*- 
class EspaciosPublicos(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion EspaciosPublicos
	'''
	#Constructor con paso de parametros 
	def __init__(self, idEspaciosPublcos= None, tieneBanos= None, tieneCocineta= None, tieneSalaEstar= None):
		self.idEspaciosPublcos = idEspaciosPublcos 
		self.tieneBanos = tieneBanos 
		self.tieneCocineta = tieneCocineta 
		self.tieneSalaEstar = tieneSalaEstar 


	#Getters y Setters de idEspaciosPublcos

	def getIdEspaciosPublcos(self):
		return self.idEspaciosPublcos
	def setIdEspaciosPublcos(self,idEspaciosPublcos):
		self.idEspaciosPublcos = idEspaciosPublcos



	#Getters y Setters de tieneBanos

	def getTieneBanos(self):
		return self.tieneBanos
	def setTieneBanos(self,tieneBanos):
		self.tieneBanos = tieneBanos



	#Getters y Setters de tieneCocineta

	def getTieneCocineta(self):
		return self.tieneCocineta
	def setTieneCocineta(self,tieneCocineta):
		self.tieneCocineta = tieneCocineta



	#Getters y Setters de tieneSalaEstar

	def getTieneSalaEstar(self):
		return self.tieneSalaEstar
	def setTieneSalaEstar(self,tieneSalaEstar):
		self.tieneSalaEstar = tieneSalaEstar




#Autogenerado: Fri May  5 10:01:52 2017