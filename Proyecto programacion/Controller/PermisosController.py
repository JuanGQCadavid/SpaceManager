from DBPermisos import DBPermisos
from DBFunctionUser import DbFunctionUser

#Funcionando Test 25 de Abril
def insertarPermiso(permisosList):
    #Formamos la clase.
    clasePermisoDB = DBPermisos()

    #Formamos el objeto y lo creamos en la BD
    return clasePermisoDB.ObejtoInsertar(permisosList)

#Funcionando Test 25 de Abri
def buscarPermiso(permisosPK):
    # Formamos la clase.
    clasePermisoDB = DBPermisos()
    return clasePermisoDB.obtenerPermisos(permisosPK)

#Funcionando Test 25 de Abri
def actualizarPermiso(permisosList):
    clase = DBPermisos()
    return clase.actualizarPermisosDB(permisosList)

#Funcionando Test 25 de Abri
def eliminarPermiso(permisosPK):
    clase = DBPermisos()
    return clase.eliminarDB(permisosPK)



#Test Eliminar

eliminarPermiso('01')


'''''''''

#Test Actualizar

permisosList = ['01',0,0,0,0,1,1,1,1,1,1]
actualizarPermiso(permisosList)

#Test Buscar

print buscarPermiso('01')

#Test Insertar

permisosList = ['01',0,1,1,1,1,1,1,1,1,1]


insertarPermiso(permisosList)

'''''''''