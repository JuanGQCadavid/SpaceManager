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
        print "select"
        return self.run_query(query)

    def selectWhere(self,atributes, table, condition):
        query = "SELECT {} FROM {} WHERE {};".format(atributes, table, condition)
        print "selectWhere"
        return self.run_query(query)
    
    def insertInto(self, table, values) :
        query = "INSERT INTO {} VALUES ({});".format(table, values)
        print "insertInto"
        return self.run_query(query)


    def deleteFrom (self, table, condition) :
        query = "DELETE FROM {} WHERE {};".format(table, condition)
        print "deleteFrom"
        return self.run_query(query)

    def up(self, table, attrb, value, condicionColumna, condicionAtributo) :
        query = "UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, attrb, value, condicionColumna,condicionAtributo)
        print "up"
        return self.run_query(query)

    def update(self,table,sets,condition):
        query = "UPDATE {} SET {} WHERE {}".format(table,sets,condition)
        print "update"
        return self.run_query(query)

    def actualizarStatement(self,tabla,nombreColumnaPk,pk,colmnua,value,tipo):

        if(tipo == 0):
            sets = colmnua + " = '{}'".format(value)
        else:
            sets = colmnua + " = {}".format(value)

        where = nombreColumnaPk + " = '{}'" .format(pk)
        print "actualizarStatement"
        return self.update(tabla,sets,where)

    def star(self):
        return self.run_query('CALL DataStart ')


'''''''''
classe = DbFunctions()

classe.update("usuario","claveUsuario='ChoriseoX2'","idusuario = 'Amanda17'")

    
'''''''''