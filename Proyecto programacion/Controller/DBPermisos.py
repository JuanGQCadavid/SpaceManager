from Model.DBFunctions import DbFunctions
from Model.Structures.PermisosStructure import Permisos
import MySQLdb

class DBPermisos (DbFunctions) :

    def formarObjeto (self, list) :
        nuevoPermiso = Permisos()

        nuevoPermiso.setIdPermisos(list[0])
        nuevoPermiso.setP_Reserva(list[1])
        nuevoPermiso.setP_Nivel(list[2])
        nuevoPermiso.setP_Bloque(list[3])
        nuevoPermiso.setP_Sede(list[4])
        nuevoPermiso.setP_Org(list[5])
        nuevoPermiso.setPC_B(list[6])
        nuevoPermiso.setPC_S(list[7])
        nuevoPermiso.setPC_N(list[8])
        nuevoPermiso.setPC_E(list[9])
        nuevoPermiso.setP_Encargado(list[10])

        return nuevoPermiso

    def insertPermisos (self, nuevoPermiso) :
        values = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(nuevoPermiso.getIdPermisos(),
                                                      nuevoPermiso.getP_Reserva(),
                                                      nuevoPermiso.getP_Nivel(),
                                                      nuevoPermiso.getP_Bloque(),
                                                      nuevoPermiso.getP_Sede(),
                                                      nuevoPermiso.getP_Org(),
                                                      nuevoPermiso.getPC_B(),
                                                      nuevoPermiso.getPC_S(),
                                                     nuevoPermiso.getPC_N(),
                                                     nuevoPermiso.getPC_E(),
                                                     nuevoPermiso.getP_Encargado()
                                                      )
        result = "ERROR"
        try:
            result = self.insertInto("permisos", values)
            return nuevoPermiso

        except (MySQLdb.IntegrityError) :
            result = "ERROR: Tenemos problema de Integridad En INSERTAR permisos"
            return None


