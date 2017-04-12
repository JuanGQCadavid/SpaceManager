# -*- coding: cp1252 -*- 
class Mensajes(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Mensajes
	'''
	#Constructor con paso de parametros 
	def __init__(self, idMensajes= None, fechaMensaje= None, tipoMensaje= None, asuntoMensaje= None, descripcionMensaje= None, usuarioAutor= None, orgId= None):
		self.idMensajes = idMensajes 
		self.fechaMensaje = fechaMensaje 
		self.tipoMensaje = tipoMensaje 
		self.asuntoMensaje = asuntoMensaje 
		self.descripcionMensaje = descripcionMensaje 
		self.usuarioAutor = usuarioAutor 
		self.orgId = orgId 


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



	#Getters y Setters de tipoMensaje

	def getTipoMensaje(self):
		return self.tipoMensaje
	def setTipoMensaje(self,tipoMensaje):
		self.tipoMensaje = tipoMensaje



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



	#Getters y Setters de orgId

	def getOrgId(self):
		return self.orgId
	def setOrgId(self,orgId):
		self.orgId = orgId




#Autogenerado: 04/11/17 21:18:43