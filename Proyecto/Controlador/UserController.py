# -*- coding: cp1252 -*-
from DBFunctions import DbFunctions

def userLogin(UserObject):
    startObject = DbFunctions()

    answer = DbFunctions.selectWhere(UserObject.getIdUsuario() , "")

    pass