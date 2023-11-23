import mysql.connector
from Modelo import Universo
from typing import List

class DAO: #Data Access Object
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='universos')
        
    def GuardarUniverso(self, u:Universo):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO universos "
               "(nombre) "
               "VALUES (%s)")
        data = (u.getNombreUniverso(),)
        cursor.execute(query, data)
        self.cnx.commit()

    def LeerUniversos(self)->List[Universo]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM universos")
        cursor.execute(query)
        listaUniversos:List[Universo] = []
        for (cod, nombre) in cursor:
            u = Universo(cod, nombre)
            listaUniversos.append(u)
        return listaUniversos

    def ActualizarUniverso(self, u:Universo):
        cursor = self.cnx.cursor()
        query = ("UPDATE universos SET nombre = %s WHERE cod_universo = %s")
        data = (u.getNombreUniverso(), u.getCodigoUniverso())
        cursor.execute(query, data)
        self.cnx.commit()
