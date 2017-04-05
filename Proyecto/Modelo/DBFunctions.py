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
    
    def insert(self):

        query = "insert into pais (idPais,nombreP) values ('03', 'Alemania Mostro ')"
        lista = {"pais":("idPais","nombreP")}

        query = "insert into pais {} values ('04', 'Alemania Renace ')".format(lista["pais"])
        print self.run_query(query)

    

    
exampleClass = DbFunctions()
print exampleClass.select("*","pais")
