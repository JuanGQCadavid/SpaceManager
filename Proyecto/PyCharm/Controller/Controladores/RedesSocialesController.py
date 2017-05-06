from Controller.DBFunctions.DBSocialNetwork import DBSocialNetwork
print 'Redes Sociales Controlador'

def actualizarRedesSociales(pk,list,tablaReferente):
    # Creamos la clase
    clase = DBSocialNetwork()

    # Generamos la PK

    list[0] = pk

    # Generamos la PK, para ver si es GenericNull o si es una propia
    primaryKey = clase.generarPrimarykey(list)

    print primaryKey
    # Creamos el objeto
    objetoRedesSociales = clase.generarRedessocialesObject(list)

    # Guardamos el id viejo para ir a borrarlo

    #Eliminamos el Registro de Privacidad Anterior

    if pk == "GenericNull":
        #No hay nada mas que hacer, el trabajo quedo echo.
        pass
    else:
        if primaryKey != pk:
            #Eliminamos el registro pasado.
            clase.deleteFrom("redesSociales","idRedesSociales = '{}'".format(pk))

    return primaryKey

def insertarRedesSociales(redesSocialesList):
    clase = DBSocialNetwork()
    objetoSocial =clase.generarRedessocialesObject(redesSocialesList)
    clase.insertRedessociales(objetoSocial)
    return objetoSocial.getIdRedesSociales()