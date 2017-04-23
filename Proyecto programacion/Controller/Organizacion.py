from Model.DBFunctions import DbFunctions
from Model.Structures.OrganizacionStructure import Organizacion

import MySQLdb
from Model.Structures.UsuarioStructure import Usuario
class DbFunctionOrganizacion(DbFunctions) :

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

    def cambiarUsuarioEncargado (self, OrgObject, Usuario) :
        OrgObject.setIdUsuarioEncargado(Usuario.getIdUsuario());
        condicion = "idOrganizacion = {}".format(OrgObject.getIdOrganizacion)
        return self.up("Organizacion", "IdUsuarioEncargado", Usuario.getIdUsuario, condicion)


