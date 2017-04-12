# -*- coding: cp1252 -*- 
class Logs(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Logs
	'''
	#Constructor con paso de parametros 
	def __init__(self, idLogs= None, fechaLog= None, usuarioLog= None, idModificacion= None):
		self.idLogs = idLogs 
		self.fechaLog = fechaLog 
		self.usuarioLog = usuarioLog 
		self.idModificacion = idModificacion 


	#Getters y Setters de idLogs

	def getIdLogs(self):
		return self.idLogs
	def setIdLogs(self,idLogs):
		self.idLogs = idLogs



	#Getters y Setters de fechaLog

	def getFechaLog(self):
		return self.fechaLog
	def setFechaLog(self,fechaLog):
		self.fechaLog = fechaLog



	#Getters y Setters de usuarioLog

	def getUsuarioLog(self):
		return self.usuarioLog
	def setUsuarioLog(self,usuarioLog):
		self.usuarioLog = usuarioLog



	#Getters y Setters de idModificacion

	def getIdModificacion(self):
		return self.idModificacion
	def setIdModificacion(self,idModificacion):
		self.idModificacion = idModificacion




#Autogenerado: 04/11/17 21:51:37