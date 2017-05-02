# -*- coding: cp1252 -*- 
class Organizacion(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Organizacion
	'''
	#Constructor con paso de parametros 
	def __init__(self, idOrganizacion= None, nombre_Org= None, numero_Sedes= None, descripcion_Org= None, idPermisosEstandar= None, idRedesSociales= None, telefonoOrg= None, estadoOrg= None):
		self.idOrganizacion = idOrganizacion 
		self.nombre_Org = nombre_Org 
		self.numero_Sedes = numero_Sedes 
		self.descripcion_Org = descripcion_Org 
		self.idPermisosEstandar = idPermisosEstandar 
		self.idRedesSociales = idRedesSociales 
		self.telefonoOrg = telefonoOrg 
		self.estadoOrg = estadoOrg 


	#Getters y Setters de idOrganizacion

	def getIdOrganizacion(self):
		return self.idOrganizacion
	def setIdOrganizacion(self,idOrganizacion):
		self.idOrganizacion = idOrganizacion



	#Getters y Setters de nombre_Org

	def getNombre_Org(self):
		return self.nombre_Org
	def setNombre_Org(self,nombre_Org):
		self.nombre_Org = nombre_Org



	#Getters y Setters de numero_Sedes

	def getNumero_Sedes(self):
		return self.numero_Sedes
	def setNumero_Sedes(self,numero_Sedes):
		self.numero_Sedes = numero_Sedes



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




#Autogenerado: 04/30/17 16:16:30