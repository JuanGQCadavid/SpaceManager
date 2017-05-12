# -*- coding: cp1252 -*- 
class Org_administradores(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Org_administradores
	'''
	#Constructor con paso de parametros 
	def __init__(self, usuario_Creador= None, contador= None, encargado= None, jefe= None, sede= None, bloque= None, nivel= None, identificador= None):
		self.usuario_Creador = usuario_Creador 
		self.contador = contador 
		self.encargado = encargado 
		self.jefe = jefe 
		self.sede = sede 
		self.bloque = bloque 
		self.nivel = nivel 
		self.identificador = identificador 


	#Getters y Setters de usuario_Creador

	def getUsuario_Creador(self):
		return self.usuario_Creador
	def setUsuario_Creador(self,usuario_Creador):
		self.usuario_Creador = usuario_Creador



	#Getters y Setters de contador

	def getContador(self):
		return self.contador
	def setContador(self,contador):
		self.contador = contador



	#Getters y Setters de encargado

	def getEncargado(self):
		return self.encargado
	def setEncargado(self,encargado):
		self.encargado = encargado



	#Getters y Setters de jefe

	def getJefe(self):
		return self.jefe
	def setJefe(self,jefe):
		self.jefe = jefe



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



	#Getters y Setters de identificador

	def getIdentificador(self):
		return self.identificador
	def setIdentificador(self,identificador):
		self.identificador = identificador




#Autogenerado: 05/09/17 23:48:59