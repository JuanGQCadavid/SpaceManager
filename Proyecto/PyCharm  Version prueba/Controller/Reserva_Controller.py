from Model.Reserva_DB import Reserva_DBF
import datetime

def reservar(idOrgCreador,idOrgContador ,idSede, fechaInicio ,
             fechaFin, horaInicio ,  horaFin,lunes, martes,
             miercoles,jueves , viernes , sabado ,domingo ):


    clase_Reserva = Reserva_DBF()
    espacios = clase_Reserva.obtenerEspacios(idOrgCreador, idOrgContador, idSede)

    if espacios.__len__() < 1:
        return espacios


    #Arreglos

    lista_Espacios = []

    listas_Espacios_Vistos = []

    lista_Dias = {'lunes':[],'martes':[],'miercoles':[],'jueves':[],'viernes':[],'sabado':[],'domingo':[]}
    resultado = {'lunes':[],'martes':[],'miercoles':[],'jueves':[],'viernes':[],'sabado':[],'domingo':[]}

    superPerra = False
    for espacio in espacios:

        for listos in listas_Espacios_Vistos:
            if (listos == espacio):
                superPerra = True

        if superPerra:
            superPerra = False
            continue

        for subSpacios in espacios:

            if (subSpacios[0] == espacio[0] and subSpacios[1] == espacio[1] and subSpacios[2] == espacio[2] and
                subSpacios[3] == espacio[3] and subSpacios[4] == espacio[4] and subSpacios[5] == espacio[5]):

                print subSpacios
                listas_Espacios_Vistos.append(subSpacios)
                lista_Espacios.append(subSpacios)


        for lista_Espacio in lista_Espacios:
            if lista_Espacio[7] == 1 or lista_Espacio[6] == None:
                lista_Dias['lunes'].append(lista_Espacio)

            if lista_Espacio[8] == 1 or lista_Espacio[6] == None:
                lista_Dias['martes'].append(lista_Espacio)

            if lista_Espacio[9] == 1 or lista_Espacio[6] == None:
                lista_Dias['miercoles'].append(lista_Espacio)

            if lista_Espacio[10] == 1 or lista_Espacio[6] == None:
                lista_Dias['jueves'].append(lista_Espacio)

            if lista_Espacio[11] == 1 or lista_Espacio[6] == None:
                lista_Dias['viernes'].append(lista_Espacio)

            if lista_Espacio[12] == 1 or lista_Espacio[6] == None:
                lista_Dias['sabado'].append(lista_Espacio)

            if lista_Espacio[13] == 1 or lista_Espacio[6] == None:
                lista_Dias['domingo'].append(lista_Espacio)



        if lista_Dias['lunes'] != []:
            if lunes:
                bandera = True
                for salon_listaDias in lista_Dias['lunes']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break

                    if (horaInicio >= salon_listaDias[16] and  horaInicio < salon_listaDias[17]) or (horaFin > salon_listaDias[16] and  horaFin < salon_listaDias[17]):
                        bandera = False
                        break

                if bandera:
                    resultado['lunes'].append(lista_Dias['lunes'][0])
                    pass
                pass


        if lista_Dias['martes'] != []:
            if martes:
                bandera = True
                for salon_listaDias in lista_Dias['martes']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break

                    if (horaInicio >= salon_listaDias[16] and horaInicio < salon_listaDias[17]) or (
                            horaFin > salon_listaDias[16] and horaFin < salon_listaDias[17]):

                        bandera = False
                        break

                if bandera:
                    resultado['martes'].append(lista_Dias['martes'][0])
                    pass
                pass



        if lista_Dias['miercoles'] != []:
            if miercoles:
                bandera = True
                for salon_listaDias in lista_Dias['miercoles']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break

                    if (horaInicio >= salon_listaDias[16] and horaInicio < salon_listaDias[17]) or (
                                    horaFin > salon_listaDias[16] and horaFin < salon_listaDias[17]):
                        bandera = False
                        break

                if bandera:
                    resultado['miercoles'].append(lista_Dias['miercoles'][0])
                    pass
                pass


        if lista_Dias['jueves'] != []:
            if jueves:
                bandera = True
                for salon_listaDias in lista_Dias['jueves']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break

                    if (horaInicio >= salon_listaDias[16] and horaInicio < salon_listaDias[17]) or (
                                    horaFin > salon_listaDias[16] and horaFin < salon_listaDias[17]):

                        bandera = False
                        break

                if bandera:
                    resultado['jueves'].append(lista_Dias['jueves'][0])
                    pass
                pass


        if lista_Dias['viernes'] != []:
            if viernes:
                bandera = True
                for salon_listaDias in lista_Dias['viernes']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break

                    if (horaInicio >= salon_listaDias[16] and horaInicio < salon_listaDias[17]) or (
                                    horaFin > salon_listaDias[16] and horaFin < salon_listaDias[17]):

                        bandera = False
                        break

                if bandera:
                    resultado['viernes'].append(lista_Dias['viernes'][0])
                    pass
                pass


        if lista_Dias['sabado'] != []:
            if sabado:
                bandera = True
                for salon_listaDias in lista_Dias['sabado']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break


                    if (horaInicio >= salon_listaDias[16] and horaInicio < salon_listaDias[17]) or (
                                    horaFin > salon_listaDias[16] and horaFin < salon_listaDias[17]):

                        bandera = False
                        break

                if bandera:
                    resultado['sabado'].append(lista_Dias['sabado'][0])
                    pass
                pass


        if lista_Dias['domingo'] != []:
            if domingo:
                bandera = True
                for salon_listaDias in lista_Dias['domingo']:

                    if salon_listaDias[6] == None:
                        bandera = True
                        break

                    if (horaInicio >= salon_listaDias[16] and horaInicio < salon_listaDias[17]) or (
                                    horaFin > salon_listaDias[16] and horaFin < salon_listaDias[17]):

                        bandera = False
                        break

                if bandera:
                    resultado['domingo'].append(lista_Dias['domingo'][0])
                    pass
                pass

        lista_Espacios = []
        lista_Dias = {'lunes': [], 'martes': [], 'miercoles': [], 'jueves': [], 'viernes': [], 'sabado': [], 'domingo': []}


    return resultado




'''


horaInicio = datetime.timedelta(hours=15, minutes=0, seconds=0)
horahoraFin = datetime.timedelta(hours=16, minutes=0, seconds=0)

result = reservar('jquiro12', 1, 1, None, None, horaInicio, horahoraFin, True, False, False, True, False, False, True)

for espacios in result['miercoles']:
    print espacios


now = datetime.datetime.now()
horahoraFin = now.replace(hour=17, minute=0, second=0, microsecond=0)

        print lista_Dias['lunes']
        print lista_Dias['martes']
        print lista_Dias['miercoles']
        print lista_Dias['jueves']
        print lista_Dias['viernes']
        print lista_Dias['sabado']
        print lista_Dias['domingo']
                print lista_Espacios
'''