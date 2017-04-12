# -*- coding: cp1252 -*-
from  Model.DBFunctions import DbFunctions

from Model.Usuario import Usuario


def userLogin(UserObject):
    startObject = DbFunctions()

    Condicion = "usuarioUsuario = '{}' AND claveUsuario ='{}'".format(UserObject.getUsuarioUsuario(),UserObject.getClaveUsuario())


    answer = startObject.selectWhere("*","usuario" ,Condicion)

    if not(answer == {}):
        print "Welcom to the Jungle!"
    else:
        print "No parse, no lo puedo dejar pasar"



objectToUsed = Usuario()
objectToUsed.setUsuarioUsuario("jquiro12")
objectToUsed.setClaveUsuario("asd123")

userLogin(objectToUsed)
