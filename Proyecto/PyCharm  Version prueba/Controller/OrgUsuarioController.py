
import time


'''

    0 Inactivo
    1 Aceptado /Aceptar
    2 Pendiente
    3 Desterrado
    4 baneado
    5 Invitado 
    6 Declinar
    7 se fue

'''

#Este metodo es usuado por Organizacion
def asociarOrgUser(idUser,idOrgContador,idOrgCreador ,idPermisos,nombrePila,estado):
    print 'Org Usuario Controlador - asociarOrgUser'

    idOrguser = idOrgCreador + "_$_" + str(idOrgContador) + '@' + idUser
    fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")

    orgList= [idOrguser,idOrgCreador,idOrgContador,idUser,idPermisos,nombrePila,estado,fechaActual]

    claseOrgUser = DBOrgUser()

    return claseOrgUser.objectInsert(orgList)

def desterrar(idOrguser):
    print 'Org Usuario Controlador - desterrar'
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrguser,'3')

def banear(idOrguser):
    print 'Org Usuario Controlador - banear'
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrguser,'4')

def salir(idOrguser):
    print 'Org Usuario Controlador - salir'
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrguser,'7')

def bossAsignation(idUser,idConsecutivo,nombrePila):
    print 'Org Usuario Controlador - bossAsignation'
    return asociarOrgUser(idUser,idConsecutivo,idUser,'theBoss',nombrePila,1)

def invitarUsuario(idUser,idConsecutivo,idOrgcreador,):
    print 'Org Usuario Controlador - invitarUsuario'
    return asociarOrgUser(idUser,idConsecutivo,idOrgcreador,'invitado','invitado',5)

def cancerlarInvitacion(idOrgUser):
    print 'Org Usuario Controlador - cancerlarInvitacion'
    clase = DBOrgUser()
    return clase.cambiarEstado(idOrgUser,'6')

def actualizarOrgUser(idOrguser,idPermisos,nombrePila):
    print 'Org Usuario Controlador - actualizarOrgUser'
    clase_Org_user = DBOrgUser()
    fechaActual = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")
    return clase_Org_user.actualizarOrgUserDB(idOrguser ,idPermisos,nombrePila,fechaActual)

def acpetarInvitacion(idOrguser,nombrePila):
    print 'Org Usuario Controlador - acpetarInvitacion'
    #Clases
    clase_Org_User = DBOrgUser()
    clase_Org_DB =  DbFunctionOrganizacion()

    #Obtener el Objeto de la org user
    objeto_org_user = clase_Org_User.obtenerUsuarioOrgComoObject(idOrguser)

    #Obtenemos el Objeto de la Org
    permisos_estandar_org = clase_Org_DB.obtenerPermisosEstandar(objeto_org_user.getIdOrgUsuarioCreador(),
                                                                           objeto_org_user.getIdOrgContador())


    return actualizarOrgUser(idOrguser,
                          permisos_estandar_org,
                          nombrePila)

def solicitar(idUser,idOrgContador,idOrgCreador):
    print 'Org Usuario Controlador - solicitar'
    return asociarOrgUser(idUser,idOrgContador,idOrgCreador ,'solicitante','solicitante',2)

def mostrarOrgsPertenece(idUser):
    print 'Org Usuario Controlador - mostrarOrgsPertenece'
    clase_Org_Usuario =DBOrgUser()
    return clase_Org_Usuario.mostrarOrgPertenece(idUser)

def mostrarOrgMiembros(idOrgCreador,idOrgContador, estadoMostrar):
    print 'Org Usuario Controlador - mostrarOrgMiembros'
    clase_Org_Usuario = DBOrgUser()
    return clase_Org_Usuario.mostrarOrgMiembros(idOrgCreador,idOrgContador, estadoMostrar)

def mostrarOrgMiembrosAcceptados(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosAcceptados'
    return mostrarOrgMiembros(idOrgCreador,idOrgContador,1)

def mostrarOrgMiembrosPendientes(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosPendientes'
    return mostrarOrgMiembros(idOrgCreador, idOrgContador, 2)

def mostrarOrgMiembrosDesterrados(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosDesterrados'
    return mostrarOrgMiembros(idOrgCreador, idOrgContador, 3)

def mostrarOrgMiembrosBaneados(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosBaneados'
    return mostrarOrgMiembros(idOrgCreador, idOrgContador, 4)

def mostrarOrgMiembrosInvitados(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosInvitados'
    return mostrarOrgMiembros(idOrgCreador, idOrgContador, 5)

def mostrarOrgMiembrosDeclinados(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosDeclinados'
    return mostrarOrgMiembros(idOrgCreador, idOrgContador, 6)

def mostrarOrgMiembrosSalidos(idOrgCreador,idOrgContador):
    print 'Org Usuario Controlador - mostrarOrgMiembrosSalidos'
    return mostrarOrgMiembros(idOrgCreador, idOrgContador, 7)

asociarOrgUser('jquiro13',1,'jquiro12' ,'theBoss','Lucas 15',1)


'''
print mostrarOrgMiembrosAcceptados('jquiro12',1)
print mostrarOrgMiembros('jquiro12',1,1)
print mostrarOrgsPertenece('jquiro12')
acpetarInvitacion('jquiro12_$_1@jquiro14','Bolas Y pAlos')
cancerlarInvitacion('jquiro12_$_1@jquiro14')
invitarUsuario('jquiro14',1,'jquiro12','La pupis')

'''

'''
asociarOrgUser('jquiro13',1,'jquiro12' ,'theBoss','Lucas 15')
invitarUsuario('Amanda178','Amanda17_nombre','La Perris ')
    bossAsignation('Amanda17811','Amanda17_nombre','LaAmanda')
   asociarOrgUser('Amanda178','Amanda17_nombre','10101010101','jquiro12')
   desterrar('Amanda17_nombre@Amanda178')
'''