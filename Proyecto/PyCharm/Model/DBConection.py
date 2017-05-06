# -*- coding: cp1252 -*-
import mysql.connector


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

        conn = mysql.connector.connect(user=self.DB_USER, password=self.DB_PASS,
                                        host=self.DB_HOST,
                                        database=self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(query)


 
        if query.upper().startswith('SELECT'):
            if query.find('obtenerConsecutivo')>= 0:
                return cursor.fetchone()
            else:
                return cursor.fetchall()



        elif query.upper().startswith('DESCRIBE'):
            data = []

            for datos in cursor.fetchall():
                data.append(datos[0])



        elif query.upper().startswith('SHOW'):
            data = []

            for datos in cursor.fetchall():
                datos = datos[0]
                data.append(datos[0].upper() + datos[1:])# Poner la primera letra en mayuscula

            
        else: 
            conn.commit()              # Hacer efectiva la escritura de datos 
            data = None 
 
        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 
 
        return data
    

'''
clase = DataBaseConection()

print clase.run_query("Select obtenerConsecutivo('Amanda178') as result")
print clase.run_query("Select * from usuario")
'''