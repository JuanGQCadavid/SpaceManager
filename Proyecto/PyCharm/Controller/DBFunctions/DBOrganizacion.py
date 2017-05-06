from Model.DBFunctions import DbFunctions
from Model.Structures.OrganizacionStructure import Organizacion

import mysql

class DbFunctionOrganizacion (DbFunctions) :

    def FormarOrgObject (self, orgList) :
        print 'organizacion DB - FormarOrgObject'
        #Creando objeto
        nuevaOrg = Organizacion(idUsuarioCreador = orgList[0],consecutivoOrg =orgList[1],
                                nombre_Org = orgList[2], descripcion_Org = orgList[3],
                                idPermisosEstandar = orgList[4], idRedesSociales = orgList[5],
                                telefonoOrg = orgList[6],estadoOrg  = orgList[7],
                                fechaCreacion = orgList[8]
                                )

        return nuevaOrg

    def insertOrg (self, nuevaOrg) :
        print 'organizacion DB - insertOrg'
        values = "'{}',{},'{}','{}','{}','{}','{}',{},'{}'".format(nuevaOrg.getIdUsuarioCreador(),
                                                              nuevaOrg.getConsecutivoOrg(),
                                                              nuevaOrg.getNombre_Org(),
                                                              nuevaOrg.getDescripcion_Org(),
                                                              nuevaOrg.getIdPermisosEstandar(),
                                                              nuevaOrg.getIdRedesSociales(),
                                                              nuevaOrg.getTelefonoOrg(),
                                                              nuevaOrg.getEstadoOrg(),
                                                              nuevaOrg.getFechaCreacion())

        try:
            result = self.insertInto("Organizacion", values)
            return nuevaOrg

        except (mysql.connector.errors.IntegrityError) :
            print "ERROR: Tenemos problema de Integridad En INSERTAR Organizacion"

    def configRedesSociales (self, pkRedesSociales, pkOrgCreador, pkOrgconsecutivo) :
        print 'organizacion DB - configRedesSociales'
        sets = "idRedesSociales = '{}'".format(pkRedesSociales)
        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(pkOrgCreador,pkOrgconsecutivo)

        return self.update('Organizacion', sets, condition)

    def cerrarOrg(self,pkOrgCreador, pkOrgconsecutivo):
        sets = 'estadoOrg = 0'
        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(pkOrgCreador,pkOrgconsecutivo)
        return self.update('Organizacion',sets,condition)

    def abrirOrg(self,pkOrgCreador, pkOrgconsecutivo):
        sets = 'estadoOrg = 1'
        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(pkOrgCreador,pkOrgconsecutivo)
        return self.update('Organizacion',sets,condition)

    def configPermisosEstandar (self, pkPermisosEstandar, pkOrgCreador, pkOrgconsecutivo) :
        print 'organizacion DB - configPermisosEstandar'

        sets = "idPermisosEstandar = '{}'".format(pkPermisosEstandar)
        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(pkOrgCreador,pkOrgconsecutivo)

        return self.update('Organizacion', sets, condition)

    def objetInsert(self, orgList) :
        print 'organizacion DB - objetInsert'
        return self.insertOrg(self.FormarOrgObject(orgList))

    def obtenerOrg(self,idCreador,consecutivo) :
        print 'organizacion DB - obtenerOrg'

        respuesta = self.selectWhere("*","Organizacion","idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(idCreador,consecutivo))

        if not(respuesta == None):
            return self.FormarOrgObject(respuesta[0])

    def obtenerConsecutivo(self,pkUser):
        print 'organizacion DB - obtenerConsecutivo'

        query = "select obtenerConsecutivo('{}')".format(pkUser)
        return (self.run_query(query))[0]

    def actualizarRow(self, pkOrgCreador, pkOrgconsecutivo, rowName, rowValue):
        print 'organizacion DB - actualizarFks'

        sets = "{} = '{}'".format(rowName,rowValue)

        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(pkOrgCreador, pkOrgconsecutivo)

        return self.update('Organizacion', sets, condition)

    def editarDatosbasicos(self,listaDatosBasicos, pkOrgCreador, pkOrgconsecutivo):
        print 'organizacion DB - editarDatosbasicos'

        sets = "nombre_Org = '{}', descripcion_Org = '{}', telefonoOrg = '{}'".format(listaDatosBasicos[0],
                                                                                      listaDatosBasicos[1],
                                                                                      listaDatosBasicos[2])
        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(pkOrgCreador, pkOrgconsecutivo)

        return self.update('Organizacion', sets, condition)