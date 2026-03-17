# ejemplo de repeticion

def ejemplo_repeticion():
    print("estructura FOR")
    
    frutas = ["manzana", "banana", "naranja"]
    
    # for para listas
    for fruta in frutas:
        print(fruta)
    
    #for para iterar rangos
    for i in range(1,5):
        print(i)
        
    # for para iterar rangos con pasos
    for i in range(1,10,2):
        print(i)
        
# ejemplo de while
def ejemplo_while():
    print("estructura WHILE")
    
    contador = 0
    
    while contador < 5:
        print(contador)
        contador += 1

# simulacion de do while
def ejemplo_do_while():
    print("simulacion de DO WHILE")
    
    secreto = "python12"
    intentos = 0
    
    while True:
        intento_usuario = "python12" # simulamos la entrada del usuario
        intentos += 1
        
        if intento_usuario == secreto:
            print("¡Acceso concedido!")
            break
        else:
            print("¡Acceso denegado!, intente de nuevo.")
        print("\n")

def main():
    ejemplo_repeticion()
    print("\n")
    ejemplo_while()
    print("\n")
    ejemplo_do_while()  

if __name__ == "__main__":
    main()
