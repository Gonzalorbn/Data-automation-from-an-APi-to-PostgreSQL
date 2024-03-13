from conexion import Conexion
from cursor_del_pool import CursorDelPool
from logger_base import log

class Consultas:
  
    @classmethod
    def seleccionar(cls, query):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando')
            cursor.execute(query)
            registros = cursor.fetchall()
            return registros       

if __name__ == '__main__':
    # Solicitar la consulta al usuario
    consulta = input("Ingrese su consulta SQL: ")
   
    # Seleccionar objetos
    consolas = Consultas.seleccionar(consulta)

    ancho = 15
    for fila in range(len(consolas)):
        for columna in range(len(consolas[fila])):
            log.debug(consolas[fila][columna])         
            print(f'{consolas[fila][columna]:<{ancho}} |', end=" ")
        print("\n")