#  Implementacion de match en python
def dias():
    print("-- dias de la semana --")
    opcion = input("ingresa una opcion (1, 2, 3, 4, 5, 6, 7): ")
    match opcion:
        case "1":
            print("Lunes")
        case "2":
            print("Martes")
        case "3":
            print("Miercoles")
        case "4":
            print("Jueves")
        case "5":
            print("Viernes")
        case "6":
            print("Sabado")
        case "7":
            print("Domingo")
        case _:
            print("No valido")
def main():
    dias()

if __name__ == "__main__":
    main()
    

