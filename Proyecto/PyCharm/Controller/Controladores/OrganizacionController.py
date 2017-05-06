# -*- coding: cp1252 -*-
#pragma once
from Controller.Controladores.PermisosController import insertarPermiso
from Controller.Controladores.RedesSocialesController import insertarRedesSociales
from Controller.DBFunctions.DBOrganizacion import DbFunctionOrganizacion
from Controller.Controladores.OrgUsuarioController import bossAsignation
import time


'''
En el Formulario, la lista se entregara de la Sigt manera

[pk,fkUser,'nombre','nr sedes', 'dec', fkPermiso, fkredesSo,telefonos]

crearOrg('Amanda17',['pk',None,None,None,None,None],['pk','nombre',0, 'dec','fkPermiso', 'fkredesSo','telefonos','estado'])

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

def crearOrg(userPk,redesSocialesList,orgList):

    permisosPk = 'theBoss'
    redesSocialesPk = insertarRedesSociales(redesSocialesList)
    pkOrg = generarPkOrg(userPk,orgList[1])

    orgList[0] = pkOrg
    orgList[4] = permisosPk
    orgList[5] = redesSocialesPk

    clase =DbFunctionOrganizacion()
    clase.objetInsert(orgList)

    #Registrar en OrgUsuario
    bossAsignation(userPk,pkOrg,'NombrePila')

'''


'''
    redesSociales[pk,[ATRIBUTOS]]
    permisosEstandarlist[ATRIBUTOS] -> osea sin campo de pk
    orgList[pk,pk,NombreOrg,descrip_Org,pkPer,pkRedes,telefonoOrg,estadoOrg(1),fechaCreacion]

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



'''
    0 -> Basicos Descripcion y Telefono
    1 -> Permisos Estandar
    2 -> Redes Sociales
    3 -> cerrar

'''

def actualizar(tipoActualizacion,pkOrg, listActualizacion):
    print 'Organizacion Controlador - actualizar'
    if tipoActualizacion == 0:
        pass
    elif tipoActualizacion == 1:
        pass
    elif tipoActualizacion == 2:
        pass
    elif tipoActualizacion == 3:
        pass



crearOrg('jquiro12',
         ['pk','pk','NombreOrg','descrip_Org','pkPer','pkRedes','telefonoOrg',1,'fechaCreacion'],
         ['pk','Face','Twitter','Linkedin','instagram','Google'],
         [1,1,1,1,1,1,1,1,1,1,1],
         'El Gonzo'
         )

'''


crearOrg('Amanda178*/7',[1,0,1,0,1,0,1,0,1,0,1],['Las Enamoradas Peputa',None,None,None,None,None],['pk','Las Enamoradas Peputa',0, 'dec',
                                                                                 'fkPermiso', 'fkredesSo','telefonos',1])

crearOrg('Amanda178*/7',[1,0,1,0,1,0,1,0,1,0,1],['Las Enamoradas Peputa',None,None,None,None,None],['pk','Las Enamoradas Peputa',0, 'dec',
                                                                                 'fkPermiso', 'fkredesSo','telefonos',1])

crearOrg('Amanda178*/7',[1,0,1,0,1,0,1,0,1,0,1],['Amanda178*/7',None,None,None,None,None],['pk','Las Enamoradas Peputa',0, 'dec',
                                                                                 'fkPermiso', 'fkredesSo','telefonos'])    

crearOrg('Amanda17',[1,0,1,0,1,0,1,0,1,0,1],['Amanda17',None,None,None,None,None],['pk','nombre',0, 'dec',
                                                                                 'fkPermiso', 'fkredesSo','telefonos'])
print(generarPkOrg('jquiro12','evers Companys'))

'''