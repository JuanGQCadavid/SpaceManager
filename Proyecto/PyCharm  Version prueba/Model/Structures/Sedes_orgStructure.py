# -*- coding: cp1252 -*- 
class Sedes_org(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Sedes_org
	'''
	#Constructor con paso de parametros 
	def __init__(self, idSede= None, idOrgUsuarioCreador= None, idOrgContador= None, nombreSede= None, encargado= None, fechaCreacion= None):
		self.idSede = idSede 
		self.idOrgUsuarioCreador = idOrgUsuarioCreador 
		self.idOrgContador = idOrgContador 
		self.nombreSede = nombreSede 
		self.encargado = encargado 
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



	#Getters y Setters de nombreSede

	def getNombreSede(self):
		return self.nombreSede
	def setNombreSede(self,nombreSede):
		self.nombreSede = nombreSede



	#Getters y Setters de encargado

	def getEncargado(self):
		return self.encargado
	def setEncargado(self,encargado):
		self.encargado = encargado



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion




#Autogenerado: 05/09/17 23:48:59