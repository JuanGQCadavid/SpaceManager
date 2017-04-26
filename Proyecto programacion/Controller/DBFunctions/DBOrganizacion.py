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
        nuevaOrg.setIdUsuarioEncargado(orgList[1])
        nuevaOrg.setNombre_Org(orgList[2])
        nuevaOrg.setNumero_Sedes(orgList[3])
        nuevaOrg.setDescripcion_Org(orgList[4])
        nuevaOrg.setIdPermisosEstandar(orgList[5])
        nuevaOrg.setIdRedesSociales(orgList[6])
        nuevaOrg.setTelefonoOrg(orgList[7])

        return nuevaOrg

    def insertOrg (self, nuevaOrg) :
        values = "'{}','{}','{}',{},'{}','{}','{}','{}'".format(nuevaOrg.getIdOrganizacion(),
                                                      nuevaOrg.getIdUsuarioEncargado(),
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
            return None


    def cambiarUsuarioEncargado (self, OrgObject, Usuario) :
        OrgObject.setIdUsuarioEncargado(Usuario.getIdUsuario());
        condicion = "idOrganizacion = {}".format(OrgObject.getIdOrganizacion)
        return self.up("Organizacion", "IdUsuarioEncargado", Usuario.getIdUsuario, condicion)

    def configPermisosEstandar (self, list) :
        pass

    def objetInsert(self,orgList):
        return self.insertOrg(self.FormarOrgObject(orgList))

