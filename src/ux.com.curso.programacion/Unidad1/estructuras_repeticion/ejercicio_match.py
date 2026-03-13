#  Implementacion de match en python

def demostracion():
    print("-- ejemplo de match --")
    opcion = input("ingresa una opcion (1, 2, 3): ")
    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            nombre = input("ingresa tu nombre: ")
            print(f"Hola {nombre}!")
        case "2":
            print("Opcion 2 seleccionada")
            Matricula = input("ingresa tu matricula: ")
            print(f"Tu matricula es: {Matricula}")
        case "3":
            print("Opcion 3 seleccionada")
            Semestre = input("ingresa tu semestre: ")
            print(f"Tu semestre es: {Semestre}")
        case _:
            print("Opcion no valida")
def main():
    demostracion()

if __name__ == "__main__":
    main()