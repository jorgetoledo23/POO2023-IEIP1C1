class Universo:
    def __init__(self, cod:int, nombre:str) -> None:
        self.__CodigoUniverso = cod
        self.__NombreUniverso = nombre

    def getNombreUniverso(self)->str:
        return self.__NombreUniverso
    
    def getCodigoUniverso(self)->int:
        return self.__CodigoUniverso