# -*- coding: cp1252 -*-
from  Model.DBFunctionUser import DbFunctionUser
#from  Model.DBFunctionUser import DbFunctionUser

from Model.Structures.UsuarioStructure import Usuario
from Model.Structures.RedessocialesStructure import Redessociales
from Model.Structures.PrivacidadusuarioStructure import Privacidadusuario

def userLogin(userList):

    #building the Object

    userObject = Usuario()
    userObject.setUsuarioUsuario(userList[0])
    userObject.setClaveUsuario(userList[1])

    #Coneccting with Db Functions for user

    functionObject = DbFunctionUser()
    userInfo = functionObject.ValidarUser(userObject)

    #checking information


    if not(userInfo == {}):
        print "Welcom to the Jungle!"
    else:
        print "No parse, no lo puedo dejar pasar"


def permisosPrivacidad(userList,permisosPrivacidadList):
    permisosPrivacidadObject = Privacidadusuario()

    if permisosPrivacidadList[0] == "Generic":
        permisosPrivacidadObject.setIdPrivacidadUsuario(permisosPrivacidadList[0])
    else:
        permisosPrivacidadObject.setIdPrivacidadUsuario(userList[0])

    permisosPrivacidadObject.setMostrarCorreo(permisosPrivacidadList[1])
    permisosPrivacidadObject.setMostrarOrgPropias(permisosPrivacidadList[2])
    permisosPrivacidadObject.setMostrarOrgPertenece(permisosPrivacidadList[3])
    permisosPrivacidadObject.setMostrarRedesSociales(permisosPrivacidadList[4])
    permisosPrivacidadObject.setMostrarTelefono(permisosPrivacidadList[5])

    # Coneccting with Db Functions for insertPermisosPrivacidad

    functionObject = DbFunctionUser()
    result = functionObject.insertPermisosPrivacidad(permisosPrivacidadObject)

    return permisosPrivacidadObject


def socialNetworkRegister(userList,socialNetworkList):

    socialObject = Redessociales()

    if socialNetworkList[0] == "Generic":
        socialObject.setIdRedesSociales(socialNetworkList[0])
    else:
        socialObject.setIdRedesSociales(userList[0])
        socialObject.setIdRedesSociales(socialNetworkList[1])
        socialObject.setFaceBook(socialNetworkList[2])
        socialObject.setTwitter(socialNetworkList[3])
        socialObject.setLinkedin(socialNetworkList[4])
        socialObject.setGoogle(socialNetworkList[4])




    # Coneccting with Db Functions for socialNetworkRegister

    functionObject = DbFunctionUser()
    userInfo = functionObject.insertSocialNetworks(socialObject)


    return socialObject




def userRegister(userList,permisosPrivacidadList,socialNetworkList):

    # building the Object Social

    socialObject = socialNetworkRegister(userList,socialNetworkList)

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







userLogin(["jquiro12","asd123a"])
