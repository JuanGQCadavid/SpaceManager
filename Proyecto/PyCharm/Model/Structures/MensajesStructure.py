# -*- coding: cp1252 -*- 
class Mensajes(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Mensajes
	'''
	#Constructor con paso de parametros 
	def __init__(self, idMensajes= None, fechaMensaje= None, asuntoMensaje= None, descripcionMensaje= None, usuarioAutor= None, idOrgCreador= None, idOrgContador= None):
		self.idMensajes = idMensajes 
		self.fechaMensaje = fechaMensaje 
		self.asuntoMensaje = asuntoMensaje 
		self.descripcionMensaje = descripcionMensaje 
		self.usuarioAutor = usuarioAutor 
		self.idOrgCreador = idOrgCreador 
		self.idOrgContador = idOrgContador 


	#Getters y Setters de idMensajes

	def getIdMensajes(self):
		return self.idMensajes
	def setIdMensajes(self,idMensajes):
		self.idMensajes = idMensajes



	#Getters y Setters de fechaMensaje

	def getFechaMensaje(self):
		return self.fechaMensaje
	def setFechaMensaje(self,fechaMensaje):
		self.fechaMensaje = fechaMensaje



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




#Autogenerado: 05/06/17 23:33:57