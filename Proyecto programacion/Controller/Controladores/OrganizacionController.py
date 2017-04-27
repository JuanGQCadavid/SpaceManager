# -*- coding: cp1252 -*-
from Controller.Controladores.PermisosController import insertarPermiso
from Controller.Controladores.RedesSocialesController import insertarRedesSociales
from Controller.DBFunctions.DBOrganizacion import DbFunctionOrganizacion

'''
En el Formulario, la lista se entregara de la Sigt manera

[pk,fkUser,'nombre','nr sedes', 'dec', fkPermiso, fkredesSo,telefonos]

crearOrg('Amanda17',[1,0,1,0,1,0,1,0,1,0,1],['Amanda17',None,None,None,None,None],['pk','nombre',0, 'dec',
                                                                                 'fkPermiso', 'fkredesSo','telefonos'])

'''

def generarPkOrg(userPk,orgName):
    orgName = orgName.lower()
    pkOrg = userPk+"_"

    for words in orgName:
        if words == ' ':
            continue
        else:
            pkOrg+= words

    return pkOrg


def crearOrg(userPk,permisoEstandarList,redesSocialesList,orgList):

    permisosPk = insertarPermiso(permisoEstandarList)
    redesSocialesPk = insertarRedesSociales(redesSocialesList)
    pkOrg = generarPkOrg(userPk,orgList[1])

    orgList[0] = pkOrg
    orgList[4] = permisosPk
    orgList[5] = redesSocialesPk

    clase =DbFunctionOrganizacion()
    return clase.objetInsert(orgList)
crearOrg('Amanda17',[1,0,1,0,1,0,1,0,1,0,1],['Amanda17',None,None,None,None,None],['pk','nombre',0, 'dec',
                                                                                 'fkPermiso', 'fkredesSo','telefonos'])

'''
print(generarPkOrg('jquiro12','evers Companys'))

'''
