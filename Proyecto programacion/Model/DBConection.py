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
        self.DB_NAME = 'spaceadmind'


    def run_query(self,query=''):
        print query
        datos = [self.DB_HOST,self.DB_USER, self.DB_PASS, self.DB_NAME] 
 
        conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
        cursor = conn.cursor()         # Crear un cursor 
        cursor.execute(query)          # Ejecutar una consulta 
 
        if query.upper().startswith('SELECT'):
            count = 0
            data = {}
            
            for datos in cursor.fetchall():  
                data[count] = datos
                count += 1
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
    



