import os
from consult_api import Consulta_API
from Crear_tabla import GestorBaseDatos
from consultas import Consultas
#aclaración:cada vez que se usa la clase CursorDelPool, indirectamente se usa también la clase Conexion encargada del usuario,pasword, 
# port, de postgres
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Consulta la API de Mercado Libre y almacena los datos en un archivo TSV
consulta_api = Consulta_API() #creo un objeto de la clase Consulta_API
output_file = 'Python\Extraer_api_ML_SQL/file.tsv'
category_id = 'MLA438566'

# llamo al método de de la clase Consulta_API, se requiere pasar como argumentos
# el id de categoria de producto y la dirección en donde guardar
consulta_api.get_most_relevant_items_for_category(category_id, output_file) 


   

# 2. Crea una tabla en la base de datos PostgreSQL
nombre_tabla = "consolas_ml"
archivo_tsv = 'Python/Extraer_api_ML_SQL/file.tsv'
gestor_bd = GestorBaseDatos(nombre_tabla, archivo_tsv) #creo un objeto de la clase GestorBaseDatos y le asigno valores a dos atributos de clase
gestor_bd.crear_tabla() # el metodo crear tabla incluye la operacion de llamado a la otra clase "Cursordelpool" que gestiona los cursores y conexiones

# 3. Copia los datos desde el archivo TSV a la tabla creada
#Aqui tambien, esta clase realiza operaciones donde llama la clase "CursordelPool"
gestor_bd.copiar_datos()

# 4. Realiza consultas SQL en la base de datos
while True:
    clear_screen()  # Limpia la pantalla antes de mostrar el menú
    print("Menú de consultas:")
    print("1. Consulta personalizada")
    print("2. Salir")
    opcion = input("Ingrese la opción deseada: ")

    if opcion == '1':
        consulta = input("Ingrese su consulta SQL: ")
        # resultados es un objeto que contendra el resultado de la consulta una lista con el resultado, se llama al metodo seleccionar para ello.
        resultados = Consultas.seleccionar(consulta) 
        if resultados:#si el resultado de la consulta contiene información, la mostramos
            for fila in resultados:
                print(fila)
        else:
            print("No se encontraron resultados para la consulta.")
        input("Presione Enter para continuar...")
    elif opcion == '2':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("¡Hasta luego!")