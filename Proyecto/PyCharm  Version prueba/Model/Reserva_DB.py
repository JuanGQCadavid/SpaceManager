from Model.DBConection import DataBaseConection


class Reserva_DBF(DataBaseConection):
    def obtenerEspacios(self,idOrgCreador,idOrgContador ,idSede):
        return self.run_query("CALL espaciosXreservas_Org('{}',{},{})".format(idOrgCreador,idOrgContador,idSede))


