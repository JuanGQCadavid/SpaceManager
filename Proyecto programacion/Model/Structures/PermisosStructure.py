# -*- coding: cp1252 -*- 
class Permisos(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Permisos
	'''
	#Constructor con paso de parametros 
	def __init__(self, idPermisos = None, p_Reserva = None, p_Nivel = None, p_Bloque = None, p_Sede = None, p_Org = None, pC_B = None, pC_S = None, pC_N= None, pC_E= None, p_Encargado= None):
		self.idPermisos = idPermisos 
		self.p_Reserva = p_Reserva 
		self.p_Nivel = p_Nivel 
		self.p_Bloque = p_Bloque 
		self.p_Sede = p_Sede 
		self.p_Org = p_Org 
		self.pC_B = pC_B 
		self.pC_S = pC_S 
		self.pC_N = pC_N 
		self.pC_E = pC_E 
		self.p_Encargado = p_Encargado 


	#Getters y Setters de idPermisos

	def getIdPermisos(self):
		return self.idPermisos
	def setIdPermisos(self,idPermisos):
		self.idPermisos = idPermisos



	#Getters y Setters de p_Reserva

	def getP_Reserva(self):
		return self.p_Reserva
	def setP_Reserva(self,p_Reserva):
		self.p_Reserva = p_Reserva



	#Getters y Setters de p_Nivel

	def getP_Nivel(self):
		return self.p_Nivel
	def setP_Nivel(self,p_Nivel):
		self.p_Nivel = p_Nivel



	#Getters y Setters de p_Bloque

	def getP_Bloque(self):
		return self.p_Bloque
	def setP_Bloque(self,p_Bloque):
		self.p_Bloque = p_Bloque



	#Getters y Setters de p_Sede

	def getP_Sede(self):
		return self.p_Sede
	def setP_Sede(self,p_Sede):
		self.p_Sede = p_Sede



	#Getters y Setters de p_Org

	def getP_Org(self):
		return self.p_Org
	def setP_Org(self,p_Org):
		self.p_Org = p_Org



	#Getters y Setters de pC_B

	def getPC_B(self):
		return self.pC_B
	def setPC_B(self,pC_B):
		self.pC_B = pC_B



	#Getters y Setters de pC_S

	def getPC_S(self):
		return self.pC_S
	def setPC_S(self,pC_S):
		self.pC_S = pC_S



	#Getters y Setters de pC_N

	def getPC_N(self):
		return self.pC_N
	def setPC_N(self,pC_N):
		self.pC_N = pC_N



	#Getters y Setters de pC_E

	def getPC_E(self):
		return self.pC_E
	def setPC_E(self,pC_E):
		self.pC_E = pC_E



	#Getters y Setters de p_Encargado

	def getP_Encargado(self):
		return self.p_Encargado
	def setP_Encargado(self,p_Encargado):
		self.p_Encargado = p_Encargado




#Autogenerado: 04/22/17 10:35:27
