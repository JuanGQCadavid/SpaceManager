from Model.DBConection import DataBaseConection
from Model.Structures.RedessocialesStructure import Redessociales

class RedesSocialesDBF(DataBaseConection):

    def generarRedessocialesObject(self, redesSocialesLista):
        print 'Redes Sociales DB - generarRedessocialesObject'

        # Creamos el Objeto por el constructor
        redessocialesNewObecjt = Redessociales(idRedesSociales= redesSocialesLista[0], faceBook= redesSocialesLista[1],
                                               twitter= redesSocialesLista[2], linkedin= redesSocialesLista[3],
                                               instagram= redesSocialesLista[4], google= redesSocialesLista[5])
        # Retornamos el objeto
        return redessocialesNewObecjt


    def insertarRedesSociales(self,idRedesSociales,FaceBook, Twitter, Linkedin, Instagram, Google):
        return self.run_query("SELECT insertar_RedesSociales('{}','{}','{}','{}','{}','{}')".format(idRedesSociales,FaceBook, Twitter,
                                                                                                     Linkedin,Instagram,Google))

    def consultarRedesSociales(self, idRedesSociales):
        return self.generarRedessocialesObject(self.run_query("CALL mostrar_RedesSociales('{}') ".format(idRedesSociales))[0][0])

    def editarRedesSociales(self,redessocialesObject):
        return self.run_query("SELECT  modificar_RedesSociales('{}','{}','{}','{}','{}','{}') ".format(redessocialesObject.getIdRedesSociales(),
                                                  redessocialesObject.getFaceBook(),
                                                  redessocialesObject.getTwitter(),
                                                  redessocialesObject.getLinkedin(),
                                                  redessocialesObject.getInstagram(),
                                                  redessocialesObject.getGoogle()))[0][0]



clase = RedesSocialesDBF()

print clase.insertarRedesSociales('Ermosa','FB','FB','FB','FB','FB')
