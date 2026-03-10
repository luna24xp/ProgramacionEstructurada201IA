# Programa para determinar califaciones en USA
def calificaciones_usa():
    calificacion = float(input("Ingrese su calificación (0-100): "))
    
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

def main():
    calificaciones_usa()

if __name__ == "__main__":
    main()