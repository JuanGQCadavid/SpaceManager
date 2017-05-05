from Model.DBFunctions import DbFunctions
from Model.Structures.PermisosStructure import Permisos
import MySQLdb

class DBPermisos (DbFunctions) :

    def formarObjeto (self, list) :
        nuevoPermiso = Permisos()
        nuevoPermiso.setIdPermisos(list[0])
        nuevoPermiso.setBoss(list[1])
        nuevoPermiso.setP_Reserva(list[2])
        nuevoPermiso.setP_Nivel(list[3])
        nuevoPermiso.setP_Bloque(list[4])
        nuevoPermiso.setP_Sede(list[5])
        nuevoPermiso.setP_Org(list[6])
        nuevoPermiso.setPC_B(list[7])
        nuevoPermiso.setPC_S(list[8])
        nuevoPermiso.setPC_N(list[9])
        nuevoPermiso.setPC_E(list[10])
        nuevoPermiso.setP_Encargado(list[11])

        return nuevoPermiso

    def insertPermisos (self, nuevoPermiso) :
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
                                                     nuevoPermiso.getP_Encargado()
                                                      )
        result = "ERROR"
        try:
            result = self.insertInto("Permisos", values)
            return nuevoPermiso

        except (MySQLdb.IntegrityError) :
            result = "ERROR: Tenemos problema de Integridad En INSERTAR permisos"
            print result
            return None

    def ObejtoInsertar(self, PermisosList):
        return self.insertPermisos(self.formarObjeto(PermisosList))

    def obtenerPermisos(self, PermisosPk):
        query = "SELECT * FROM Permisos WHERE idPermisos = '{}'".format(PermisosPk)
        result = self.run_query(query)
        print result
        if not(result == []):
            return result[0]

    def actualizarPermisosDB(self, permisosList):
        # Suponiendo que van en un arrayList, en ese orden.
        sets = "P_Reserva = {}, P_Nivel = {}, P_Bloque = {}, P_Sede = {}, P_Org = {}," \
               "PC_B = {}, PC_S = {}, PC_N = {}, PC_E = {}, P_Encargado = {}".format(permisosList[1],
                                                                                      permisosList[2],
                                                                                      permisosList[3],
                                                                                      permisosList[4],
                                                                                      permisosList[5],
                                                                                      permisosList[6],
                                                                                      permisosList[7],
                                                                                      permisosList[8],
                                                                                      permisosList[9],
                                                                                      permisosList[10])


        condicion = "idPermisos = '{}'".format(permisosList[0])

        return self.update("Permisos", sets, condicion)

    def eliminarDB(self, pk):
        return self.deleteFrom ('Permisos', "idPermisos = '{}'".format(pk))
