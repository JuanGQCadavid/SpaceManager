from Model.DBConection import DataBaseConection


class Reserva_DBF(DataBaseConection):
    def obtenerEspacios(self,idOrgCreador,idOrgContador ,idSede):
        return self.run_query("CALL espaciosXreservas_Org('{}',{},{})".format(idOrgCreador,idOrgContador,idSede))


    def reservar(self,idEspacio , idNivel , idBloque , idSede , idOrgCreador , idOrgConsecutivo , idUsuario ,Lunes , Martes ,Miercoles,Jueves ,Viernes
                ,Sabado, Domingo, fechaInicio, fechaFin, horaInicio, horaFin):
        return self.run_query("CALL insert_Reserva ({},{},{},{},'{}',{},'{}',{},{},{},{},{},{},{},'{}','{}','{}','{}')".format(idEspacio , idNivel , idBloque , idSede , idOrgCreador ,
                                                              idOrgConsecutivo , idUsuario ,Lunes , Martes ,Miercoles,Jueves ,Viernes
                                                              ,Sabado, Domingo, fechaInicio, fechaFin, horaInicio, horaFin))

