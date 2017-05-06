from Model.DBFunctions import DbFunctions
from Model.Structures.PermisosStructure import Permisos
import mysql



class DBPermisos (DbFunctions) :

    def formarObjeto (self, list) :
        print 'Permisos DB - formarObjeto'

        nuevoPermiso = Permisos(idPermisos= list[0], boss= list[1], p_Reserva= list[2],
                                p_Nivel= list[3], p_Bloque= list[4], p_Sede= list[5],
                                p_Org= list[6], pC_B= list[7], pC_S= list[8],
                                pC_N= list[9], pC_E= list[10], p_Encargado= list[11])

        return nuevoPermiso

    def insertPermisos (self, nuevoPermiso) :
        print 'Permisos DB - insertPermisos'

        values = "'{}', {} ,{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(nuevoPermiso.getIdPermisos(),
                                                                           nuevoPermiso.getBoss(),
                                                                           nuevoPermiso.getP_Reserva(),
                                                                           nuevoPermiso.getP_Nivel(),
                                                                           nuevoPermiso.getP_Bloque(),
                                                                           nuevoPermiso.getP_Sede(),
                                                                           nuevoPermiso.getP_Org(),
                                                                           nuevoPermiso.getPC_B(),
                                                                           nuevoPermiso.getPC_S(),
                                                                           nuevoPermiso.getPC_N(),
                                                                           nuevoPermiso.getPC_E(),
                                                                           nuevoPermiso.getP_Encargado())
        result = "ERROR"
        try:
            result = self.insertInto("Permisos", values)
            return nuevoPermiso

        except (mysql.connector.errors.IntegrityError) :
            result = "ERROR: Tenemos problema de Integridad En INSERTAR permisos"
            print result
            return None

    def ObejtoInsertar(self, PermisosList):
        print 'Permisos DB - ObejtoInsertar'
        return (self.insertPermisos(self.formarObjeto(PermisosList))).getIdPermisos()

    def obtenerPermisos(self, PermisosPk):
        print 'Permisos DB - obtenerPermisos'

        query = "SELECT * FROM Permisos WHERE idPermisos = '{}'".format(PermisosPk)
        result = self.run_query(query)


        if not(result == []):
            return result[0]

    def eliminarDB(self, pk):
        return self.deleteFrom ('Permisos', "idPermisos = '{}'".format(pk))
