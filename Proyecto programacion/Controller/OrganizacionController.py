# -*- coding: cp1252 -*-
from DBOrganizacion import DbFunctionOrganizacion
from RedesSocialesController import insertarRedesSociales
from PermisosController import insertarPermiso

from Model.Structures.OrganizacionStructure import Organizacion

'''
En el Formulario, la lista se entregara de la Sigt manera

[pk,fkUser,'nombre','nr sedes', 'dec', fkPermiso, fkredesSo,telefonos]


crearOrg('Amanda17',[0,1,0,1,0,1,0,1,0,1],['Amanda17',None,None,None,None,None],['pk','fkUser','nombre',0, 'dec',
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
    pkOrg = generarPkOrg(userPk,orgList[2])

    orgList[0] = pkOrg
    orgList[1] = userPk
    orgList[5] = permisosPk
    orgList[6] = redesSocialesPk

    clase =DbFunctionOrganizacion()
    return clase.objetInsert(orgList)


'''
print(generarPkOrg('jquiro12','evers Companys'))

'''