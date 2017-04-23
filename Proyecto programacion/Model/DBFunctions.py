# -*- coding: cp1252 -*-

from Model.DBConection import DataBaseConection

class DbFunctions(DataBaseConection):
    def __init__(self):
        self.createDBData()
        pass

    #Creados para Generar Codigo
    def getTables(self):
        #Listo
        query = "SHOW TABLES"
        return self.run_query(query)

    def getColumns(self, table):
        #Listo
        query = "DESCRIBE {}".format(table)
        return self.run_query(query)

    #Querys generales


    def select(self, atributes ,table):
        query = "SELECT {} FROM {}".format(atributes,table)
        return self.run_query(query)

    def selectWhere(self,atributes, table, condition):
        query = "SELECT {} FROM {} WHERE {};".format(atributes,table,condition)

        return self.run_query(query)
    
    def insertInto(self,table,values) :
        query = "INSERT INTO {} VALUES ({});".format(table, values)
        print query
        return self.run_query(query)
        



    
