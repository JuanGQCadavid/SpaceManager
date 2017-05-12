# -*- coding: cp1252 -*- 
class Pais_dep_ciudad(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Pais_dep_ciudad
	'''
	#Constructor con paso de parametros 
	def __init__(self, pais= None, departamento= None, ciudad= None):
		self.pais = pais 
		self.departamento = departamento 
		self.ciudad = ciudad 


	#Getters y Setters de pais

	def getPais(self):
		return self.pais
	def setPais(self,pais):
		self.pais = pais



	#Getters y Setters de departamento

	def getDepartamento(self):
		return self.departamento
	def setDepartamento(self,departamento):
		self.departamento = departamento



	#Getters y Setters de ciudad

	def getCiudad(self):
		return self.ciudad
	def setCiudad(self,ciudad):
		self.ciudad = ciudad




#Autogenerado: 05/09/17 23:48:59