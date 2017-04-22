from Model.DBFunctions import DbFunctions
from Model.Structures.PrivacidadusuarioStructure import Privacidadusuario
import MySQLdb
class DBFunctionPermisoPrivacidad(DbFunctions):



    def generarPrimarykey(self,privacidadList):
        primaryKey = privacidadList[0]

        if ( privacidadList[1] == 0 and privacidadList[2] == 0
            and privacidadList[3] == 0 and privacidadList[4] == 0
            and privacidadList[5] == 0):

            primaryKey = "GenericF"

            return primaryKey

        elif( privacidadList[1] != 0 and privacidadList[2] != 0
            and privacidadList[3] != 0 and privacidadList[4] != 0
            and privacidadList[5] != 0):

            primaryKey = "GenericT"

            return primaryKey
        else:
            return primaryKey



    def generarPrivacidadObject(self, privacidadList):

        primaryKey = self.generarPrimarykey(privacidadList)



        # Creamos el Objeto por el constructor
        privacidadNewObecjt = Privacidadusuario(primaryKey,
                                                privacidadList[1],
                                                privacidadList[2],
                                                privacidadList[3],
                                                privacidadList[4],
                                                privacidadList[5])
        #Retornamos el objeto
        return privacidadNewObecjt

    def insertPermisosPrivacidad(self,permisosPrivacidadObject):

        #Si el objeto es un generic, simplemnete lo devolvemos como est, si no creamos el registro.

        if permisosPrivacidadObject.getIdPrivacidadUsuario == "GenericT" or permisosPrivacidadObject.getIdPrivacidadUsuario == "GenericF" :

            return permisosPrivacidadObject

        else:

            #Buscar si hay un atributo con la mismas carateristicas
            values ="'{}',{},{},{},{},{}".format(permisosPrivacidadObject.getIdPrivacidadUsuario(),
                                                      permisosPrivacidadObject.getMostrarCorreo(),
                                                      permisosPrivacidadObject.getMostrarOrgPropias(),
                                                      permisosPrivacidadObject.getMostrarOrgPertenece(),
                                                      permisosPrivacidadObject.getMostrarRedesSociales(),
                                                      permisosPrivacidadObject.getMostrarTelefono()
                                                      )
            result = "ERROR"
            try:
                result = self.insertInto("privacidadusuario",values)
                return permisosPrivacidadObject

            except(MySQLdb.IntegrityError),e:

                result = "ERROR: Tenemos problema de Integridad"
                return None



'''''''''
joder = DBFunctionPermisoPrivacidad()

Objeto = joder.generarPrivacidadObject(("jquiro12556",1,1,1,1,1,1))

print joder.insertPermisosPrivacidad(Objeto)
'''''''''