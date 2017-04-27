
from Controller.DBFunctions.DBOrgUser import DBOrgUser
import time

'''

    0 Inactivo
    1 Aceptado
    2 Pendiente
    3 Desterrado
    4 baneado
    5 Invitado

'''
def asociarOrgUser(idUser,idOrg,idPermisos,nombrePila):

    idOrguser = idOrg + "@" + idUser
    fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")

    orgList= [idOrguser,idUser,idOrg,idPermisos,nombrePila,1,fechaActual]

    claseOrgUser = DBOrgUser()

    return claseOrgUser.objectInsert(orgList)

def desterrar(idOrguser):
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrguser,'3')

def banear(idOrguser):
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrguser,'4')

def acceptar(idOrguser):
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrguser,'1')


def bossAsignation(idUser,idOrg,nombrePila):
    return asociarOrgUser(idUser,idOrg,'theBoss',nombrePila)

def invitarUsuario(idUser,idOrg,nombrePila):
    return asociarOrgUser(idUser,idOrg,'invitado',nombrePila)

'''
   asociarOrgUser('Amanda178','Amanda17_nombre','10101010101','jquiro12')
   desterrar('Amanda17_nombre@Amanda178')
'''