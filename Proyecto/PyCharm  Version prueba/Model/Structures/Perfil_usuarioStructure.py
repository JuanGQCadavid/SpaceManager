# -*- coding: cp1252 -*- 
class Perfil_usuario(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Perfil_usuario
	'''
	#Constructor con paso de parametros 
	def __init__(self, idUsuario= None, nombreUsuario= None, descripcion= None, telefonoCelular= None, correoElectronico= None, estadousuario= None, fechaCreacion= None, mostrarCorreo= None, mostrarOrgPertenece= None, mostrarOrgPropias= None, mostrarRedesSociales= None, mostrarTelefono= None, faceBook= None, twitter= None, linkedin= None, instagram= None, google= None):
		self.idUsuario = idUsuario 
		self.nombreUsuario = nombreUsuario 
		self.descripcion = descripcion 
		self.telefonoCelular = telefonoCelular 
		self.correoElectronico = correoElectronico 
		self.estadousuario = estadousuario 
		self.fechaCreacion = fechaCreacion 
		self.mostrarCorreo = mostrarCorreo 
		self.mostrarOrgPertenece = mostrarOrgPertenece 
		self.mostrarOrgPropias = mostrarOrgPropias 
		self.mostrarRedesSociales = mostrarRedesSociales 
		self.mostrarTelefono = mostrarTelefono 
		self.faceBook = faceBook 
		self.twitter = twitter 
		self.linkedin = linkedin 
		self.instagram = instagram 
		self.google = google 


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



	#Getters y Setters de estadousuario

	def getEstadousuario(self):
		return self.estadousuario
	def setEstadousuario(self,estadousuario):
		self.estadousuario = estadousuario



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion



	#Getters y Setters de mostrarCorreo

	def getMostrarCorreo(self):
		return self.mostrarCorreo
	def setMostrarCorreo(self,mostrarCorreo):
		self.mostrarCorreo = mostrarCorreo



	#Getters y Setters de mostrarOrgPertenece

	def getMostrarOrgPertenece(self):
		return self.mostrarOrgPertenece
	def setMostrarOrgPertenece(self,mostrarOrgPertenece):
		self.mostrarOrgPertenece = mostrarOrgPertenece



	#Getters y Setters de mostrarOrgPropias

	def getMostrarOrgPropias(self):
		return self.mostrarOrgPropias
	def setMostrarOrgPropias(self,mostrarOrgPropias):
		self.mostrarOrgPropias = mostrarOrgPropias



	#Getters y Setters de mostrarRedesSociales

	def getMostrarRedesSociales(self):
		return self.mostrarRedesSociales
	def setMostrarRedesSociales(self,mostrarRedesSociales):
		self.mostrarRedesSociales = mostrarRedesSociales



	#Getters y Setters de mostrarTelefono

	def getMostrarTelefono(self):
		return self.mostrarTelefono
	def setMostrarTelefono(self,mostrarTelefono):
		self.mostrarTelefono = mostrarTelefono



	#Getters y Setters de faceBook

	def getFaceBook(self):
		return self.faceBook
	def setFaceBook(self,faceBook):
		self.faceBook = faceBook



	#Getters y Setters de twitter

	def getTwitter(self):
		return self.twitter
	def setTwitter(self,twitter):
		self.twitter = twitter



	#Getters y Setters de linkedin

	def getLinkedin(self):
		return self.linkedin
	def setLinkedin(self,linkedin):
		self.linkedin = linkedin



	#Getters y Setters de instagram

	def getInstagram(self):
		return self.instagram
	def setInstagram(self,instagram):
		self.instagram = instagram



	#Getters y Setters de google

	def getGoogle(self):
		return self.google
	def setGoogle(self,google):
		self.google = google




#Autogenerado: 05/09/17 23:48:59