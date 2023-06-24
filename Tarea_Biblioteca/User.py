from sys import path

path.append("..\\fernandal2693629")

from Account import *


class User(Account):
    def _init_(self , Name:str , ID:int, informacion):
        self._name = Name
        self.__id = ID
        self.__verificado = None
        self.__account  = informacion
        self.__informacion = {}
        Account._init_(self , Name , ID)
        
    
    def verify (self , Name:str, ID:int):
        if self.name == Name and self._id == ID:
            self.__verificado = "Verificado"
            return "Verificado"
        else:
            self.__verificado = "No Verificado"
            return "No Verificado"
            

    def CheckAccount (self, Name:str , Informacion:int):
        self.__account = Informacion
        print(Informacion)
    
    def get_book_info (self , Titulo:str , informacion):
        self.__informacion = informacion
        print(self.__informacion)