# -*- coding: cp1252 -*- 
class Privacidadusuario(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Privacidadusuario
	'''
	#Constructor con paso de parametros 
	def __init__(self, idPrivacidadUsuario= None, mostrarCorreo= None, mostrarOrgPropias= None, mostrarOrgPertenece= None, mostrarRedesSociales= None, mostrarTelefono= None):
		self.idPrivacidadUsuario = idPrivacidadUsuario 
		self.mostrarCorreo = mostrarCorreo 
		self.mostrarOrgPropias = mostrarOrgPropias 
		self.mostrarOrgPertenece = mostrarOrgPertenece 
		self.mostrarRedesSociales = mostrarRedesSociales 
		self.mostrarTelefono = mostrarTelefono 


	#Getters y Setters de idPrivacidadUsuario

	def getIdPrivacidadUsuario(self):
		return self.idPrivacidadUsuario
	def setIdPrivacidadUsuario(self,idPrivacidadUsuario):
		self.idPrivacidadUsuario = idPrivacidadUsuario



	#Getters y Setters de mostrarCorreo

	def getMostrarCorreo(self):
		return self.mostrarCorreo
	def setMostrarCorreo(self,mostrarCorreo):
		self.mostrarCorreo = mostrarCorreo



	#Getters y Setters de mostrarOrgPropias

	def getMostrarOrgPropias(self):
		return self.mostrarOrgPropias
	def setMostrarOrgPropias(self,mostrarOrgPropias):
		self.mostrarOrgPropias = mostrarOrgPropias



	#Getters y Setters de mostrarOrgPertenece

	def getMostrarOrgPertenece(self):
		return self.mostrarOrgPertenece
	def setMostrarOrgPertenece(self,mostrarOrgPertenece):
		self.mostrarOrgPertenece = mostrarOrgPertenece



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




#Autogenerado: 04/30/17 16:16:30