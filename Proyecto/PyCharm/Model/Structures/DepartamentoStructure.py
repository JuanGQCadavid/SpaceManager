# -*- coding: cp1252 -*- 
class Departamento(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Departamento
	'''
	#Constructor con paso de parametros 
	def __init__(self, idDepartamento= None, idPais= None, nombreDep= None):
		self.idDepartamento = idDepartamento 
		self.idPais = idPais 
		self.nombreDep = nombreDep 


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



	#Getters y Setters de nombreDep

	def getNombreDep(self):
		return self.nombreDep
	def setNombreDep(self,nombreDep):
		self.nombreDep = nombreDep




#Autogenerado: 05/06/17 12:11:06