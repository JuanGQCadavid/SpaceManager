# -*- coding: cp1252 -*- 
class Espacio(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Espacio
	'''
	#Constructor con paso de parametros 
	def __init__(self, idEspacio= None, idNivel= None, idBloque= None, idSede= None, idOrgCreador= None, idOrgContador= None, idPermiso= None, capacidadEspacio= None, descripcionEspaco= None, nomenclaturaEspecal= None, fechaCreacion= None):
		self.idEspacio = idEspacio 
		self.idNivel = idNivel 
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrgCreador = idOrgCreador 
		self.idOrgContador = idOrgContador 
		self.idPermiso = idPermiso 
		self.capacidadEspacio = capacidadEspacio 
		self.descripcionEspaco = descripcionEspaco 
		self.nomenclaturaEspecal = nomenclaturaEspecal 
		self.fechaCreacion = fechaCreacion 


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



	#Getters y Setters de idOrgCreador

	def getIdOrgCreador(self):
		return self.idOrgCreador
	def setIdOrgCreador(self,idOrgCreador):
		self.idOrgCreador = idOrgCreador



	#Getters y Setters de idOrgContador

	def getIdOrgContador(self):
		return self.idOrgContador
	def setIdOrgContador(self,idOrgContador):
		self.idOrgContador = idOrgContador



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



	#Getters y Setters de nomenclaturaEspecal

	def getNomenclaturaEspecal(self):
		return self.nomenclaturaEspecal
	def setNomenclaturaEspecal(self,nomenclaturaEspecal):
		self.nomenclaturaEspecal = nomenclaturaEspecal



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion




#Autogenerado: 05/06/17 12:11:06