# -*- coding: cp1252 -*-
from  DBFunctionUser import DbFunctionUser
from DBSocialNetwork import DBSocialNetwork
from DBFunctionPermisosPrivacidad import DBFunctionPermisoPrivacidad



from Model.Structures.UsuarioStructure import Usuario



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

        print "Welcom to the Jungle! {}".format(userObject.getNombreUsuario())
    else:
        print "No parse, no lo puedo dejar pasar"


def userRegister(userList,permisosPrivacidadList,socialNetworkList):
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

listaRedes = ["amanda","Face","Twitter","Linkedin","Instagram","Google"]
listaPrivacidad = ["amanda",1,1,1,0,1,1]
listaUsuario = ["Amanda17","choriseo","Amanda la del Atraro","Atracando ando","0598714","amanda@gmail.com",None,None,0]


userRegister(listaUsuario,listaPrivacidad,listaRedes)

'''''
'''''''''
userLogin(["jquiro125","asd123"])
'''''''''''