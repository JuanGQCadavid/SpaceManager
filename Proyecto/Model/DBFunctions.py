# -*- coding: cp1252 -*-

from Model.DBConection import DataBaseConection

class DbFunctions(DataBaseConection):
    def __init__(self):
        self.createDBData()
        pass

    def generateMap(self):
        #Falta
        self.Diccionario = {"pais":("idPais","nombreP")}
        
    def select(self, atributes ,table):
        #Listo
        query = "SELECT {} FROM {}".format(atributes,table)
        return self.run_query(query)

    def selectWhere(self,atributes, table, condition):
        query = "SELECT {} FROM {} WHERE {};".format(atributes,table,condition)

        return self.run_query(query)
    
    def insert(self,country, values):
        #Falta
        
        lista = {"pais":("idPais","nombreP")}

        query = "insert into {} values {}".format(country,values)#,lista[country])
        print self.run_query(query)

    def getTables(self):
        #Listo
        query = "SHOW TABLES"
        return self.run_query(query)

    def getColumns(self, table):
        #Listo
        query = "DESCRIBE {}".format(table)
        return self.run_query(query)
    
