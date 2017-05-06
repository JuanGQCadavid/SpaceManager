
from Controller.DBFunctions.DBOrgUser import DBOrgUser

import time

print 'Org Usuario Controlador'
'''

    0 Inactivo
    1 Aceptado /Aceptar
    2 Pendiente
    3 Desterrado
    4 baneado
    5 Invitado Aceptar
    6 Declinar

'''
def asociarOrgUser(idUser,idOrgContador,idOrgCreador ,idPermisos,nombrePila):

    idOrguser = idOrgCreador + "_$_" + str(idOrgContador) + '@' + idUser
    fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")

    orgList= [idOrguser,idOrgCreador,idOrgContador,idUser,idPermisos,nombrePila,1,fechaActual]

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

def bossAsignation(idUser,idConsecutivo,nombrePila):
    return asociarOrgUser(idUser,idConsecutivo,idUser,'theBoss',nombrePila)

def invitarUsuario(idUser,idConsecutivo,idOrgcreador, nombrePila):
    return asociarOrgUser(idUser,idConsecutivo,idOrgcreador,'invitado',nombrePila)

'''
def acpetarInvitacion(idOrguser):
    #Crear Clases
    claseOrg = DbFunctionOrganizacion()
    claseOrgUser = DBOrgUser()


    orgUserObject = claseOrgUser.obtenerUsuarioOrgComoObject(idOrguser)
    permisosEstandar = claseOrg.obtenerUsuarioComoObject(orgUserObject.getIdOrg())

    return claseOrgUser.acceptarInivitacion(idOrguser,permisosEstandar)
'''
def cancerlarInvitacion(idOrgUser):
    clase = DBOrgUser
    return clase.cambiarEstado(idOrgUser,'6')


'''
invitarUsuario('Amanda178','Amanda17_nombre','La Perris ')
    bossAsignation('Amanda17811','Amanda17_nombre','LaAmanda')
   asociarOrgUser('Amanda178','Amanda17_nombre','10101010101','jquiro12')
   desterrar('Amanda17_nombre@Amanda178')
'''