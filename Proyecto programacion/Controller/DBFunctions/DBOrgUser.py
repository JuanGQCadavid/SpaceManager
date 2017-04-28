from Model.DBFunctions import DbFunctions
from Model.Structures.OrgusuarioStructure import Orgusuario
import time
class DBOrgUser(DbFunctions):
    def generarObjeto(self,orgList):

        objectOrgUsuario = Orgusuario(orgList[0],orgList[1],
                                      orgList[2],orgList[3],
                                      orgList[4],orgList[5],orgList[6])
        return objectOrgUsuario

    def insertOrgUser(self,objetoOrgUser):
        query = "INSERT INTO OrgUsuario VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(objetoOrgUser.getIdOrgUsuario(),
                                                                                          objetoOrgUser.getIdUsuario(),
                                                                                          objetoOrgUser.getIdOrg(),
                                                                                          objetoOrgUser.getIdPermisos(),
                                                                                          objetoOrgUser.getNombrePilaUser(),
                                                                                          objetoOrgUser.getEstadoUsuario(),
                                                                                          objetoOrgUser.getFechaEstado())
        self.run_query(query)

    def objectInsert(self,orgList):
        return self.insertOrgUser(self.generarObjeto(orgList))

    def cambiarEstado(self,idOrguser,estadoNuevo):
        fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")
        sets = "estadoUsuario = {}, fechaEstado = '{}'".format(estadoNuevo,fechaActual)
        condicion = "idOrgUsuario = '{}'".format(idOrguser)
        return self.update("OrgUsuario", sets, condicion)

    def obtenerOrgUser(self,primaryKey):
        respuesta = self.selectWhere("*","OrgUsuario","idOrgUsuario = '{}'".format(primaryKey))

        if respuesta == None:
            return None
        else:
            return respuesta[0]

    def obtenerUsuarioOrgComoObject(self,primaryKey):
        return self.generarObjeto(self.obtenerOrgUser(primaryKey))

    def acceptarInivitacion(self, pkOrgUser, pkPermisos):
        self.actualizarStatement('OrgUsuario','idOrgUsuario',pkOrgUser,'idPermisos',pkPermisos,0)
        self.cambiarEstado(pkOrgUser,1)
        pass