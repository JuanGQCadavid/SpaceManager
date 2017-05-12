from Controller.DBFunctions.DBPermisos import DBPermisos


print 'Permisos Controlador'

'''
    El ID de permisos se basa en la combinacion de sus elementos.
    
    En las Listas no se incluye el espacio pk, ejemplo: [1,1,1,0,1,1,1,1,1,1,1]
'''

def validarPk (pk):
    # Formamos la clase.
    clasePermisoDB = DBPermisos()

    #Crearemos una consulta, si nos devuelve un registro, entonces ya esta, si no la creamos

    result = clasePermisoDB.obtenerPermisos(pk)
    return result != None

def generarPk(permisosList):
    pk = ""

    if permisosList[0] == 1:
        return 'theBoss'

    for campo in permisosList:
        pk += str(campo)
    return pk

def insertarPermiso(permisosList):
    #Formamos la clase.
    clasePermisoDB = DBPermisos()

    #Formamos la PK y la validamos
    pk = generarPk(permisosList)

    if not(validarPk(pk)):

        permisosList.insert(0, pk)
        clasePermisoDB.ObejtoInsertar(permisosList)
        return  pk

    return pk

def buscarPermiso(permisosPK):
    # Formamos la clase.
    clasePermisoDB = DBPermisos()
    return clasePermisoDB.obtenerPermisos(permisosPK)


def actualizarPermiso(permisosList):
    clase = DBPermisos()
    pk = generarPk(permisosList)
    if validarPk(pk):
        return pk
    else:
        permisosList.insert(0,pk)
        return clase.ObejtoInsertar(permisosList)



def eliminarPermiso(permisosPK):
    clase = DBPermisos()
    return clase.eliminarDB(permisosPK)



'''''''''

print insertarPermiso([0,1,1,0,1,1,0,1,1,1,1])
print actualizarPermiso([0,1,1,0,1,0,0,1,1,1,1])



#Test Eliminar

eliminarPermiso('01')

#Test Actualizar

permisosList = ['01',0,0,0,0,1,1,1,1,1,1]
actualizarPermiso(permisosList)

#Test Buscar

print buscarPermiso('01')

#Test Insertar

permisosList = ['01',0,1,1,1,1,1,1,1,1,1]


insertarPermiso(permisosList)

'''''''''
