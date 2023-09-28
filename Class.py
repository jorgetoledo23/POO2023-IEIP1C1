class Usuario:

    def __init__(self, id, nombre,correo, password, telefono, privacidad):
        self.Id = id
        self.Nombre = nombre
        self.Correo = correo
        self.Telefono = telefono
        self.Password = password
        self.ListaSeguidos = []
        self.ListaSeguidores = []
        self.PostGuardados = []
        self.Privacidad = privacidad


    def GuardarPost(self, post):
        self.PostGuardados.append(post)

    def Seguir(self, user):
        self.ListaSeguidos.append(user)
        user.ListaSeguidores.append(self)

    def verSeguidores(self):
        print(f"Tienes un total de {len(self.ListaSeguidores)} Seguidores")
        for seguidor in self.ListaSeguidores:
            print(f"{seguidor.Nombre}")
    def verSeguidos(self):
        print(f"Tienes un total de {len(self.ListaSeguidos)} Seguidos")
        for seguido in self.ListaSeguidos:
            print(f"{seguido.Nombre}")

    #Generar el Metodo para dar UnFollow (Dejar de Seguir)
    def UnFollow(self, user):
        input(f"Dejaste de Seguir a {user.Nombre}")
        self.ListaSeguidos.remove(user)
        user.ListaSeguidores.remove(self)
        

import os
os.system("cls")

hinchaX = Usuario(1234, "Pedrito", "pedroPunk17@gmail.com", "12345", "+56912345678", "publico")
cuentaColoColo = Usuario(5674, "ColoColoOficial", "colocolochile@colocolo.cl", "asyzxYash#", "+56285478963", "publico")
anita = Usuario(1234, "AnaMaria", "pedroPunk17@gmail.com", "12345", "+56912345678", "publico")

hinchaX.Seguir(cuentaColoColo)
anita.Seguir(cuentaColoColo)

for cuenta in anita.ListaSeguidos:
    print(cuenta.Nombre)

input()

anita.UnFollow(cuentaColoColo)

#hinchaX.verSeguidos()
cuentaColoColo.verSeguidores()
