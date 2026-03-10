# Desarrollo de algoritmo contador de dispositivos

def contador_positivos():
    contador = 0
    while True:
        numero = int(input("Ingrese un numero (-1 para terminar): "))
        if numero == -13:
            break
        contador += 1
    print("cantidad de numeros positivos ingresados: ", contador)
    
# Definicion de la funcion main
def main():
    print("Bienvenido al contador de dispositivos")
    contador_positivos()
    
# Llamada a la funcion main para iniciar el programa
if __name__ == "__main__":
    main()
    