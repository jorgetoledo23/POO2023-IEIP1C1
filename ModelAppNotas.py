class Alumno:

    def __init__(self, rut, nombre, apellido):
        self.Rut = rut
        self.Nombre = nombre.title()
        self.Apellido = apellido.title()
        self.Notas = []

    def getNombre(self):
        print(f"Alumno Rut: {self.Rut}, Nombre: {self.Nombre} {self.Apellido}")

    def getInfo(self):
        print(f"Alumno Rut: {self.Rut}, Nombre: {self.Nombre} {self.Apellido}")
        if(len(self.Notas) >= 1):
            count = 1
            for nota in self.Notas:
                print(f"Nota {count}: {nota}")
                count +=1
        else:
            input("No tienes notas")

    
    def AddNota(self, nota:float):
        self.Notas.append(nota)

    def VerPromedio(self):
        if (len(self.Notas) > 0):
            print(self.getNombre())
            total = 0
            for nota in self.Notas:
                total += nota
            print(f"Promedio: { total / len(self.Notas)  }")
            input()
        else:
            print(self.getNombre())
            input("El Alumno No posee Notas!")



