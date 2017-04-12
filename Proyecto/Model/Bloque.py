# -*- coding: cp1252 -*- 
class Bloque(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Bloque
	'''
	#Constructor con paso de parametros 
	def __init__(self, idBloque= None, idSede= None, idOrg= None, idUsuarioEncargado= None, descripcionBloqe= None, numeroNiveles= None):
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrg = idOrg 
		self.idUsuarioEncargado = idUsuarioEncargado 
		self.descripcionBloqe = descripcionBloqe 
		self.numeroNiveles = numeroNiveles 


	#Getters y Setters de idBloque

	def getIdBloque(self):
		return self.idBloque
	def setIdBloque(self,idBloque):
		self.idBloque = idBloque



	#Getters y Setters de idSede

	def getIdSede(self):
		return self.idSede
	def setIdSede(self,idSede):
		self.idSede = idSede



	#Getters y Setters de idOrg

	def getIdOrg(self):
		return self.idOrg
	def setIdOrg(self,idOrg):
		self.idOrg = idOrg



	#Getters y Setters de idUsuarioEncargado

	def getIdUsuarioEncargado(self):
		return self.idUsuarioEncargado
	def setIdUsuarioEncargado(self,idUsuarioEncargado):
		self.idUsuarioEncargado = idUsuarioEncargado



	#Getters y Setters de descripcionBloqe

	def getDescripcionBloqe(self):
		return self.descripcionBloqe
	def setDescripcionBloqe(self,descripcionBloqe):
		self.descripcionBloqe = descripcionBloqe



	#Getters y Setters de numeroNiveles

	def getNumeroNiveles(self):
		return self.numeroNiveles
	def setNumeroNiveles(self,numeroNiveles):
		self.numeroNiveles = numeroNiveles




#Autogenerado: 04/11/17 21:51:37