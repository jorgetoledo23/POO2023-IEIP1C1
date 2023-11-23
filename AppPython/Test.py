#pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode
import os
from typing import List

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user="root",
                password="root",
                host="localhost",
                database="universos"
            )
            #print("Conexion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos NO existe")
            else:
                print(err)

#Insertar 12 Registros a la Tabla Universos

class Universo:

    def __init__(self, cod, nombre) -> None:
        self.__Cod_Universo = cod
        self.__NombreUniverso = nombre

    def getNombre(self)->str:
        return self.__NombreUniverso
    
    def getCodigo(self)->str:
        return self.__Cod_Universo

dao = DAO()

while True:
    os.system("cls")
    print("{Opcion 1} . Ingresar Nuevo Universo")
    print("{Opcion 2} . Ver Universos Ingresados")

    op = input("Selecciona una Opcion: ")
    if(op=="1"): #Insertar
        pass
    if(op=="2"): #Leer
        pass