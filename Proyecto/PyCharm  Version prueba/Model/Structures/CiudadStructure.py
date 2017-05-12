# -*- coding: cp1252 -*- 
class Ciudad(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Ciudad
	'''
	#Constructor con paso de parametros 
	def __init__(self, idCiudad= None, idDepartamento= None, idPais= None, nombre= None):
		self.idCiudad = idCiudad 
		self.idDepartamento = idDepartamento 
		self.idPais = idPais 
		self.nombre = nombre 


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



	#Getters y Setters de nombre

	def getNombre(self):
		return self.nombre
	def setNombre(self,nombre):
		self.nombre = nombre




#Autogenerado: 05/09/17 23:48:59