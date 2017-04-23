# -*- coding: cp1252 -*-

from Model.DBConection import DataBaseConection

class DbFunctions (DataBaseConection):
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

        query = "SELECT {} FROM {} WHERE {};".format(atributes, table, condition)


        query = "SELECT {} FROM {} WHERE {};".format(atributes,table,condition)
        print query

        return self.run_query(query)
    
    def insertInto(self, table, values) :
        query = "INSERT INTO {} VALUES ({});".format(table, values)
        print query
        return self.run_query(query)


    def deleteFrom (self, table, condition) :
        query = "DELETE FROM {} WHERE {};".format(table, condition)
        return self.run_query()

    def up(self, table, attrb, value, condicion) :
        query = "UPDATE {} SET {} = {} WHERE {}".format(table, attrb, value, condicion)
        return self.run_query()

    def update(self,table,sets,condition):
        query = "UPDATE {} SET {} WHERE {}".format(table,sets,condition)
        print query
        return self.run_query(query)

    def actualizarStatement(self,tabla,nombreColumnaPk,pk,colmnua,value,tipo):

        if(tipo == 0):
            sets = colmnua + " = '{}'".format(value)
        else:
            sets = colmnua + " = {}".format(value)

        where = nombreColumnaPk + " = '{}'" .format(pk)

        return self.update(tabla,sets,where)



'''''''''
classe = DbFunctions()

classe.update("usuario","claveUsuario='ChoriseoX2'","idusuario = 'Amanda17'")

    
'''''''''