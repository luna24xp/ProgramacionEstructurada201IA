# Ejemplo de una simulación de entrenamiento por lotes

"""
Se define la función
"""
def simulacion_entrenamiento_lotes():
    tam_lotes = int(input("Ingrese el tamaño del lote de tensores: "))
    
    """
    Se establece la condición para prevenir el error "out of memory"
    """
    if tam_lotes >= 2500:
        print(f"El tamaño del lote de tensores es: {tam_lotes}")
        print("El proceso de carga de ha detenido debido a que el tamaño del lote es demasiado grande.")
    else:
        print(f"El tamaño del lote de tensores es: {tam_lotes}")
        print("El proceso se ha iniciado correctamente.")

# Definición de la función main para iniciar el programa
"""
Definicion de la funcion principal del programa
"""
def main():
    simulacion_entrenamiento_lotes()
    
# Llamada a la funcion main para iniciar el programa

if __name__ == "__main__":
    main()