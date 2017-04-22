from Model.DBFunctions import DbFunctions
from Model.Structures.RedessocialesStructure import Redessociales
import MySQLdb

class DBSocialNetwork(DbFunctions):

    def generarPrimarykey(self, socialNetworkList):
        primaryKey = socialNetworkList[0]

        if (socialNetworkList[1] == None and socialNetworkList[2] == 0
            and socialNetworkList[3] == 0 and socialNetworkList[4] == 0
            and socialNetworkList[5] == 0):

            primaryKey = "GenericNull"

            return primaryKey

        else:
            return primaryKey

    def generarRedessocialesObject(self, socialNetworkList):

        primaryKey = self.generarPrimarykey(socialNetworkList)

        # Creamos el Objeto por el constructor
        redessocialesNewObecjt = Redessociales(primaryKey,
                                                socialNetworkList[1],
                                                socialNetworkList[2],
                                                socialNetworkList[3],
                                                socialNetworkList[4],
                                                socialNetworkList[5])
        # Retornamos el objeto
        return redessocialesNewObecjt

    def insertRedessociales(self, redessocialesObject):

        # Si el objeto es un generic, simplemnete lo devolvemos como est, si no creamos el registro.

        if redessocialesObject.getIdRedesSociales == "GenericNull":

            return redessocialesObject

        else:

            # Buscar si hay un atributo con la mismas carateristicas
            values = "'{}','{}','{}','{}','{}','{}'".format(redessocialesObject.getIdRedesSociales(),
                                                  redessocialesObject.getFaceBook(),
                                                  redessocialesObject.getTwitter(),
                                                  redessocialesObject.getLinkedin(),
                                                  redessocialesObject.getInstagram(),
                                                  redessocialesObject.getGoogle()
                                                  )
            result = "ERROR"
            try:
                result = self.insertInto("redessociales", values)
                return redessocialesObject

            except(MySQLdb.IntegrityError), e:

                result = "ERROR: Tenemos problema de Integridad"
                return None


'''''''''
joder = DBSocialNetwork()

Objeto = joder.generarRedessocialesObject(("jquiro12","Face","Twitter","Linkedin","Instagram","Google"))

print joder.insertRedessociales(Objeto)
'''''''''