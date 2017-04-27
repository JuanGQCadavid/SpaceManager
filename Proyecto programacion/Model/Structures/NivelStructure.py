# -*- coding: cp1252 -*- 
class Nivel(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Nivel
	'''
	#Constructor con paso de parametros 
	def __init__(self, idNivel= None, idBloque= None, idSede= None, idOrg= None, idUsuarioEncargado= None, idEspacioPublico= None, descripcionNivel= None, numeroEspacios= None, numeroNivel= None):
		self.idNivel = idNivel 
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrg = idOrg 
		self.idUsuarioEncargado = idUsuarioEncargado 
		self.idEspacioPublico = idEspacioPublico 
		self.descripcionNivel = descripcionNivel 
		self.numeroEspacios = numeroEspacios 
		self.numeroNivel = numeroNivel 


	#Getters y Setters de idNivel

	def getIdNivel(self):
		return self.idNivel
	def setIdNivel(self,idNivel):
		self.idNivel = idNivel



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



	#Getters y Setters de idEspacioPublico

	def getIdEspacioPublico(self):
		return self.idEspacioPublico
	def setIdEspacioPublico(self,idEspacioPublico):
		self.idEspacioPublico = idEspacioPublico



	#Getters y Setters de descripcionNivel

	def getDescripcionNivel(self):
		return self.descripcionNivel
	def setDescripcionNivel(self,descripcionNivel):
		self.descripcionNivel = descripcionNivel



	#Getters y Setters de numeroEspacios

	def getNumeroEspacios(self):
		return self.numeroEspacios
	def setNumeroEspacios(self,numeroEspacios):
		self.numeroEspacios = numeroEspacios



	#Getters y Setters de numeroNivel

	def getNumeroNivel(self):
		return self.numeroNivel
	def setNumeroNivel(self,numeroNivel):
		self.numeroNivel = numeroNivel




#Autogenerado: 04/26/17 19:26:09