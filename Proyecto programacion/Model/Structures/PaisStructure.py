# -*- coding: cp1252 -*- 
class Pais(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Pais
	'''
	#Constructor con paso de parametros 
	def __init__(self, idPais= None, nombreP= None):
		self.idPais = idPais 
		self.nombreP = nombreP 


	#Getters y Setters de idPais

	def getIdPais(self):
		return self.idPais
	def setIdPais(self,idPais):
		self.idPais = idPais



	#Getters y Setters de nombreP

	def getNombreP(self):
		return self.nombreP
	def setNombreP(self,nombreP):
		self.nombreP = nombreP




#Autogenerado: 04/22/17 10:35:27