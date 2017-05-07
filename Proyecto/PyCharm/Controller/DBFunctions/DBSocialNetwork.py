from Model.DBFunctions import DbFunctions
from Model.Structures.RedessocialesStructure import Redessociales
import mysql



class DBSocialNetwork(DbFunctions):

    def generarPrimarykey(self, socialNetworkList):
        print 'Redes Sociales DB - generarPrimarykey'

        primaryKey = socialNetworkList[0]

        if (socialNetworkList[1] == None and socialNetworkList[2] == None
            and socialNetworkList[3] == None and socialNetworkList[4] == None
            and socialNetworkList[5] == None):

            primaryKey = "GenericNull"

            return primaryKey

        else:
            return primaryKey

    def generarRedessocialesObject(self, socialNetworkList):
        print 'Redes Sociales DB - generarRedessocialesObject'
        primaryKey = self.generarPrimarykey(socialNetworkList)

        # Creamos el Objeto por el constructor
        redessocialesNewObecjt = Redessociales(idRedesSociales= primaryKey, faceBook= socialNetworkList[1],
                                               twitter= socialNetworkList[2], linkedin= socialNetworkList[3],
                                               instagram= socialNetworkList[4], google= socialNetworkList[5])
        # Retornamos el objeto
        return redessocialesNewObecjt

    def insertRedessociales(self, redessocialesObject) :
        print 'Redes Sociales DB - insertRedessociales'

        # Si el objeto es un generic, simplemnete lo devolvemos como est, si no creamos el registro.

        if redessocialesObject.getIdRedesSociales() == "GenericNull" :

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
                result = self.insertInto("RedesSociales", values)
                return redessocialesObject

            except(mysql.connector.errors.IntegrityError), e:
                result = "ERROR: Tenemos problema de Integridad En INSERTAR Social NETWORk"
                return None

    def actualizarRedes(self,listaPropiedades):
        print 'Redes Sociales DB - actualizarRedes'
        sets = "FaceBook = '{}',Twitter = '{}', Linkedin = '{}',Instagram = '{}', Google = '{}'".format(listaPropiedades[1],
                                                                                                        listaPropiedades[2],
                                                                                                        listaPropiedades[3],
                                                                                                        listaPropiedades[4],
                                                                                                        listaPropiedades[5])

        conditions = "idRedesSociales = '{}'".format(listaPropiedades[0])

        return self.update('RedesSociales',sets,conditions)




'''''''''
joder = DBSocialNetwork()

Objeto = joder.generarRedessocialesObject(("jquiro12","Face","Twitter","Linkedin","Instagram","Google"))

print joder.insertRedessociales(Objeto)
'''''''''
