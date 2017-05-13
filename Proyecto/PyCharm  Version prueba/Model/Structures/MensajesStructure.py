# -*- coding: cp1252 -*- 
class Mensajes(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Mensajes
	'''
	#Constructor con paso de parametros 
	def __init__(self, idMensajes= None, idOrgCreador= None, idOrgContador= None, asuntoMensaje= None, descripcionMensaje= None, usuarioAutor= None, tipoMensaje= None, fechaMensaje= None):
		self.idMensajes = idMensajes 
		self.idOrgCreador = idOrgCreador 
		self.idOrgContador = idOrgContador 
		self.asuntoMensaje = asuntoMensaje 
		self.descripcionMensaje = descripcionMensaje 
		self.usuarioAutor = usuarioAutor 
		self.tipoMensaje = tipoMensaje 
		self.fechaMensaje = fechaMensaje 


	#Getters y Setters de idMensajes

	def getIdMensajes(self):
		return self.idMensajes
	def setIdMensajes(self,idMensajes):
		self.idMensajes = idMensajes



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



	#Getters y Setters de asuntoMensaje

	def getAsuntoMensaje(self):
		return self.asuntoMensaje
	def setAsuntoMensaje(self,asuntoMensaje):
		self.asuntoMensaje = asuntoMensaje



	#Getters y Setters de descripcionMensaje

	def getDescripcionMensaje(self):
		return self.descripcionMensaje
	def setDescripcionMensaje(self,descripcionMensaje):
		self.descripcionMensaje = descripcionMensaje



	#Getters y Setters de usuarioAutor

	def getUsuarioAutor(self):
		return self.usuarioAutor
	def setUsuarioAutor(self,usuarioAutor):
		self.usuarioAutor = usuarioAutor



	#Getters y Setters de tipoMensaje

	def getTipoMensaje(self):
		return self.tipoMensaje
	def setTipoMensaje(self,tipoMensaje):
		self.tipoMensaje = tipoMensaje



	#Getters y Setters de fechaMensaje

	def getFechaMensaje(self):
		return self.fechaMensaje
	def setFechaMensaje(self,fechaMensaje):
		self.fechaMensaje = fechaMensaje




#Autogenerado: 05/09/17 23:48:59