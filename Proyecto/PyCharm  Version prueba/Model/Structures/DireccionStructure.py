# -*- coding: cp1252 -*- 
class Direccion(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Direccion
	'''
	#Constructor con paso de parametros 
	def __init__(self, idDireccion= None, idCiudad= None, idDepartamento= None, idPais= None, direccion= None):
		self.idDireccion = idDireccion 
		self.idCiudad = idCiudad 
		self.idDepartamento = idDepartamento 
		self.idPais = idPais 
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



	#Getters y Setters de idDepartamento

	def getIdDepartamento(self):
		return self.idDepartamento
	def setIdDepartamento(self,idDepartamento):
		self.idDepartamento = idDepartamento



	#Getters y Setters de idPais

	def getIdPais(self):
		return self.idPais
	def setIdPais(self,idPais):
		self.idPais = idPais



	#Getters y Setters de direccion

	def getDireccion(self):
		return self.direccion
	def setDireccion(self,direccion):
		self.direccion = direccion




#Autogenerado: 05/09/17 23:48:59