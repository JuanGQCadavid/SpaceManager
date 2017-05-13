# -*- coding: cp1252 -*- 
class Nivel_bloques_sede_org(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Nivel_bloques_sede_org
	'''
	#Constructor con paso de parametros 
	def __init__(self, idNivel= None, idBloque= None, idSede= None, idOrgCreador= None, idOrgConsecutivo= None, numeroNivel= None, encargado= None, iF(EspaciosPublicos.tieneBanos,'Si', 'No')= None, iF(EspaciosPublicos.tieneCocineta,'Si', 'No')= None, iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')= None, descripcionNivel= None, fechaCreacion= None):
		self.idNivel = idNivel 
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrgCreador = idOrgCreador 
		self.idOrgConsecutivo = idOrgConsecutivo 
		self.numeroNivel = numeroNivel 
		self.encargado = encargado 
		self.iF(EspaciosPublicos.tieneBanos,'Si', 'No') = iF(EspaciosPublicos.tieneBanos,'Si', 'No') 
		self.iF(EspaciosPublicos.tieneCocineta,'Si', 'No') = iF(EspaciosPublicos.tieneCocineta,'Si', 'No') 
		self.iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No') = iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No') 
		self.descripcionNivel = descripcionNivel 
		self.fechaCreacion = fechaCreacion 


	#Getters y Setters de idNivel

	def getIdNivel(self):
		return self.idNivel
	def setIdNivel(self,idNivel):
		self.idNivel = idNivel



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



	#Getters y Setters de numeroNivel

	def getNumeroNivel(self):
		return self.numeroNivel
	def setNumeroNivel(self,numeroNivel):
		self.numeroNivel = numeroNivel



	#Getters y Setters de encargado

	def getEncargado(self):
		return self.encargado
	def setEncargado(self,encargado):
		self.encargado = encargado



	#Getters y Setters de iF(EspaciosPublicos.tieneBanos,'Si', 'No')

	def getIF(EspaciosPublicos.tieneBanos,'Si', 'No')(self):
		return self.iF(EspaciosPublicos.tieneBanos,'Si', 'No')
	def setIF(EspaciosPublicos.tieneBanos,'Si', 'No')(self,iF(EspaciosPublicos.tieneBanos,'Si', 'No')):
		self.iF(EspaciosPublicos.tieneBanos,'Si', 'No') = iF(EspaciosPublicos.tieneBanos,'Si', 'No')



	#Getters y Setters de iF(EspaciosPublicos.tieneCocineta,'Si', 'No')

	def getIF(EspaciosPublicos.tieneCocineta,'Si', 'No')(self):
		return self.iF(EspaciosPublicos.tieneCocineta,'Si', 'No')
	def setIF(EspaciosPublicos.tieneCocineta,'Si', 'No')(self,iF(EspaciosPublicos.tieneCocineta,'Si', 'No')):
		self.iF(EspaciosPublicos.tieneCocineta,'Si', 'No') = iF(EspaciosPublicos.tieneCocineta,'Si', 'No')



	#Getters y Setters de iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')

	def getIF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')(self):
		return self.iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')
	def setIF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')(self,iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')):
		self.iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No') = iF(EspaciosPublicos.tieneSalaEstar,'Si', 'No')



	#Getters y Setters de descripcionNivel

	def getDescripcionNivel(self):
		return self.descripcionNivel
	def setDescripcionNivel(self,descripcionNivel):
		self.descripcionNivel = descripcionNivel



	#Getters y Setters de fechaCreacion

	def getFechaCreacion(self):
		return self.fechaCreacion
	def setFechaCreacion(self,fechaCreacion):
		self.fechaCreacion = fechaCreacion




#Autogenerado: 05/09/17 23:48:59