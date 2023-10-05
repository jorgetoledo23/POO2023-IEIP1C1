import os
from ModelAppNotas import Alumno
from typing import List
print("Bienvenido al Sistema de Notas")

listaAlumnos:List[Alumno] = []

def BuscarAlumnoPorRut(rut:str):
    for alumno in listaAlumnos:
        if(alumno.Rut == rut):
            return alumno


while True:
    os.system("cls")
    print("[1] - Ingresar Alumno al Sistema")
    print("[2] - Ingresar Nota al Sistema")
    print("[3] - Ver Info Alumno")
    print("[4] - Ver Todos los Alumnos")
    print("[5] - Ver el Promedio de un Alumno")
    print("[0] - Salir")

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
        os.system("cls")
        rut = input("Ingresa Rut del Alumno: ")
        alumno = BuscarAlumnoPorRut(rut)
        if(alumno == None):
            input("Alumno NO Encontrado!")
        else:
            alumno.AddNota(float(input("Ingresa la Nota: ")))
            input("Nota Ingresada Correctamente!")
    
    if(op == "3"):
        os.system("cls")
        rut = input("Ingresa Rut del Alumno: ")
        alumno = BuscarAlumnoPorRut(rut)
        if(alumno == None):
            input("Alumno NO Encontrado!")
        else:
            alumno.getInfo()
            input()

    if(op == "5"):
        os.system("cls")
        rut = input("Ingresa Rut del Alumno: ")
        alumno = BuscarAlumnoPorRut(rut)
        if(alumno == None):
            input("Alumno NO Encontrado!")
        else:
            alumno.VerPromedio()
            input()