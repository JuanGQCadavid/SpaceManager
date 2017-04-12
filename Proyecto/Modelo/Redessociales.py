# -*- coding: cp1252 -*- 
class Redessociales(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Redessociales
	'''
	#Constructor con paso de parametros 
	def __init__(self, idRedesSociales= None, faceBook= None, twitter= None, linkedin= None, instagram= None, google= None):
		self.idRedesSociales = idRedesSociales 
		self.faceBook = faceBook 
		self.twitter = twitter 
		self.linkedin = linkedin 
		self.instagram = instagram 
		self.google = google 


	#Getters y Setters de idRedesSociales

	def getIdRedesSociales(self):
		return self.idRedesSociales
	def setIdRedesSociales(self,idRedesSociales):
		self.idRedesSociales = idRedesSociales



	#Getters y Setters de faceBook

	def getFaceBook(self):
		return self.faceBook
	def setFaceBook(self,faceBook):
		self.faceBook = faceBook



	#Getters y Setters de twitter

	def getTwitter(self):
		return self.twitter
	def setTwitter(self,twitter):
		self.twitter = twitter



	#Getters y Setters de linkedin

	def getLinkedin(self):
		return self.linkedin
	def setLinkedin(self,linkedin):
		self.linkedin = linkedin



	#Getters y Setters de instagram

	def getInstagram(self):
		return self.instagram
	def setInstagram(self,instagram):
		self.instagram = instagram



	#Getters y Setters de google

	def getGoogle(self):
		return self.google
	def setGoogle(self,google):
		self.google = google




#Autogenerado: 04/11/17 21:18:43