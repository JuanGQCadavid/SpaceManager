from Model.DBFunctions import DbFunctions
from Model.Structures.UsuarioStructure import Usuario
class DbFunctionUser(DbFunctions):

    def FormarUserObject(self,userList):
        #Creando Objeto
        userNewObject = Usuario()

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







    def insertSocialNetworks(self,socialObject):
        values = "'{}','{}','{}','{}','{}'".format(socialObject.getIdRedesSociales(),socialObject.getFaceBook(),
                                                   socialObject.getTwitter(),socialObject.getLinkedin(),
                                                   socialObject.getGoogle())
        return self.insertInto("RedesSociales",values)

    def insertUser(self,userObject):
        pass