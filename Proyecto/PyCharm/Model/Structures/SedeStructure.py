# -*- coding: cp1252 -*- 
class Sede(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Sede
	'''
	#Constructor con paso de parametros 
	def __init__(self, idSede= None, idOrgUsuarioCreador= None, idOrgContador= None, idDireccionSede= None, idUsuarioEncargado= None, nombreSede= None, numero_Bloques= None, fechaCreacion= None):
		self.idSede = idSede 
		self.idOrgUsuarioCreador = idOrgUsuarioCreador 
		self.idOrgContador = idOrgContador 
		self.idDireccionSede = idDireccionSede 
		self.idUsuarioEncargado = idUsuarioEncargado 
		self.nombreSede = nombreSede 
		self.numero_Bloques = numero_Bloques 
		self.fechaCreacion = fechaCreacion 


	#Getters y Setters de idSede

	def getIdSede(self):
		return self.idSede
	def setIdSede(self,idSede):
		self.idSede = idSede



	#Getters y Setters de idOrgUsuarioCreador

	def getIdOrgUsuarioCreador(self):
		return self.idOrgUsuarioCreador
	def setIdOrgUsuarioCreador(self,idOrgUsuarioCreador):
		self.idOrgUsuarioCreador = idOrgUsuarioCreador



	#Getters y Setters de idOrgContador

	def getIdOrgContador(self):
		return self.idOrgContador
	def setIdOrgContador(self,idOrgContador):
		self.idOrgContador = idOrgContador



	#Getters y Setters de idDireccionSede

	def getIdDireccionSede(self):
		return self.idDireccionSede
	def setIdDireccionSede(self,idDireccionSede):
		self.idDireccionSede = idDireccionSede



	#Getters y Setters de idUsuarioEncargado

	def getIdUsuarioEncargado(self):
		return self.idUsuarioEncargado
	def setIdUsuarioEncargado(self,idUsuarioEncargado):
		self.idUsuarioEncargado = idUsuarioEncargado



	#Getters y Setters de nombreSede

	def getNombreSede(self):
		return self.nombreSede
	def setNombreSede(self,nombreSede):
		self.nombreSede = nombreSede



	#Getters y Setters de numero_Bloques

	def getNumero_Bloques(self):
		return self.numero_Bloques
	def setNumero_Bloques(self,numero_Bloques):
		self.numero_Bloques = numero_Bloques



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion




#Autogenerado: 05/05/17 23:15:34