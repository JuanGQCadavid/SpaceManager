# -*- coding: cp1252 -*-
from  DBFunctionUser import DbFunctionUser
#from  Model.DBFunctionUser import DbFunctionUser

from Model.Structures.UsuarioStructure import Usuario
from Model.Structures.RedessocialesStructure import Redessociales
from Controller.DBFunctionPermisosPrivacidad import Privacidadusuario
from Model.Structures.PrivacidadusuarioStructure import Privacidadusuario


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

    # building the Object Social

    socialObject = socialNetworkRegister(userList[0],socialNetworkList)

    # Building Permisos Object

    permisosPrivacidadObject = permisosPrivacidad(userList,permisosPrivacidadList)

    # building the Object

    userObject = Usuario()
    userObject.setIdUsuario(userList[0])
    userObject.setClaveUsuario(userList[1])
    userObject.setNombreUsuario(userList[2])
    userObject.setDescripcion(userList[3])
    userObject.setTelefonoCelular(userList[4])
    userObject.setCorreoElectronico(userList[5])
    userObject.setIdRedesSociales(socialObject.getIdRedesSociales())
    userObject.setIdPrivacidad(permisosPrivacidadObject.getIdPrivacidadUsuario())
    userObject.setEstadoUsuario(1)

    #Coneccting with Db Functions for user

    functionObject = DbFunctionUser()
    userInfo = functionObject.insertUser(userObject)







userLogin(["jquiro125","asd123"])
