from Model.DBFunctions import DbFunctions

import mysql



class DbFunctionUser(DbFunctions):

    def actualizarRedesS(self,userPk,redesSocialesPk):
        print 'Usuario Db - actualizarRedesS'
        return self.update('Usuario', "idRedesSociales = '{}'".format(redesSocialesPk), "idUsuario = '{}'".format(userPk))

    def actualizarUsuario(self,list,pk):
        print 'Usuario Db - actualizarUsuario'

        #Suponiendo que van en un arrayList, en ese orden.
        sets = "nombreusuario = '{}', descripcion = '{}',telefonoCelular = '{}'".format(list[0],
                                                                                        list[1],
                                                                                        list[2])

        condicion = "idUsuario = '{}'".format(pk)

        return self.update("usuario", sets, condicion)



    def insertUser(self,userObject):
        print 'Usuario Db - insertUser'

        values = "'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}'".format(userObject.getIdUsuario(),
                                                                     userObject.getClaveUsuario(),
                                                                     userObject.getNombreUsuario(),
                                                                     userObject.getDescripcion(),
                                                                     userObject.getTelefonoCelular(),
                                                                     userObject.getCorreoElectronico(),
                                                                     userObject.getIdRedesSociales(),
                                                                     userObject.getIdPrivacidad(),
                                                                     userObject.getEstadoUsuario(),
                                                                          userObject.getFechaCreacion()
                                                        )
        result = ""
        try:
            result = self.insertInto("Usuario", values)
            return userObject

        except(mysql.connector.errors.IntegrityError), e:

            result = "ERROR: Tenemos problema de Integridad En Insertar usuario Registro"
            return None
        pass






'''''''''

#generqr Objeto

joder = DbFunctionUser()

objeto = joder.generarUsuario("Amanda17")
print objeto.getIdUsuario()

#

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


print joder.insertUser(Objeto)
'''''''''



