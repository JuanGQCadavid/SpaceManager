from Model.DBFunctions import DbFunctions
from Model.Structures.OrganizacionStructure import Organizacion
from Model.Structures.PermisosStructure import Permisos
from Controller.DBFunctionUser import DbFunctionUser
from Controller.DBSocialNetwork import DBSocialNetwork
from Controller.DBFunctionPermisosPrivacidad import DBFunctionPermisoPrivacidad
from Controller.DBPermisos import DBPermisos
import MySQLdb
from Model.Structures.UsuarioStructure import Usuario
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
            return None


    def cambiarUsuarioEncargado (self, OrgObject, Usuario) :
        OrgObject.setIdUsuarioEncargado(Usuario.getIdUsuario());
        condicion = "idOrganizacion = {}".format(OrgObject.getIdOrganizacion)
        return self.up("Organizacion", "IdUsuarioEncargado", Usuario.getIdUsuario, condicion)

    def configPermisosEstandar (self, list) :
        a = Permisos(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11])





listredes = [1, "twitter", "facebook", "instagram", "linkedin", "google"]
r = DBSocialNetwork()
redes = r.generarRedessocialesObject(listredes)
r.insertRedessociales(redes)

listp = [23, 1, 1, 1, 1, 1]
p = DBFunctionPermisoPrivacidad()
permiso = p.generarPrivacidadObject(listp)
p.insertPermisosPrivacidad(permiso)

listu = [1, "asd", "RONALD", "HolA sOY RonalAld", "3106260064", "correo", 1, 'GenericT', 1]
u = DbFunctionUser()
user = u.FormarUserObject(listu)
u.insertUser(user)

listpermisos = [321, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lu = DBPermisos()
permisos =lu.formarObjeto(listpermisos)
lu.insertPermisos(permisos)

list = [1, 1, "Ronald", 12, "COMOTEVAOK", 321, 1, "5561457"]
n = DbFunctionOrganizacion()
a = n.FormarOrgObject(list)
n.insertOrg(a)
