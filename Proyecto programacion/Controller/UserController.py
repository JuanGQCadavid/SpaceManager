# -*- coding: cp1252 -*-
from  DBFunctionUser import DbFunctionUser
from DBSocialNetwork import DBSocialNetwork
from DBFunctionPermisosPrivacidad import DBFunctionPermisoPrivacidad
from PrivacidadUserController import actualizarPrivacidad
from Model.Structures.UsuarioStructure import Usuario



def actualizarStatement(list,tipo,pk):
    claseFunctionUser = DbFunctionUser()


    if tipo == 0:
        return claseFunctionUser.actualizarStatement("usuario","idUsuario",pk,"claveUsuario",list,0)
    else:
        return claseFunctionUser.actualizarStatement("usuario", "idUsuario", pk, "estadoUsuario", list, 4)

def actualizarInfo(list,tipo,pk):

    '''''''''
        0 -> Cambio de Clave FUNCIONANDO
        4 -> Cambio de Estado FUNCIONANDO
        1 -> Cambio basico info usuario FUNCIONANDO
        2 -> Cambio basico Redes Sociales
        3 -> Cambio basico Privacidad usuario FUNCIONANDO
    '''''''''

    if tipo == 0 or tipo == 4:
        return actualizarStatement(list,tipo,pk)
    elif tipo == 1:
        claseFunctionUser = DbFunctionUser()
        return claseFunctionUser.actualizarUsuario(list,pk)
        pass
    elif tipo == 2:
        pass
    elif tipo == 3:
        return actualizarPrivacidad(pk,list)
        pass

def userLogin(userList):


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

def modificarPrivacidad(pk,PrivacidadList):
    return actualizarPrivacidad(pk,PrivacidadList)

def modificarRedesSociales(pk,redesSocialesList):
    pass


actualizarInfo(['pk',1,1,1,1,1],3,"Amanda17")

'''''''''
Probando actualizarInfo

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
