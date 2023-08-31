#POO
#Programacion Orientada a Objetos

nombre = "Jorge"
asignatura = "POO"

def Sumar(x,y):
    return x + y

if(nombre == "Jorge"):
    print("Bienvenido")
    Sumar(1,2)





class Persona:
    #Atributos
    Rut = None
    Nombre = None
    Apellido = None
    Edad = None

    #Metodos
    def CambiarClave():
        pass

    def RecuperClave():
        pass

class Alumno(Persona):
    CodigoMatricula = None

    def VerNotas():
        pass

class Profesor(Persona):
    CodigoContrato = None

    def IngresarNota():
        pass

class Trabajador(Persona):
    NTarjeta = None


class Repuesto:
    Valor = None
    Nombre = None
    Codigo = None





Boleta
Factura
Venta
Cliente
Vendedor
Producto 

Doctores
AtencionMedica
Examen
Medicamento
Asistente

Alumnos
Profesores
JefeCarrera
Asignaturas
Secciones
Carreras


#Taller Mecanico
Vehiculos
Clientes
Mecanico
Herramientas
Repuestos
Auxiliar
Boleta
Reparacion 



#Instancia

DocenteJorge = Profesor()
DocenteCesar = Profesor()


DocenteJorge.CambiarClave()
DocenteCesar.IngresarNota()