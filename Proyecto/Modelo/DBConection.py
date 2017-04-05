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
        
        datos = [self.DB_HOST,self.DB_USER, self.DB_PASS, self.DB_NAME] 
 
        conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
        cursor = conn.cursor()         # Crear un cursor 
        cursor.execute(query)          # Ejecutar una consulta 
 
        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()   # Traer los resultados de un select 
        else: 
            conn.commit()              # Hacer efectiva la escritura de datos 
            data = True 
 
        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 
 
        return data



