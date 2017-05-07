# -*- coding: cp1252 -*-
#pragma once
from Controller.Controladores.PermisosController import insertarPermiso,actualizarPermiso
from Controller.Controladores.RedesSocialesController import insertarRedesSociales,actualizarRedesSociales
from Controller.DBFunctions.DBOrganizacion import DbFunctionOrganizacion
from Controller.Controladores.OrgUsuarioController import bossAsignation
import time


'''
En el Formulario, la lista se entregara de la Sigt manera

redesSociales[pk,[ATRIBUTOS]]
    permisosEstandarlist[ATRIBUTOS] -> osea sin campo de pk
    orgList[pk,pk,NombreOrg,descrip_Org,pkPer,pkRedes,telefonoOrg,estadoOrg(1),fechaCreacion]

'''

def generarPkOrg(user_pk,orgName):
    print 'Organizacion Controlador - generarPkOrg'

    orgName = orgName.lower()
    pkOrg = user_pk+"$"

    for words in orgName:
        if words == ' ':
            continue
        else:
            pkOrg+= words

    return pkOrg



'''
    redesSociales[pk,[ATRIBUTOS]]
    permisosEstandarlist[ATRIBUTOS] -> osea sin campo de pk
    orgList[pk,pk,NombreOrg,descrip_Org,pkPer,pkRedes,telefonoOrg,estadoOrg(1),fechaCreacion, tipoEnrrol]
    
    ENROLL:
    
        1 -> Solo invitacion
        2 -> tambien Solicitud
        3 -> Libre

'''
def crearOrg(userPk,  orgList ,redesSocialesList, permisosEstandarList,nombrePila):
    print 'Organizacion Controlador - crearOrg'

    claseDBFunctions = DbFunctionOrganizacion()
    '''
        Generar Pk Org
        
        1- obtener el consecutivo
    '''

    consecutivo = (claseDBFunctions.obtenerConsecutivo(userPk))+1
    primaryKey = userPk+ "_$_"+ str(consecutivo)

    #Generamos la PK para redes Sociales
    redesSocialesList[0] = primaryKey

    #Mandamos a crear Redes Sociales
    pkRedesSociales = insertarRedesSociales(redesSocialesList)

    #Mandamos a crear Permiso Estandares
    pkPermisosEstandares = insertarPermiso(permisosEstandarList)

    #Generamos Fecha
    fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")

    #mandamos a crear la Org

    #Asignamos Pks

    orgList[0] = userPk
    orgList[1] = consecutivo
    orgList[4] = pkPermisosEstandares
    orgList[5] = pkRedesSociales
    orgList[8] = fechaActual

    objetoOrgNuevo = claseDBFunctions.objetInsert(orgList)

    bossAsignation(userPk,consecutivo, nombrePila)


def obtenerOrg(orgPk):
    print 'Organizacion Controlador - obtenerOrg'

    clase = DbFunctionOrganizacion()
    return clase.obtenerUsuarioComoObject(orgPk)


def actualizarRedes(pkOrgCreador,pkOrgConsecutivo, listActualizacion):
    print 'Organizacion Controlador - actualizarRedes'
    claseDb = DbFunctionOrganizacion()
    objetoOrg = claseDb.obtenerOrg(pkOrgCreador,pkOrgConsecutivo)

    pk_Redes_Sociales = pkOrgCreador + "_$_" + str(pkOrgConsecutivo)

    claseDb.configRedesSociales('GenericNull',pkOrgCreador,pkOrgConsecutivo )

    primaryKey = actualizarRedesSociales(pk_Redes_Sociales, listActualizacion)

    claseDb.configRedesSociales(primaryKey,pkOrgCreador,pkOrgConsecutivo)


def actualizarPermisos(pkOrgCreador,pkOrgConsecutivo, listActualizacion):
    print 'Organizacion Controlador - actualizarPermisos'

    claseDb = DbFunctionOrganizacion()

    primaryKey = actualizarPermiso(listActualizacion)

    return claseDb.configPermisosEstandar(primaryKey,pkOrgCreador,pkOrgConsecutivo)




'''
    1 -> Basicos Descripcion y Telefono [NOMBRE,DESC,TELEFONO]
    3 -> Permisos Estandar
    2 -> Redes Sociales 
    0 -> cerrar
    4 -> Abrir Org
    5 -> cambiar Tipo Enrrol

'''


def actualizar(tipoActualizacion,pkOrgCreador,pkOrgConsecutivo, listActualizacion):
    print 'Organizacion Controlador - actualizar'

    clase = DbFunctionOrganizacion()

    if tipoActualizacion == 0:
        return clase.cerrarOrg(pkOrgCreador,pkOrgConsecutivo)
    elif tipoActualizacion == 1:
        return clase.editarDatosbasicos(listActualizacion,pkOrgCreador,pkOrgConsecutivo)
    elif tipoActualizacion == 2:
        return actualizarRedes(pkOrgCreador,pkOrgConsecutivo, listActualizacion)
    elif tipoActualizacion == 3:
        return actualizarPermisos(pkOrgCreador,pkOrgConsecutivo, listActualizacion)
    elif tipoActualizacion == 4:
        return clase.abrirOrg(pkOrgCreador, pkOrgConsecutivo)
    elif tipoActualizacion == 5:
        return clase.camiarEnroll(pkOrgCreador,pkOrgConsecutivo, listActualizacion)

def consultar(id_User_Creador,id_Consecutivo = None):
    print 'Organizacion Controlador - consultar'
    clase_BD = DbFunctionOrganizacion()

    if id_Consecutivo == None:
        condition = "idUsuarioCreador = '{}'".format(id_User_Creador)
    else:

        condition = "idUsuarioCreador = '{}' AND consecutivoOrg = {}".format(id_User_Creador,id_Consecutivo)

    return clase_BD.consultarOrg(condition)






'''
actualizar(3,'jquiro12',1,[0,1,0,1,0,1,0,1,0,1,0])
actualizar(5,'jquiro12',1,2)
actualizarPermisos('jquiro12',1,[0,1,1,1,0,1,0,1,0,1,0])

print consultar('jquiro12',4)
actualizar(2,'jquiro12',3,[None,None,None,None,None])
actualizar(1,'jquiro12',3,['Los ANDES','Dandole Cana','2930926'])
actualizar(4,'jquiro12',2,None)

crearOrg('jquiro12',
         ['pk','pk','NombreOrg','descrip_Org','pkPer','pkRedes','telefonoOrg',1,'fechaCreacion',1],
         ['pk','Face','Twitter','Linkedin','instagram','Google'],
         [1,1,1,1,1,1,1,1,1,1,1],
         'El Gonzo'
         )
         

print(generarPkOrg('jquiro12','evers Companys'))

'''