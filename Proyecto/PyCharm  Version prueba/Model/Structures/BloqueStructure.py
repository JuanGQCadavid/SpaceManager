# -*- coding: cp1252 -*- 
class Bloque(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Bloque
	'''
	#Constructor con paso de parametros 
	def __init__(self, idBloque= None, idSede= None, idOrgCreador= None, idOrgConsecutivo= None, nombreBloque= None, idUsuarioEncargado= None, descripcionBloqe= None, estado= None, fechaEstado= None, fechaCreacion= None):
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrgCreador = idOrgCreador 
		self.idOrgConsecutivo = idOrgConsecutivo 
		self.nombreBloque = nombreBloque 
		self.idUsuarioEncargado = idUsuarioEncargado 
		self.descripcionBloqe = descripcionBloqe 
		self.estado = estado 
		self.fechaEstado = fechaEstado 
		self.fechaCreacion = fechaCreacion 


	#Getters y Setters de idBloque

	def getIdBloque(self):
		return self.idBloque
	def setIdBloque(self,idBloque):
		self.idBloque = idBloque



	#Getters y Setters de idSede

	def getIdSede(self):
		return self.idSede
	def setIdSede(self,idSede):
		self.idSede = idSede



	#Getters y Setters de idOrgCreador

	def getIdOrgCreador(self):
		return self.idOrgCreador
	def setIdOrgCreador(self,idOrgCreador):
		self.idOrgCreador = idOrgCreador



	#Getters y Setters de idOrgConsecutivo

	def getIdOrgConsecutivo(self):
		return self.idOrgConsecutivo
	def setIdOrgConsecutivo(self,idOrgConsecutivo):
		self.idOrgConsecutivo = idOrgConsecutivo



	#Getters y Setters de nombreBloque

	def getNombreBloque(self):
		return self.nombreBloque
	def setNombreBloque(self,nombreBloque):
		self.nombreBloque = nombreBloque



	#Getters y Setters de idUsuarioEncargado

	def getIdUsuarioEncargado(self):
		return self.idUsuarioEncargado
	def setIdUsuarioEncargado(self,idUsuarioEncargado):
		self.idUsuarioEncargado = idUsuarioEncargado



	#Getters y Setters de descripcionBloqe

	def getDescripcionBloqe(self):
		return self.descripcionBloqe
	def setDescripcionBloqe(self,descripcionBloqe):
		self.descripcionBloqe = descripcionBloqe



	#Getters y Setters de estado

	def getEstado(self):
		return self.estado
	def setEstado(self,estado):
		self.estado = estado



	#Getters y Setters de fechaEstado

	def getFechaEstado(self):
		return self.fechaEstado
	def setFechaEstado(self,fechaEstado):
		self.fechaEstado = fechaEstado



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion




#Autogenerado: 05/09/17 23:48:59