import psycopg2
from cursor_del_pool import CursorDelPool
from logger_base import log

class GestorBaseDatos:
    def __init__(self, nombre_tabla, archivo_tsv):
        self.nombre_tabla = nombre_tabla
        self.archivo_tsv = archivo_tsv

    def crear_tabla(self):
        create_table = f"""
            CREATE TABLE IF NOT EXISTS {self.nombre_tabla} (
                id VARCHAR(100),
                site_id VARCHAR(100),
                title VARCHAR(100),
                price VARCHAR(100),
                sold_quantity VARCHAR(100),
                condition VARCHAR(100),
                thumbnail VARCHAR(100),
                created_date VARCHAR(8),
                PRIMARY KEY (id, created_date)
            )
        """
        try:
            with CursorDelPool() as cursor:
                cursor.execute(create_table)
                log.debug(f'Se creó la tabla {self.nombre_tabla}')
        except Exception as e:
            log.error(f'Ocurrió un error al crear la tabla: {e}')

    def copiar_datos(self):
        sql_copia = f"COPY {self.nombre_tabla} FROM stdin WITH CSV HEADER DELIMITER as '\t'"
        try:
            with CursorDelPool() as cursor:
                with open(self.archivo_tsv, 'r', encoding='utf-8') as file:
                    cursor.copy_expert(sql_copia, file)
                log.debug(f'Se copiaron los datos en la tabla {self.nombre_tabla}')
        except Exception as e:
            log.error(f'Ocurrió un error al copiar los datos: {e}')

if __name__ == '__main__':
    nombre_tabla = "consolas_ml"
    archivo_tsv = 'Python/Extraer_api_ML_SQL/file.tsv'

    gestor_bd = GestorBaseDatos(nombre_tabla, archivo_tsv)
    gestor_bd.crear_tabla()
    gestor_bd.copiar_datos()