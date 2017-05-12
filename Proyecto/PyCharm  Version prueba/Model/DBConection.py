# -*- coding: cp1252 -*-

import MySQLdb


class DataBaseConection(object):
    '''
        Esta clase se encarga de generar
        y mantener todo lo relacionado con
        la base de datos.
        
    '''
    def __init__(self):
         self.createDBData()

    def createDBData(self):
        self.DB_HOST = '127.0.0.1' 
        self.DB_USER = 'adminMySpace'
        self.DB_PASS = 'asd123'
        self.DB_NAME = 'SpaceAdmind'


    def run_query(self,query=''):


        print query

        datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]

        conn = MySQLdb.connect(*datos)
        cursor = conn.cursor()
        cursor.execute(query)


        if query.upper().startswith('SELECT'):
            try:
                resp =  cursor.fetchall()
            except(MySQLdb.Error), e:
                resp = cursor.fetchone()

            conn.commit()  # Hacer efectiva la escritura de datos
            return resp


        elif query.upper().startswith('DESCRIBE'):
            data = []

            for datos in cursor.fetchall():
                data.append(datos[0])
            return data



        elif query.upper().startswith('SHOW'):
            data = []

            for datos in cursor.fetchall():
                datos = datos[0]
                data.append(datos[0].upper() + datos[1:])# Poner la primera letra en mayuscula
            return data


        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 
 

    

'''
clase = DataBaseConection()

print clase.run_query("Select obtenerConsecutivo('Amanda178') as result")
print clase.run_query("Select * from usuario")
'''