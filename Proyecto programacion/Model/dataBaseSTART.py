from DBConection import DataBaseConection

#Definimos la clase.
classe = DataBaseConection()


def registrarPrivacidadUsaruaio():


    queryGenerricT= "INSERT INTO PrivacidadUsuario VALUES ('GenericT',1,1,1,1,1)"
    queryGenerricF= "INSERT INTO PrivacidadUsuario VALUES ('GenericF',0,0,0,0,0)"

    classe.run_query(queryGenerricT)
    classe.run_query(queryGenerricF)

def registrarRedesSociales():
    queryGenerricNull = "INSERT INTO redesSociales VALUES ('GenericNull',null,null,null,null,null)"
    classe.run_query(queryGenerricNull)



'''''''''
registrarRedesSociales()
registrarPrivacidadUsaruaio()
'''''''''