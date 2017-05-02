# -*- coding: cp1252 -*- 
class Espacio(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Espacio
	'''
	#Constructor con paso de parametros 
	def __init__(self, idEspacio= None, idNivel= None, idBloque= None, idSede= None, idOrg= None, idPermiso= None, capacidadEspacio= None, descripcionEspaco= None):
		self.idEspacio = idEspacio 
		self.idNivel = idNivel 
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrg = idOrg 
		self.idPermiso = idPermiso 
		self.capacidadEspacio = capacidadEspacio 
		self.descripcionEspaco = descripcionEspaco 


	#Getters y Setters de idEspacio

	def getIdEspacio(self):
		return self.idEspacio
	def setIdEspacio(self,idEspacio):
		self.idEspacio = idEspacio



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



	#Getters y Setters de idPermiso

	def getIdPermiso(self):
		return self.idPermiso
	def setIdPermiso(self,idPermiso):
		self.idPermiso = idPermiso



	#Getters y Setters de capacidadEspacio

	def getCapacidadEspacio(self):
		return self.capacidadEspacio
	def setCapacidadEspacio(self,capacidadEspacio):
		self.capacidadEspacio = capacidadEspacio



	#Getters y Setters de descripcionEspaco

	def getDescripcionEspaco(self):
		return self.descripcionEspaco
	def setDescripcionEspaco(self,descripcionEspaco):
		self.descripcionEspaco = descripcionEspaco




#Autogenerado: 04/30/17 16:16:30