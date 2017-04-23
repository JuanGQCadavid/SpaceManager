from DBFunctionPermisosPrivacidad import DBFunctionPermisoPrivacidad

#Objetos para compararlos

from Model.Structures.OrganizacionStructure import Organizacion
from Model.Structures.UsuarioStructure import Usuario


def actualizarPrivacidad(pk, PrivacidadList):

    #Creamos la clase
    clase = DBFunctionPermisoPrivacidad()


    #Generamos la PK

    PrivacidadList[0] = pk


    #Generamos la PK, para ver si es Generic T or F o si es una propia
    primaryKey = clase.generarPrimarykey(PrivacidadList)

    # Creamos el objeto
    objetoPrivacida = clase.generarPrivacidadObject(PrivacidadList)

    #Guardamos el id viejo para ir a borrarlo
    print primaryKey

    if primaryKey == "GenericF" :
        clase.up("usuario","idPrivacidad","GenericF","idUsuario",pk)
    elif primaryKey == "GenericT":
        clase.up("usuario", "idPrivacidad", "GenericT", "idUsuario", pk)
    else:
        #Insertamos el Registro de Privacidad Nuevo
        clase.insertPermisosPrivacidad(objetoPrivacida)
        #Actualizamos el reguistro de usuario
        clase.up("usuario", "idPrivacidad", primaryKey, "idUsuario", pk)

    #Eliminamos el Registro de Privacidad Anterior

    if pk == "GenericF" or pk == "GenericT":
        #No hay nada mas que hacer, el trabajo quedo echo.
        pass
    else:
        #Eliminamos el registro pasado.
        if primaryKey != pk:
            #Eliminamos el registro pasado.
            clase.deleteFrom("privacidadUsuario", "idPrivacidadUsuario = '{}'".format(pk))


    pass





'''''''''
#Creamos los Objetos, para saber a que tipo de clase, estamos comprando
    objetoOrg = Organizacion()
    objetoUser = Usuario()


    #Creamos la clase
    clase = DBFunctionPermisoPrivacidad()


    #Generamos la PK y la clausura Where

    if object.__class__ ==  objetoUser.__class__ :
        PrivacidadList[0] = object.getIdPrivacidadUsuario()

    else:
        PrivacidadList[0] = object.getIdOrganizacion()
        
'''''''''



