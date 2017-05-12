from Model.DBConection import DataBaseConection
from Model.Structures.UsuarioStructure import Usuario

class UsuarioDBF(DataBaseConection):

    def formarUserObject(self,userList):
        print 'Usuario Db - FormarUserObject'

        #Creando Objeto
        userNewObject = Usuario(idUsuario= userList[0], claveUsuario= userList[1],
                                nombreUsuario= userList[2], descripcion= userList[3],
                                telefonoCelular= userList[4], correoElectronico= userList[5],
                                idRedesSociales= userList[6], idPrivacidad= userList[7],
                                estadoUsuario= userList[8], fechaCreacion= userList[9])

        #Rertornamos
        return userNewObject

    def userLogin(self,idUser,claveUser):

        return  self.run_query("SELECT login_Usuario('{}','{}');".format(idUser,claveUser))[0][0]

    def insertarUsuario(self,idUsuario, claveUsuario, nombreUsuario ,descripcion, telefonoCelular ,
                        correoElectronico ,idRedesSociales ,idPrivacidad ):

        return self.run_query("SELECT insertar_Usuario('{}','{}','{}','{}','{}','{}','{}','{}');".format(idUsuario,
                                                                                                              claveUsuario,
                                                                                                              nombreUsuario,
                                                                                                              descripcion,
                                                                                                              telefonoCelular,
                                                                                                              correoElectronico,
                                                                                                              idRedesSociales,
                                                                                                              idPrivacidad))[0][0]

    def obtenerUsuario(self,user_PK):
        print 'Usuario Db - ObtenerUsuario'

        respuesta = self.run_query("CALL obtener_Usuario('{}');".format(user_PK))

        if respuesta != None:
            return respuesta[0]


clase =UsuarioDBF()

print clase.userLogin('0','1')