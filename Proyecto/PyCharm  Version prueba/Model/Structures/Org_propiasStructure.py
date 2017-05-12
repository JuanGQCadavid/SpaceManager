# -*- coding: cp1252 -*- 
class Org_propias(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Org_propias
	'''
	#Constructor con paso de parametros 
	def __init__(self, idUsuario= None, nombrePilaUser= None, estado_Usuario= None, nombre_Org= None, estado_Org= None):
		self.idUsuario = idUsuario 
		self.nombrePilaUser = nombrePilaUser 
		self.estado_Usuario = estado_Usuario 
		self.nombre_Org = nombre_Org 
		self.estado_Org = estado_Org 


	#Getters y Setters de idUsuario

	def getIdUsuario(self):
		return self.idUsuario
	def setIdUsuario(self,idUsuario):
		self.idUsuario = idUsuario



	#Getters y Setters de nombrePilaUser

	def getNombrePilaUser(self):
		return self.nombrePilaUser
	def setNombrePilaUser(self,nombrePilaUser):
		self.nombrePilaUser = nombrePilaUser



	#Getters y Setters de estado_Usuario

	def getEstado_Usuario(self):
		return self.estado_Usuario
	def setEstado_Usuario(self,estado_Usuario):
		self.estado_Usuario = estado_Usuario



	#Getters y Setters de nombre_Org

	def getNombre_Org(self):
		return self.nombre_Org
	def setNombre_Org(self,nombre_Org):
		self.nombre_Org = nombre_Org



	#Getters y Setters de estado_Org

	def getEstado_Org(self):
		return self.estado_Org
	def setEstado_Org(self,estado_Org):
		self.estado_Org = estado_Org




#Autogenerado: 05/09/17 23:48:59