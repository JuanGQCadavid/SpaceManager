from Model.DBFunctions import DbFunctions
from Model.Structures.UsuarioStructure import Usuario
import MySQLdb

class DbFunctionUser(DbFunctions):

    def actualizarUsuario(self,userObject):

        #Suponiendo que van en un arrayList, en ese orden.
        sets = "nombreusuario = '{}', descripcion = '{}',telefonoCelular = '{}'".format(userObject.getNombreUsuario(),
                                                                                        userObject.getDescripcion(),
                                                                                        userObject.getTelefonoCelular())

        condicion = "idUsuario = '{}'".format(userObject.getIdUsuario())

        return self.update("usuario",sets,condicion)


    def FormarUserObject(self,userList):
        #Creando Objeto
        userNewObject = Usuario(userList[0],userList[1],userList[2],
                                userList[3],userList[4],userList[5],
                                userList[6],userList[7],userList[8])


        #Rertornamos
        return userNewObject

    def ValidarUser(self, userObject):

        #Hacemos el Sq1
        Condicion = "idUsuario = '{}' AND claveUsuario ='{}'".format(userObject.getIdUsuario(),
                                                                                  userObject.getClaveUsuario())

        #Answer me guardara el resultado de la consulta
        answer =  self.selectWhere("*", "usuario", Condicion)



        #Si existe el usuario crearemos el objeto usuario que se movera en todo el sistena
        if not(answer  == {}):
            # Descomponer el diccionario en una sola tupla
            # Recordemos que la consulta nos entrega un diccionario

            user_info = answer[0]

            #Armaremos el objeto.
            userObject = self.FormarUserObject(user_info)
        else:
            #Si no existe dicho usuario, retornaremos el objeto como None
            userObject = None

        return userObject

        #La respuesta final es el Objeto usuario.

    def metodoPorDefinir(self,permisosPrivacidadObject):
        structure = "MostrarCorreo = {} AND MostrarOrgPropias  = {} AND" \
                    "MostrarOrgPertenece = {} AND MostrarRedesSociales = {} AND" \
                    "MostrarTelefono = {}".format(permisosPrivacidadObject.getMostrarCorreo(),
                                                  permisosPrivacidadObject.getMostrarOrgPropias(),
                                                  permisosPrivacidadObject.getMostrarOrgPertenece(),
                                                  permisosPrivacidadObject.getMostrarRedesSociales(),
                                                  permisosPrivacidadObject.getMostrarTelefono()
                                                  )

        result = self.insertInto("PrivacidadUsuario", structure)

        print result

    def insertUser(self,userObject):
        values = "'{}','{}','{}','{}','{}','{}','{}','{}',{}".format(userObject.getIdUsuario(),
                                                                     userObject.getClaveUsuario(),
                                                                     userObject.getNombreUsuario(),
                                                                     userObject.getDescripcion(),
                                                                     userObject.getTelefonoCelular(),
                                                                     userObject.getCorreoElectronico(),
                                                                     userObject.getIdRedesSociales(),
                                                                     userObject.getIdPrivacidad(),
                                                                     userObject.getEstadoUsuario()
                                                        )
        result = ""
        try:
            result = self.insertInto("usuario", values)
            return userObject

        except(MySQLdb.IntegrityError), e:

            result = "ERROR: Tenemos problema de Integridad En Insertar usuario Registro"
            return None
        pass







'''''''''
joder = DbFunctionUser()

Objeto = joder.FormarUserObject(("Amanda17","bandoleo","Maria Carmen","El perreo Intenso","585897841","mari@gmail.com","jquiro12","GenericF",0))

print joder.actualizarUsuario(Objeto)

joder.actualizarStatement("usuario","Amanda17","claveusuario","perreoIntenso",0)
joder.actualizarStatement("usuario","Amanda17","estadousuario",1,1)



        #Assignando valores
        userNewObject.setIdUsuario(userList[0])
        userNewObject.setClaveUsuario(userList[1])
        userNewObject.setNombreUsuario(userList[2])
        userNewObject.setDescripcion(userList[3])
        userNewObject.setTelefonoCelular(userList[4])
        userNewObject.setCorreoElectronico(userList[5])
        userNewObject.setIdRedesSociales(userList[6])
        userNewObject.setIdPrivacidad(userList[7])
        userNewObject.setEstadoUsuario(userList[8])

'''''''''