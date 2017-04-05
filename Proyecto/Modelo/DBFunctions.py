# -*- coding: cp1252 -*-

from DBConection import DataBaseConection

class DbFunctions(DataBaseConection):
    def __init__(self):
        self.createDBData()
        pass

    def generateMap(self):

        self.Diccionario = {"pais":("idPais","nombreP")}
        
    def select(self, atributes ,table):
        
        query = "SELECT {} FROM {}".format(atributes,table)
        return self.run_query(query)
    
    def insert(self,country, values):

        
        lista = {"pais":("idPais","nombreP")}

        query = "insert into {} values {}".format(country,values)#,lista[country])
        print self.run_query(query)

    

    
exampleClass = DbFunctions()
exampleClass.insert("pais",('111"', 'Geortge'))
print exampleClass.select("*","pais")
