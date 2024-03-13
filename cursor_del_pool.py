from logger_base import log
from conexion import Conexion
# El propósito principal es proporcionar un manejo más limpio y seguro de las operaciones de base de datos, 
# incluyendo la gestión de transacciones y liberación de recursos.Simplifica el manejo y transacciones de base de datos.
class CursorDelPool:
    """
    Gestiona conexiones y cursores en un contexto With
    """
    def __init__(self):
        self._conexion = None
        self._cursor = None

    #este metodo se encarga de obtener una conexion
    def __enter__(self):
        """
        Se obtiene una conexión de la piscina de conexiones utilizando la clase Conexion 
        La conexión se almacena en el atributo _conexion.
        Se crea un cursor asociado a la conexión y se almacena en el atributo _cursor.
        Finalmente, el método devuelve el cursor, lo que permite su uso dentro del bloque with.
        """
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    #el metodo exit se manda a llamar al finalizar el bloque with, y se hace commit o rollback
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        """
        si valor de exepcion es diferente de nulo significa que hubo una excepción,y se debe hacer rollback para desacer 
        cambios en la transacción y registrando el error.
        Si no hubo excepción se realiza commit para confirmar los cambios.
        """
        log.debug('Se ejecuta método __exit__')
        if valor_excepcion: 
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción, se hace un rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

#PRUEBA DE OBJETO CURSOR
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())