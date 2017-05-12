# -*- coding: cp1252 -*- 
class Reservas_mias(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Reservas_mias
	'''
	#Constructor con paso de parametros 
	def __init__(self, usuario_ID= None, organizacion= None, sede= None, bloque= None, nivel= None, espacio= None, estado= None):
		self.usuario_ID = usuario_ID 
		self.organizacion = organizacion 
		self.sede = sede 
		self.bloque = bloque 
		self.nivel = nivel 
		self.espacio = espacio 
		self.estado = estado 


	#Getters y Setters de usuario_ID

	def getUsuario_ID(self):
		return self.usuario_ID
	def setUsuario_ID(self,usuario_ID):
		self.usuario_ID = usuario_ID



	#Getters y Setters de organizacion

	def getOrganizacion(self):
		return self.organizacion
	def setOrganizacion(self,organizacion):
		self.organizacion = organizacion



	#Getters y Setters de sede

	def getSede(self):
		return self.sede
	def setSede(self,sede):
		self.sede = sede



	#Getters y Setters de bloque

	def getBloque(self):
		return self.bloque
	def setBloque(self,bloque):
		self.bloque = bloque



	#Getters y Setters de nivel

	def getNivel(self):
		return self.nivel
	def setNivel(self,nivel):
		self.nivel = nivel



	#Getters y Setters de espacio

	def getEspacio(self):
		return self.espacio
	def setEspacio(self,espacio):
		self.espacio = espacio



	#Getters y Setters de estado

	def getEstado(self):
		return self.estado
	def setEstado(self,estado):
		self.estado = estado




#Autogenerado: 05/09/17 23:48:59