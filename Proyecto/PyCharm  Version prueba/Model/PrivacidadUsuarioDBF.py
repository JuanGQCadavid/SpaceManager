from Model.DBConection import DataBaseConection
from Model.Structures.PrivacidadusuarioStructure import Privacidadusuario

class PrivacidadUsuarioDBF(DataBaseConection):

    def generarPrivacidadObject(self, privacidadList):

         # Creamos el Objeto por el constructor
        privacidadNewObecjt = Privacidadusuario(idPrivacidadUsuario= privacidadList[0], mostrarCorreo= privacidadList[1],
                                                mostrarOrgPropias=  privacidadList[2], mostrarOrgPertenece= privacidadList[3],
                                                mostrarRedesSociales= privacidadList[4], mostrarTelefono= privacidadList[5])
        #Retornamos el objeto
        return privacidadNewObecjt

    def insertarPrivacidad(self,MostrarCorreo,MostrarOrgPropias ,MostrarOrgPertenece ,MostrarRedesSociales ,MostrarTelefono):
        return self.run_query("SELECT insertar_Privacidad({},{},{},{},{})".format(MostrarCorreo,MostrarOrgPropias,
                                                                                      MostrarOrgPertenece,MostrarRedesSociales,
                                                                                      MostrarTelefono))[0][0]

    def consultarPrivacidad(self, idPrivacidadUsuario):
        return self.generarPrivacidadObject(self.run_query("CALL mostrarPrivacidadU('{}') ".format(idPrivacidadUsuario))[0][0])


    def editarPrivacidad(self, idPrivacidadUsuario,MostrarCorreo,MostrarOrgPropias ,
                         MostrarOrgPertenece ,MostrarRedesSociales ,MostrarTelefono):
        return self.run_query("SELECT  modificar_PrivacidadUsuario('{}',{},{},{},{},{}) ".format(idPrivacidadUsuario,
                                                                                                 MostrarCorreo,
                                                                                                 MostrarOrgPropias,
                                                                                                 MostrarOrgPertenece,
                                                                                                 MostrarRedesSociales,
                                                                                                 MostrarTelefono))[0][0]

clase = PrivacidadUsuarioDBF()
print clase.insertarPrivacidad(1,1,0,1,1)