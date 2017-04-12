# -*- coding: cp1252 -*- 
class Usuario(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Usuario
	'''
	#Constructor con paso de parametros 
	def __init__(self, idUsuario= None, nombreUsuario= None, descripcion= None, claveUsuario= None, estadoUsuario= None, telefonoCelular= None, correoElectronico= None, usuarioUsuario= None, idRedesSociales= None, idPrivacidad= None):
		self.idUsuario = idUsuario 
		self.nombreUsuario = nombreUsuario 
		self.descripcion = descripcion 
		self.claveUsuario = claveUsuario 
		self.estadoUsuario = estadoUsuario 
		self.telefonoCelular = telefonoCelular 
		self.correoElectronico = correoElectronico 
		self.usuarioUsuario = usuarioUsuario 
		self.idRedesSociales = idRedesSociales 
		self.idPrivacidad = idPrivacidad 


	#Getters y Setters de idUsuario

	def getIdUsuario(self):
		return self.idUsuario
	def setIdUsuario(self,idUsuario):
		self.idUsuario = idUsuario



	#Getters y Setters de nombreUsuario

	def getNombreUsuario(self):
		return self.nombreUsuario
	def setNombreUsuario(self,nombreUsuario):
		self.nombreUsuario = nombreUsuario



	#Getters y Setters de descripcion

	def getDescripcion(self):
		return self.descripcion
	def setDescripcion(self,descripcion):
		self.descripcion = descripcion



	#Getters y Setters de claveUsuario

	def getClaveUsuario(self):
		return self.claveUsuario
	def setClaveUsuario(self,claveUsuario):
		self.claveUsuario = claveUsuario



	#Getters y Setters de estadoUsuario

	def getEstadoUsuario(self):
		return self.estadoUsuario
	def setEstadoUsuario(self,estadoUsuario):
		self.estadoUsuario = estadoUsuario



	#Getters y Setters de telefonoCelular

	def getTelefonoCelular(self):
		return self.telefonoCelular
	def setTelefonoCelular(self,telefonoCelular):
		self.telefonoCelular = telefonoCelular



	#Getters y Setters de correoElectronico

	def getCorreoElectronico(self):
		return self.correoElectronico
	def setCorreoElectronico(self,correoElectronico):
		self.correoElectronico = correoElectronico



	#Getters y Setters de usuarioUsuario

	def getUsuarioUsuario(self):
		return self.usuarioUsuario
	def setUsuarioUsuario(self,usuarioUsuario):
		self.usuarioUsuario = usuarioUsuario



	#Getters y Setters de idRedesSociales

	def getIdRedesSociales(self):
		return self.idRedesSociales
	def setIdRedesSociales(self,idRedesSociales):
		self.idRedesSociales = idRedesSociales



	#Getters y Setters de idPrivacidad

	def getIdPrivacidad(self):
		return self.idPrivacidad
	def setIdPrivacidad(self,idPrivacidad):
		self.idPrivacidad = idPrivacidad




#Autogenerado: 04/11/17 21:51:37