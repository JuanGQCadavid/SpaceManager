
from Model.PrivacidadUsuarioDBF import PrivacidadUsuarioDBF
from Model.RedesSocialesDBF import RedesSocialesDBF
from Model.UsuarioDBF import UsuarioDBF

import time
'''

def actualizarStatement(list,tipo,pk) :

    print 'usuario_Controller actualizarStatement'
    claseFunctionUser = DbFunctionUser()

    if tipo == 0:
        return claseFunctionUser.actualizarStatement("Usuario","idUsuario",pk,"claveUsuario",list,0)
    else:
        return claseFunctionUser.actualizarStatement("Usuario", "idUsuario", pk, "estadoUsuario", list, 4)

def actualizarInfo(list,tipo,user_PK):
    print 'usuario_Controller actualizarInfo'
    claseFunctionUser = DbFunctionUser()
    ''
        0 -> Cambio de Clave FUNCIONANDO
        4 -> Cambio de Estado FUNCIONANDO
        1 -> Cambio basico info usuario FUNCIONANDO
        2 -> Cambio basico Redoes Sciales 
        3 -> Cambio basico Privacidad usuario FUNCIONANDO
    ''

    if tipo == 0 or tipo == 4:
        return actualizarStatement(list,tipo,user_PK)
    elif tipo == 1:

        return claseFunctionUser.actualizarUsuario(list,user_PK)
    elif tipo == 2:

        claseFunctionUser.actualizarRedesS(user_PK,'GenericNull')

        pkredes =  actualizarRedesSociales(user_PK,list)

        claseFunctionUser.actualizarRedesS(user_PK, pkredes)

    elif tipo == 3:
        return actualizarPrivacidad(user_PK,list)

        pass
'''
def userLogin(idUsuario,claveUsuario):
    print 'usuario_Controller userLogin'

    #Clase
    userDBF = UsuarioDBF()

    #Obtner Respuesta
    respuesta = userDBF.userLogin(idUsuario,claveUsuario)

    print respuesta

    #checking information


    return respuesta

def userRegister (userList, permisosPrivacidadList, socialNetworkList) :
    print 'usuario_Controller userRegister'

    #Creando Classes

    claseSocialNetwor = RedesSocialesDBF()
    clasePrivacidadUsuario = PrivacidadUsuarioDBF()
    claseUsuario = UsuarioDBF()



    # Creando objeto Social y guardando en MySQL.

    userList.insert(6,claseSocialNetwor.insertarRedesSociales(idRedesSociales = socialNetworkList[0],
                                                          FaceBook = socialNetworkList[1],
                                                          Twitter = socialNetworkList[2],
                                                          Linkedin = socialNetworkList[3],
                                                          Instagram = socialNetworkList[4],
                                                          Google = socialNetworkList[5]))


    # Building Permisos Object y guardando en MySQL.

    if (permisosPrivacidadList[0] == None and permisosPrivacidadList[1] == None and
        permisosPrivacidadList[2] == None and permisosPrivacidadList[3] == None and
        permisosPrivacidadList[4] == None):

        userList.insert(7,None)

    else:
        userList.insert(7,clasePrivacidadUsuario.insertarPrivacidad(MostrarCorreo = permisosPrivacidadList[0],
                                                            MostrarOrgPropias = permisosPrivacidadList[1] ,
                                                            MostrarOrgPertenece = permisosPrivacidadList[2] ,
                                                            MostrarRedesSociales = permisosPrivacidadList[3] ,
                                                            MostrarTelefono = permisosPrivacidadList[4]))

    # building user Object y guardando en MySQL.


    print userList


    #Creando Objeto y guardando en MySQL.


    return claseUsuario.insertarUsuario(idUsuario = userList[0], claveUsuario= userList[1], nombreUsuario= userList[2],
                                        descripcion = userList[3], telefonoCelular = userList[4] ,correoElectronico = userList[5] ,
                                        idRedesSociales = userList[6],idPrivacidad = userList[7] )


def obtenerUser(userID):
    claseUsuario = UsuarioDBF()
    return claseUsuario.obtenerUsuario(userID)



'''''''''


userRegister(["Anita14","bandoleo","Juan Gonzalo","El perreo Intenso","3147703216","juangonzalo23@gmail.com"],
             [0,0,0,0,0],['Anita14',None,None,None,None,None])

userLogin('jquiro12','bandoleo')



actualizarInfo([None,None,None,None,None],2,'jquiro12')
userRegister(["jquiro12","bandoleo","Juan Gonzalo","El perreo Intenso","3147703216","juangonzalo23@gmail.com"],
             [0,0,0,0,0],['jquiro12',None,None,None,None,None])
userRegister(["pkUser","claveusuario","NombreUsuario","Descripcion","Telefono","CorreoElectronico","pkRS","pkIP",EstadoU,fechaCreacion],
             ["pkUser",MC,MOPRO,MOPERT,MRS,MT],['pkUser',"Face","Twitter","Linkelin","Instagram","Google"])

userRegister(["jquiro12","bandoleo","Juan Gonzalo","El perreo Intenso","3147703216","juangonzalo23@gmail.com","pk","pk",1,"fecha"],
             ["jquiro12",0,0,0,0,0],['jquiro12',None,None,None,None,None])
             
userRegister(["jquiro13","bandoleo2","Juan Gonzalo","El perreo Intenso","3147703216","juangonzalo23@gmail.com","pk","pk",1,"fecha"],
             ["jquiro13",0,0,0,0,0],['jquiro13',None,None,None,None,None])

userRegister(["jquiro14","bandoleo3","Juan Gonzalo","El perreo Intenso","3147703216","juangonzalo23@gmail.com","pk","pk",1,"fecha"],
             ["jquiro14",0,0,0,0,0],['jquiro14',None,None,None,None,None])
             
             
Probando actualizarInfo
actualizarInfo(["pk",None,None,None,None,None],2,"Amanda17")
actualizarInfo(1,4, "Amanda17")

//Clave

userNewObject = Usuario("Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com","amanda","amanda",1)

actualizarInfo(userNewObject, "La Amante perfecta", 0)

//Estado

userNewObject = Usuario("Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com","amanda","amanda",1)

actualizarInfo(userNewObject, 0, 4)


'''''''''





'''''''''

listaRedes = ["Amanda17","Face","Twitter","Linkedin","Instagram","Google"]
listaPrivacidad = ["Amanda17",1,1,1,0,1,1]
listaUsuario = ["Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com",None,None,0]


userRegister(listaUsuario,listaPrivacidad,listaRedes)

'''''
'''''''''
userLogin(["jquiro125","asd123"])
'''''''''''
