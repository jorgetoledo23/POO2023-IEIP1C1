import os
from Modelo import Universo
from ConexionBaseDatos import DAO

dao = DAO()

while True:
    os.system("cls")
    print("[1] - Agregar un Universo")
    print("[2] - Ver Universos Almacenados")
    print("[3] - Actualizar un Universo")

    opcion = input("Ingresa una Opcion: ")

    if(opcion == "1"):
        os.system("cls")
        n = input("Ingresa el nombre del Universo:  ")
        u = Universo(0, n)
        dao.GuardarUniverso(u)
        input("Universo Guardado! Presiona ENTER para continuar...")

    if(opcion == "2"):
        os.system("cls")
        for u in dao.LeerUniversos():
            print(u.getNombreUniverso())
        input("\nUniversos Listados! Presiona ENTER para continuar...")

    if(opcion == "3"):
        os.system("cls")
        for u in dao.LeerUniversos():
            print(f"{u.getCodigoUniverso()} | {u.getNombreUniverso()}")
        cod = input("Cual Universo necesitas Actulizar? (Ingresa su Codigo): ")
        n = input("Ingresa el nuevo nombre para ese Universo: ")
        u = Universo(cod,n)
        dao.ActualizarUniverso(u)
        input("Universo Actualizado! Presiona ENTER para continuar...")

    if(opcion == "4"):
        pass
    #Eliminar Universo 