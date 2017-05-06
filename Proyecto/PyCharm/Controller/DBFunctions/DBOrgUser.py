from Model.DBFunctions import DbFunctions
from Model.Structures.OrgusuarioStructure import Orgusuario
import time
import mysql
print 'Org user Db'

class DBOrgUser(DbFunctions):
    def generarObjeto(self,orgList):

        objectOrgUsuario = Orgusuario(idOrgUsuario = orgList[0],idOrgUsuarioCreador = orgList[1],
                                      idOrgContador = orgList[2],idUsuario = orgList[3],
                                      idPermisos = orgList[4], nombrePilaUser = orgList[5],
                                      estadoUsuario = orgList[6], fechaEstado = orgList[7])
        return objectOrgUsuario

    def insertOrgUser(self,objetoOrgUser):
        query = "INSERT INTO OrgUsuario VALUES ('{}','{}',{},'{}','{}','{}',{},'{}')".format(objetoOrgUser.getIdOrgUsuario(),
                                                                                          objetoOrgUser.getIdOrgUsuarioCreador(),
                                                                                          objetoOrgUser.getIdOrgContador(),
                                                                                          objetoOrgUser.getIdUsuario(),
                                                                                          objetoOrgUser.getIdPermisos(),
                                                                                          objetoOrgUser.getNombrePilaUser(),
                                                                                          objetoOrgUser.getEstadoUsuario(),
                                                                                          objetoOrgUser.getFechaEstado())

        try:
            return self.run_query(query)
        except(mysql.connector.errors.IntegrityError),e:
            print 'Error de Integridad en Insertar DB Org user'

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