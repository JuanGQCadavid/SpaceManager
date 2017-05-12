# -*- coding: cp1252 -*- 
class Organizacion(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Organizacion
	'''
	#Constructor con paso de parametros 
	def __init__(self, idUsuarioCreador= None, consecutivoOrg= None, nombre_Org= None, descripcion_Org= None, idPermisosEstandar= None, idRedesSociales= None, telefonoOrg= None, estadoOrg= None, fechaCreacion= None, tipoEnroll= None):
		self.idUsuarioCreador = idUsuarioCreador 
		self.consecutivoOrg = consecutivoOrg 
		self.nombre_Org = nombre_Org 
		self.descripcion_Org = descripcion_Org 
		self.idPermisosEstandar = idPermisosEstandar 
		self.idRedesSociales = idRedesSociales 
		self.telefonoOrg = telefonoOrg 
		self.estadoOrg = estadoOrg 
		self.fechaCreacion = fechaCreacion 
		self.tipoEnroll = tipoEnroll 


	#Getters y Setters de idUsuarioCreador

	def getIdUsuarioCreador(self):
		return self.idUsuarioCreador
	def setIdUsuarioCreador(self,idUsuarioCreador):
		self.idUsuarioCreador = idUsuarioCreador



	#Getters y Setters de consecutivoOrg

	def getConsecutivoOrg(self):
		return self.consecutivoOrg
	def setConsecutivoOrg(self,consecutivoOrg):
		self.consecutivoOrg = consecutivoOrg



	#Getters y Setters de nombre_Org

	def getNombre_Org(self):
		return self.nombre_Org
	def setNombre_Org(self,nombre_Org):
		self.nombre_Org = nombre_Org



	#Getters y Setters de descripcion_Org

	def getDescripcion_Org(self):
		return self.descripcion_Org
	def setDescripcion_Org(self,descripcion_Org):
		self.descripcion_Org = descripcion_Org



	#Getters y Setters de idPermisosEstandar

	def getIdPermisosEstandar(self):
		return self.idPermisosEstandar
	def setIdPermisosEstandar(self,idPermisosEstandar):
		self.idPermisosEstandar = idPermisosEstandar



	#Getters y Setters de idRedesSociales

	def getIdRedesSociales(self):
		return self.idRedesSociales
	def setIdRedesSociales(self,idRedesSociales):
		self.idRedesSociales = idRedesSociales



	#Getters y Setters de telefonoOrg

	def getTelefonoOrg(self):
		return self.telefonoOrg
	def setTelefonoOrg(self,telefonoOrg):
		self.telefonoOrg = telefonoOrg



	#Getters y Setters de estadoOrg

	def getEstadoOrg(self):
		return self.estadoOrg
	def setEstadoOrg(self,estadoOrg):
		self.estadoOrg = estadoOrg



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion



	#Getters y Setters de tipoEnroll

	def getTipoEnroll(self):
		return self.tipoEnroll
	def setTipoEnroll(self,tipoEnroll):
		self.tipoEnroll = tipoEnroll




#Autogenerado: 05/09/17 23:48:59