from Model.DBFunctions import DbFunctions
from Model.Structures.OrgusuarioStructure import Orgusuario

import MySQLdb
from Model.Structures.UsuarioStructure import Usuario
from Model.Structures.OrganizacionStructure import Organizacion

import MySQLdb

class DbFunctionsOrgUsuario(DbFunctions) :

    def formarOrgUsuarioObject (self, orgUsList) :
        nuevaOrgusuarioObject = Orgusuario()

        #Inicializando atributos
        nuevaOrgusuarioObject.setIdOrgUsuario(orgUsList[0])
        nuevaOrgusuarioObject.setIdUsuario(orgUsList[1])
        nuevaOrgusuarioObject.setIdOrg(orgUsList[2])
        nuevaOrgusuarioObject.setIdPermisos(orgUsList[3])
        nuevaOrgusuarioObject.setNombrePilaUser(orgUsList[4])
        nuevaOrgusuarioObject.setEstadoUsuario([orgUsList[5]])

        return nuevaOrgusuarioObject

    def expulsarUsuario (self, Usuario, Organizacion) :
        condicion = "Orgusuario.IdUsuario = {} AND IdOrganizacion = {}".format(Usuario.getIdUsuario(),
                                                                               Organizacion.getIdOrganizacion())

         #Answer me guardara el resultado de la consulta
        return self.deleteFrom("Orgusuario", condicion)

