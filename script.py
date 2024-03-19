import os
import time

def eliminar_capturas_antiguas(ruta_carpeta, antiguedad_meses):
    ruta_carpeta = os.path.abspath(ruta_carpeta)
    fecha_limite = time.time() - antiguedad_meses * 30 * 24 * 60 * 60  # Convertir meses a segundos
    capturas_eliminadas = False  # Variable para realizar un seguimiento de si se eliminó alguna captura

    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            fecha_modificacion = os.path.getmtime(ruta_archivo)
            if fecha_modificacion < fecha_limite:
                os.remove(ruta_archivo)
                capturas_eliminadas = True
                print("###########################################")
                print(f"Se ha eliminado el archivo: {ruta_archivo}")
                print("###########################################")

    if not capturas_eliminadas:
        print("##################################################")
        print("No se encontraron capturas antiguas para eliminar.")
        print("##################################################")

# Configuración
ruta_carpeta = r"C:\Pictures\Screenshots"
antiguedad_meses = int(input("Ingrese la antigüedad en meses de las capturas a eliminar: "))

# Llamada a la función para eliminar las capturas antiguas
eliminar_capturas_antiguas(ruta_carpeta, antiguedad_meses)
