# -*- coding: cp1252 -*-
import time


from Model.DBFunctions import DbFunctions

class GeneradorCodigo(DbFunctions) :
    def __init__(self) :
        self.createDBData()
        self.dictionaryFiles = {}
        self.generar()
        
    def createFile (self, name, text) :
        newFile = open("{}Structure.py".format(self.mayusculaPrimerCaracter(name)),"w")
        newFile.write(text)
        newFile.close()

        self.dictionaryFiles[name] = "{}Model.py".format(name)

    def generar (self):
        Tables = self.getTables()
        result = ''
        
        for table in Tables:
            result = ''
            columns = self.getColumns(table)
            
            
            result += self.generarEncabezado(table) + '\n'
            result += self.constructor(columns) + '\n'
            result += self.gettersAndSetters(columns) + '\n'
            result += self.piedePagina()
            self.createFile(table, result)
            
            
      

    def generarEncabezado (self, tableName):
        meta = "# -*- coding: cp1252 -*- \n"
        classDeclaration = "class {}({}):\n".format(tableName,"object")
        classDeclaration += "\t'''\n\tClase con Constructor, Getters y Setters\n\tde la relacion {}\n\t'''".format(tableName)

        return meta + classDeclaration
    

    def constructor (self, columns):
        #Vacio
        #constructor = '\t#Constructor vacio \n'
        #constructor += '\tdef __init__(self):\n'
        #constructor += "\t'''\n\tConstructor por defecto, valores nulos.\n\t'''\n"
        '''
        atributos = ''
        
        for atribute in columns:
            atributos += '\t\tself.{}\n'.format(self.minusculasPrimerCaracter(atribute))

        constructorDefault = (constructor + atributos) + "\n"

        #Con paramatros
        
        linea = 'self'
        atributos = ''
        
        
        for atribute in columns:
            linea += ', '+ atribute
            atributos += '\t\tself.{A} = {A} \n'.format(A = self.minusculasPrimerCaracter(atribute))
        '''
        
        lineaS = 'self'
        atributos = ''
        #lineaC = 'self'

        for atribute in columns:
            atribute = self.minusculasPrimerCaracter(atribute)
            lineaS += ', '+ atribute +'= None'
            #lineaC += ', '+ atribute
            atributos += '\t\tself.{A} = {A} \n'.format(A = self.minusculasPrimerCaracter(atribute))

        
        constructor = '\t#Constructor con paso de parametros \n'
        constructor += '\tdef __init__({}):\n'.format(lineaS)
        #constructor += "'''\n\tConstructor por paso de valaores por parametros\n\t'''\n"
        
        constructorFull = (constructor + atributos) + "\n"
        return constructorFull
        #return (constructorDefault + constructorFull) + "\n"


    def gettersAndSetters(self,columns):

        line = ''
        
        for columna in columns:
            
            #Getters
            line +='\t#Getters y Setters de {}\n'.format(self.minusculasPrimerCaracter(columna))
            line += '\n'
            line +='\tdef get{}(self):\n'.format(self.mayusculaPrimerCaracter(columna))
            line +='\t\treturn self.{}\n'.format(self.minusculasPrimerCaracter(columna))

            #Setters
            
            line +='\tdef set{}(self,{}):\n'.format(self.mayusculaPrimerCaracter(columna),self.minusculasPrimerCaracter(columna))
            line +='\t\tself.{A} = {A}\n'.format(A = self.minusculasPrimerCaracter(columna))
            line += '\n\n\n'

        return line

    def piedePagina(self):
        
        #time.strftime("%H:%M:%S") #Formato de 24 horas
        #Tomado de http://www.pythondiario.com/2014/05/obtener-fecha-y-hora-actual-en-python.html
        return  "#Autogenerado: " + time.strftime("%c")
        
    
    

    def mayusculaPrimerCaracter(self, caracter):
        if caracter[0] == caracter[0].upper:
            return caracter
        else:
            caracter = caracter[0].upper() + caracter[1:]
            return caracter

    def minusculasPrimerCaracter(self, caracter):
        if caracter[0] == caracter[0].lower:
            return caracter
        else:
            caracter = caracter[0].lower() + caracter[1:]
            return caracter
        
SePrendioEstaMierda = GeneradorCodigo()
