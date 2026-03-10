# Programa para determinar califaciones en USA
"""
Se define la funcion para determinar las calificaciones
"""
def calificaciones_usa():
    calificacion = float(input("Ingrese su calificación (0-100): "))
    
    """ 
    Se establecen las condiciones para determinar la calificación
    """
    
    if calificacion >= 90:
        print("Su calificación es: A")
    elif calificacion < 90 and calificacion >= 80:
        print("Su calificación es: B")
    elif calificacion < 80 and calificacion >= 70:
        print("Su calificación es:  C")
    elif calificacion < 70 and calificacion >= 69:
        print("Su calificación es: D")
    else:
        print("Su calificación es: F")

# Definicion de la funcion main para iniciar el programa
"""
Definicion de la funcion principal del programa para iniciar el contador de dispositivos
"""
def main():
    calificaciones_usa()
    
# Llamada a la funcion main para iniciar el programa

if __name__ == "__main__":
    main()