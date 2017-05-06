# -*- coding: cp1252 -*- 
class Orgusuario(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Orgusuario
	'''
	#Constructor con paso de parametros 
	def __init__(self, idOrgUsuario= None, idOrgUsuarioCreador= None, idOrgContador= None, idUsuario= None, idPermisos= None, nombrePilaUser= None, estadoUsuario= None, fechaEstado= None):
		self.idOrgUsuario = idOrgUsuario 
		self.idOrgUsuarioCreador = idOrgUsuarioCreador 
		self.idOrgContador = idOrgContador 
		self.idUsuario = idUsuario 
		self.idPermisos = idPermisos 
		self.nombrePilaUser = nombrePilaUser 
		self.estadoUsuario = estadoUsuario 
		self.fechaEstado = fechaEstado 


	#Getters y Setters de idOrgUsuario

	def getIdOrgUsuario(self):
		return self.idOrgUsuario
	def setIdOrgUsuario(self,idOrgUsuario):
		self.idOrgUsuario = idOrgUsuario



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



	#Getters y Setters de idUsuario

	def getIdUsuario(self):
		return self.idUsuario
	def setIdUsuario(self,idUsuario):
		self.idUsuario = idUsuario



	#Getters y Setters de idPermisos

	def getIdPermisos(self):
		return self.idPermisos
	def setIdPermisos(self,idPermisos):
		self.idPermisos = idPermisos



	#Getters y Setters de nombrePilaUser

	def getNombrePilaUser(self):
		return self.nombrePilaUser
	def setNombrePilaUser(self,nombrePilaUser):
		self.nombrePilaUser = nombrePilaUser



	#Getters y Setters de estadoUsuario

	def getEstadoUsuario(self):
		return self.estadoUsuario
	def setEstadoUsuario(self,estadoUsuario):
		self.estadoUsuario = estadoUsuario



	#Getters y Setters de fechaEstado

	def getFechaEstado(self):
		return self.fechaEstado
	def setFechaEstado(self,fechaEstado):
		self.fechaEstado = fechaEstado




#Autogenerado: 05/05/17 23:15:34