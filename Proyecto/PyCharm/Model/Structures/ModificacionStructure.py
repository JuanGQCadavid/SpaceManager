# -*- coding: cp1252 -*- 
class Modificacion(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Modificacion
	'''
	#Constructor con paso de parametros 
	def __init__(self, idModificacion= None, tipoModificacion= None, modOrg= None, modSede= None, modBloque= None, modNivel= None, modEspacio= None, modUsuarioEnc= None, modOrgCon= None):
		self.idModificacion = idModificacion 
		self.tipoModificacion = tipoModificacion 
		self.modOrg = modOrg 
		self.modSede = modSede 
		self.modBloque = modBloque 
		self.modNivel = modNivel 
		self.modEspacio = modEspacio 
		self.modUsuarioEnc = modUsuarioEnc 
		self.modOrgCon = modOrgCon 


	#Getters y Setters de idModificacion

	def getIdModificacion(self):
		return self.idModificacion
	def setIdModificacion(self,idModificacion):
		self.idModificacion = idModificacion



	#Getters y Setters de tipoModificacion

	def getTipoModificacion(self):
		return self.tipoModificacion
	def setTipoModificacion(self,tipoModificacion):
		self.tipoModificacion = tipoModificacion



	#Getters y Setters de modOrg

	def getModOrg(self):
		return self.modOrg
	def setModOrg(self,modOrg):
		self.modOrg = modOrg



	#Getters y Setters de modSede

	def getModSede(self):
		return self.modSede
	def setModSede(self,modSede):
		self.modSede = modSede



	#Getters y Setters de modBloque

	def getModBloque(self):
		return self.modBloque
	def setModBloque(self,modBloque):
		self.modBloque = modBloque



	#Getters y Setters de modNivel

	def getModNivel(self):
		return self.modNivel
	def setModNivel(self,modNivel):
		self.modNivel = modNivel



	#Getters y Setters de modEspacio

	def getModEspacio(self):
		return self.modEspacio
	def setModEspacio(self,modEspacio):
		self.modEspacio = modEspacio



	#Getters y Setters de modUsuarioEnc

	def getModUsuarioEnc(self):
		return self.modUsuarioEnc
	def setModUsuarioEnc(self,modUsuarioEnc):
		self.modUsuarioEnc = modUsuarioEnc



	#Getters y Setters de modOrgCon

	def getModOrgCon(self):
		return self.modOrgCon
	def setModOrgCon(self,modOrgCon):
		self.modOrgCon = modOrgCon




#Autogenerado: 05/05/17 23:15:34