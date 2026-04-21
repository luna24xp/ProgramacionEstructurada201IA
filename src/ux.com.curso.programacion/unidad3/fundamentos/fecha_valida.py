# Programa que valida una fecha ingresada por el usuario
def fecha_valida():
    dia = int(input("Ingrese dia:"))
    mes = int(input("Ingrese mes:"))
    año = int(input("Ingrese año:"))

    if dia < 1 or dia > 31:
        print("Dia no valido")
    elif mes < 1 or mes > 12:
        print("Mes no valido")
    elif año < 0:
        print("Año no valido")
    else:
        print("Fecha valida")

def main():
    fecha_valida()

if __name__ == "__main__":
    main()
