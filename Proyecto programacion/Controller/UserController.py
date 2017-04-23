# -*- coding: cp1252 -*-
from  DBFunctionUser import DbFunctionUser
from DBSocialNetwork import DBSocialNetwork
from DBFunctionPermisosPrivacidad import DBFunctionPermisoPrivacidad

from Model.Structures.UsuarioStructure import Usuario

<<<<<<< HEAD
def userLogin (userList) :
=======

def actualizarStatement(userObject,tipo):
    claseFunctionUser = DbFunctionUser()
    pk = userObject.getIdUsuario()

    if tipo == 0:
        return claseFunctionUser.actualizarStatement("usuario","idUsuario",pk,"claveUsuario",userObject.getClaveUsuario(),0)
    else:
        return claseFunctionUser.actualizarStatement("usuario", "idUsuario", pk, "estadoUsuario", userObject.getEstadoUsuario(), 4)

def actualizarInfo(userObject,tipo):

    '''''''''
        0 -> Cambio de Clave
        4 -> Cambio de Estado
        1 -> Cambio basico info usuario
        2 -> Cambio basico Redes Sociales
        3 -> Cambio basico Privacidad usuario
    '''''''''

    if tipo == 0 or tipo == 4:
        return actualizarStatement(userObject,tipo)
    elif tipo == 1:
        claseFunctionUser = DbFunctionUser()
        return claseFunctionUser.actualizarUsuario(userObject)
        pass
    elif tipo == 2:
        pass
    elif tipo == 3:
        pass


def userLogin(userList):
>>>>>>> 1d4a3638c1a112bb3f71de94057f03e2f40ba777

    #building the Object

    userObject = Usuario()
    userObject.setIdUsuario(userList[0])
    userObject.setClaveUsuario(userList[1])

    #Coneccting with Db Functions for user

    functionObject = DbFunctionUser()
    userObject = functionObject.ValidarUser(userObject)



    #checking information


    if not(userObject == None):

        print "Welcome to the Jungle! {}".format(userObject.getNombreUsuario())
    else:
        print "No parse, no lo puedo dejar pasar"


def userRegister (userList,permisosPrivacidadList,socialNetworkList) :
    #Creando Classes

    claseSocialNetwor = DBSocialNetwork()
    clasePrivacidadUsuario = DBFunctionPermisoPrivacidad()
    claseUsuario = DbFunctionUser()

    # Creando objeto Social y guardando en MySQL.

    socialObject = claseSocialNetwor.generarRedessocialesObject(socialNetworkList)
    claseSocialNetwor.insertRedessociales(socialObject)


    # Building Permisos Object y guardando en MySQL.

    permisosPrivacidadObject = clasePrivacidadUsuario.generarPrivacidadObject(permisosPrivacidadList)
    clasePrivacidadUsuario.insertPermisosPrivacidad(permisosPrivacidadObject)

    # building user Object y guardando en MySQL.

    #Estableciendo PK

    userList[6] = socialObject.getIdRedesSociales()
    userList[7] = permisosPrivacidadObject.getIdPrivacidadUsuario()

    #Creando Objeto y guardando en MySQL.

    userObject = claseUsuario.FormarUserObject(userList)
    claseUsuario.insertUser(userObject)





'''''''''
Probando actualizarInfo

//Clave

userNewObject = Usuario("Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com","amanda","amanda",1)

actualizarInfo(userNewObject, "La Amante perfecta", 0)

//Estado

userNewObject = Usuario("Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com","amanda","amanda",1)

actualizarInfo(userNewObject, 0, 4)


'''''''''





'''''''''

listaRedes = ["amanda","Face","Twitter","Linkedin","Instagram","Google"]
listaPrivacidad = ["amanda",1,1,1,0,1,1]
listaUsuario = ["Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com",None,None,0]


userRegister(listaUsuario,listaPrivacidad,listaRedes)

'''''
'''''''''
userLogin(["jquiro125","asd123"])
'''''''''''
