from Controller.DBFunctions.DBSocialNetwork import DBSocialNetwork


'''
    
    [FB,Twtter,Linkein,Intagram,Google]

'''

def actualizarRedesSociales(entidad_remitente_Pk,redes_Sociales_List):
    print 'Redes Sociales Controlador - actualizarRedesSociales'

    clase_DBSocial = DBSocialNetwork()

    redes_Sociales_List.insert(0,entidad_remitente_Pk)

    pk_Nueva = clase_DBSocial.generarPrimarykey(redes_Sociales_List)

    if entidad_remitente_Pk == pk_Nueva:
        clase_DBSocial.actualizarRedes(redes_Sociales_List)
        return entidad_remitente_Pk

    if pk_Nueva == 'GenericNull':
        clase_DBSocial.deleteFrom("redesSociales", "idRedesSociales = '{}'".format(entidad_remitente_Pk))
        return pk_Nueva
    else:
        redes_Sociales_List[0] = pk_Nueva
        return insertarRedesSociales(redes_Sociales_List)



def insertarRedesSociales(redesSocialesList):
    print 'Redes Sociales Controlador - insertarRedesSociales'

    clase = DBSocialNetwork()

    objetoSocial =clase.generarRedessocialesObject(redesSocialesList)
    clase.insertRedessociales(objetoSocial)

    return objetoSocial.getIdRedesSociales()


'''
def actualizarRedesSociales(pk,list):
    # Creamos la clase
    clase = DBSocialNetwork()

    # Generamos la PK

    list.insert(0,pk)

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
'''