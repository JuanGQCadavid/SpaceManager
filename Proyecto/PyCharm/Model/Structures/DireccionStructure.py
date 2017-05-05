# -*- coding: cp1252 -*- 
class Direccion(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Direccion
	'''
	#Constructor con paso de parametros 
	def __init__(self, idDireccion= None, idCiudad= None, direccion= None):
		self.idDireccion = idDireccion 
		self.idCiudad = idCiudad 
		self.direccion = direccion 


	#Getters y Setters de idDireccion

	def getIdDireccion(self):
		return self.idDireccion
	def setIdDireccion(self,idDireccion):
		self.idDireccion = idDireccion



	#Getters y Setters de idCiudad

	def getIdCiudad(self):
		return self.idCiudad
	def setIdCiudad(self,idCiudad):
		self.idCiudad = idCiudad



	#Getters y Setters de direccion

	def getDireccion(self):
		return self.direccion
	def setDireccion(self,direccion):
		self.direccion = direccion




#Autogenerado: Fri May  5 10:01:52 2017