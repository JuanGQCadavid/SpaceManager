from Model.DBFunctions import DbFunctions
from Model.Structures.OrganizacionStructure import Organizacion
from Model.Structures.PermisosStructure import Permisos
import MySQLdb

class DbFunctionOrganizacion (DbFunctions) :

    def FormarOrgObject (self, orgList) :
        #Creando objeto
        nuevaOrg = Organizacion()

        #Inicializando atributos
        nuevaOrg.setIdOrganizacion(orgList[0])
        nuevaOrg.setNombre_Org(orgList[1])
        nuevaOrg.setNumero_Sedes(orgList[2])
        nuevaOrg.setDescripcion_Org(orgList[3])
        nuevaOrg.setIdPermisosEstandar(orgList[4])
        nuevaOrg.setIdRedesSociales(orgList[5])
        nuevaOrg.setTelefonoOrg(orgList[6])

        return nuevaOrg

    def insertOrg (self, nuevaOrg) :
        values = "'{}','{}',{},'{}','{}','{}','{}'".format(nuevaOrg.getIdOrganizacion(),
                                                      nuevaOrg.getNombre_Org(),
                                                      nuevaOrg.getNumero_Sedes(),
                                                      nuevaOrg.getDescripcion_Org(),
                                                      nuevaOrg.getIdPermisosEstandar(),
                                                      nuevaOrg.getIdRedesSociales(),
                                                      nuevaOrg.getTelefonoOrg()
                                                      )
        result = "ERROR"
        try:
            result = self.insertInto("organizacion", values)
            return nuevaOrg

        except (MySQLdb.IntegrityError) :
            result = "ERROR: Tenemos problema de Integridad En INSERTAR Organizacion"
            print result
            raise
            return None


    def cambiarUsuarioEncargado (self, OrgObject, Usuario) :
        OrgObject.setIdUsuarioEncargado(Usuario.getIdUsuario());
        condicion = "idOrganizacion = {}".format(OrgObject.getIdOrganizacion)
        return self.up("Organizacion", "IdUsuarioEncargado", Usuario.getIdUsuario, condicion)

    def configPermisosEstandar (self, list) :
        pass

    def objetInsert(self,orgList):
        return self.insertOrg(self.FormarOrgObject(orgList))

    def obtenerOrg(self,primaryKey):
        respuesta = self.selectWhere("*","Organizacion","idOrganizacion = '{}'".format(primaryKey))

        if respuesta == None:
            return None
        else:
            return respuesta[0]

    def obtenerUsuarioComoObject(self,primaryKey):
        return self.generarObjeto(self.obtenerOrgUser(primaryKey))