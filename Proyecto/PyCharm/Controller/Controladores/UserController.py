# -*- coding: cp1252 -*-
from Controller.Controladores.PrivacidadUserController import actualizarPrivacidad
from Controller.Controladores.RedesSocialesController import actualizarRedesSociales
from Controller.DBFunctions.DBPrivacidad import DBFunctionPermisoPrivacidad
from Controller.DBFunctions.DBSocialNetwork import DBSocialNetwork
from  Controller.DBFunctions.DBUser import DbFunctionUser
from Model.Structures.UsuarioStructure import Usuario
import time


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
    '''''''''
        0 -> Cambio de Clave FUNCIONANDO
        4 -> Cambio de Estado FUNCIONANDO
        1 -> Cambio basico info usuario FUNCIONANDO
        2 -> Cambio basico Redoes Sciales 
        3 -> Cambio basico Privacidad usuario FUNCIONANDO
    '''''''''

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

def userLogin(userList):
    print 'usuario_Controller userLogin'

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

def userRegister (userList, permisosPrivacidadList, socialNetworkList) :
    print 'usuario_Controller userRegister'

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

    #Añadir fecha

    userList[9] = time.strftime("%Y-%m-%d") + " " + time.strftime("%X")
    print userList


    #Creando Objeto y guardando en MySQL.

    userObject = claseUsuario.FormarUserObject(userList)
    claseUsuario.insertUser(userObject)



'''''''''
actualizarInfo([None,None,None,None,None],2,'jquiro12')

userRegister(["pkUser","claveusuario","NombreUsuario","Descripcion","Telefono","CorreoElectronico","pkRS","pkIP",EstadoU,fechaCreacion],
             ["pkUser",MC,MOPRO,MOPERT,MRS,MT],['pkUser',"Face","Twitter","Linkelin","Instagram","Google"])

userRegister(["jquiro12","bandoleo","Juan Gonzalo","El perreo Intenso","3147703216","juangonzalo23@gmail.com","pk","pk",1,"fecha"],
             ["jquiro12",0,0,0,0,0],['jquiro12',None,None,None,None,None])
             
             
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
