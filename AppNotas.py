import os
from ModelAppNotas import Alumno
from typing import List
print("Bienvenido al Sistema de Notas")

listaAlumnos:List[Alumno] = []
#listaAlumnos = []

while True:
    os.system("cls")
    print("[1] - Ingresar Alumno")
    print("[2] - Ingresar Nota")
    print("[3] - Ver Info Alumno")
    print("[4] - Ver Todos los Alumnos")
    op = input("Selecciona una Opcion: ")

    if(op == "1"):
        os.system("cls")
        r = input("Rut: ")
        n = input("Nombre: ")
        a = input("Apellido: ")
        listaAlumnos.append(Alumno(r,n,a))
        input("Alumno Ingresado!")

    if(op == "4"):
        for a in listaAlumnos:
            a.getNombre()
        input()

    if(op == "2"):
        #Ingreso de Notas
        pass