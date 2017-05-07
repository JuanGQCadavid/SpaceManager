from Model.DBFunctions import DbFunctions
from Model.Structures.OrgusuarioStructure import Orgusuario
import time
import mysql


class DBOrgUser(DbFunctions):
    def generarObjeto(self,orgList):
        print 'Org user Db - generarObjeto'

        objectOrgUsuario = Orgusuario(idOrgUsuario = orgList[0],idOrgUsuarioCreador = orgList[1],
                                      idOrgContador = orgList[2],idUsuario = orgList[3],
                                      idPermisos = orgList[4], nombrePilaUser = orgList[5],
                                      estadoUsuario = orgList[6], fechaEstado = orgList[7])
        return objectOrgUsuario

    def insertOrgUser(self,objetoOrgUser):
        print 'Org user Db - insertOrgUser'
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
        print 'Org user Db - objectInsert'
        return self.insertOrgUser(self.generarObjeto(orgList))

    def cambiarEstado(self,idOrguser,estadoNuevo):
        print 'Org user Db - cambiarEstado'

        fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")

        sets = "estadoUsuario = {}, fechaEstado = '{}'".format(estadoNuevo,fechaActual)

        condicion = "idOrgUsuario = '{}'".format(idOrguser)

        return self.update("OrgUsuario", sets, condicion)

    def obtenerOrgUser(self,primaryKey):
        print 'Org user Db - obtenerOrgUser'
        respuesta = self.selectWhere("*","OrgUsuario","idOrgUsuario = '{}'".format(primaryKey))

        if respuesta == None:
            return None
        else:
            return respuesta[0]

    def obtenerUsuarioOrgComoObject(self,primaryKey):
        print 'Org user Db - obtenerUsuarioOrgComoObject'
        return self.generarObjeto(self.obtenerOrgUser(primaryKey))

    def actualizarOrgUserDB(self,idOrguser,idPermisos,nombrePila,fechaActual):
        print 'Org user Db - actualizarOrgUserDB'
        sets = "idPermisos = '{}', nombrePilaUser = '{}', estadoUsuario = 1, fechaEstado = '{}'".format(idPermisos,
                                                                                                        nombrePila,
                                                                                                        fechaActual)

        condition = "idOrgUsuario = '{}'".format(idOrguser)

        return self.update('OrgUsuario', sets, condition)

    def mostrarOrgPertenece(self,idUser):
        return self.selectWhere('*', 'OrgUsuario', "idUsuario = '{}'".format(idUser))

    def mostrarOrgMiembros(self,idOrgCreador,idOrgContador, estadoMostrar):

        condition= "idOrgUsuarioCreador = '{}'AND idOrgContador = {} AND estadoUsuario = {}".format(idOrgCreador,idOrgContador,estadoMostrar)

        return self.selectWhere('*', 'OrgUsuario', condition)