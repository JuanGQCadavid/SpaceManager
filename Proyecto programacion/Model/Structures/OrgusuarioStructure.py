# -*- coding: cp1252 -*- 
class Orgusuario(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Orgusuario
	'''
	#Constructor con paso de parametros 
	def __init__(self, idOrgUsuario= None, idUsuario= None, idOrg= None, idPermisos= None, nombrePilaUser= None, estadoUsuario= None):
		self.idOrgUsuario = idOrgUsuario 
		self.idUsuario = idUsuario 
		self.idOrg = idOrg 
		self.idPermisos = idPermisos 
		self.nombrePilaUser = nombrePilaUser 
		self.estadoUsuario = estadoUsuario 


	#Getters y Setters de idOrgUsuario

	def getIdOrgUsuario(self):
		return self.idOrgUsuario
	def setIdOrgUsuario(self,idOrgUsuario):
		self.idOrgUsuario = idOrgUsuario



	#Getters y Setters de idUsuario

	def getIdUsuario(self):
		return self.idUsuario
	def setIdUsuario(self,idUsuario):
		self.idUsuario = idUsuario



	#Getters y Setters de idOrg

	def getIdOrg(self):
		return self.idOrg
	def setIdOrg(self,idOrg):
		self.idOrg = idOrg



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




#Autogenerado: 04/22/17 10:35:27