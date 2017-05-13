# -*- coding: cp1252 -*- 
class Usuarios_org(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Usuarios_org
	'''
	#Constructor con paso de parametros 
	def __init__(self, idOrgUsuario= None, idOrgUsuarioCreador= None, nombre= None, idPermisos= None, nombrePilaUser= None, estadoUsuario= None, fechaEstado= None):
		self.idOrgUsuario = idOrgUsuario 
		self.idOrgUsuarioCreador = idOrgUsuarioCreador 
		self.nombre = nombre 
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



	#Getters y Setters de nombre

	def getNombre(self):
		return self.nombre
	def setNombre(self,nombre):
		self.nombre = nombre



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




#Autogenerado: 05/09/17 23:48:59