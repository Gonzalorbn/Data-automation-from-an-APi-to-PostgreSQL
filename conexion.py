from logger_base import log
from psycopg2 import pool
import sys
#clase para gestionar conexiones
class Conexion:
    _DATABASE = 'CURSO_PDE'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

#codigo para obtener un pool de conexiones
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:  #si pool es none entonces no ha sido inicializada
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn() #obtenemos un objeto de conexion hacia la base de datos
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)#regresa el objeto conexion que ya no usa cierto usuario al pool de conexiones
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()#se cierran todos los objetos de conexiones disponibles en el objeto pool

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion() # crea un pool de conexiones, y se solicita un objeto de conexion a partir del pool
    Conexion.liberarConexion(conexion1) #se libera ese objeto de conexion anterior
    conexion2 = Conexion.obtenerConexion() # se usa ese mismo objeto ya que esta liberado, podemos verlo ne memoria
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()

