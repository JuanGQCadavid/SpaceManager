from Model.DBFunctions import DbFunctions
class DbFunctionUser(DbFunctions):


    def ValidarUser(self, userObject):
        Condicion = "usuarioUsuario = '{}' AND claveUsuario ='{}'".format(userObject.getUsuarioUsuario(),
                                                                          userObject.getClaveUsuario())

        return self.selectWhere("*", "usuario", Condicion)

    '''
    if permisosPrivacidadList[0] == "Generic":
        permisosPrivacidadObject.getIdPrivacidadUsuario(permisosPrivacidadList[0])
    else:
        permisosPrivacidadObject.getIdPrivacidadUsuario(userList[0])

    permisosPrivacidadObject.getMostrarCorreo(permisosPrivacidadList[1])
    permisosPrivacidadObject.getMostrarOrgPropias(permisosPrivacidadList[2])
    permisosPrivacidadObject.getMostrarOrgPertenece(permisosPrivacidadList[3])
    permisosPrivacidadObject.getMostrarRedesSociales(permisosPrivacidadList[4])
    permisosPrivacidadObject.getMostrarTelefono(permisosPrivacidadList[5])
    '''

    def metodoPorDefinir(self,permisosPrivacidadObject):
        condition = "MostrarCorreo = {} AND MostrarOrgPropias  = {} AND" \
                    "MostrarOrgPertenece = {} AND MostrarRedesSociales = {} AND" \
                    "MostrarTelefono = {}".format(permisosPrivacidadObject.getMostrarCorreo(),
                                                  permisosPrivacidadObject.getMostrarOrgPropias(),
                                                  permisosPrivacidadObject.getMostrarOrgPertenece(),
                                                  permisosPrivacidadObject.getMostrarRedesSociales(),
                                                  permisosPrivacidadObject.getMostrarTelefono()
                                                  )

        result = self.selectWhere("idPrivacidadUsuario", "PrivacidadUsuario", condition)

    def insertPermisosPrivacidad(self,permisosPrivacidadObject):
        #Buscar si hay un atributo con la mismas carateristicas
        Primarykey ="{}{}{}{}{}'".format(permisosPrivacidadObject.getMostrarCorreo(),
                                                  permisosPrivacidadObject.getMostrarOrgPropias(),
                                                  permisosPrivacidadObject.getMostrarOrgPertenece(),
                                                  permisosPrivacidadObject.getMostrarRedesSociales(),
                                                  permisosPrivacidadObject.getMostrarTelefono()
                                                  )


        if result == {}{}


    def insertSocialNetworks(self,socialObject):
        values = "'{}','{}','{}','{}','{}'".format(socialObject.getIdRedesSociales(),socialObject.getFaceBook(),
                                                   socialObject.getTwitter(),socialObject.getLinkedin(),
                                                   socialObject.getGoogle())
        return self.insertInto("RedesSociales",values)

    def insertUser(self,userObject):
        pass