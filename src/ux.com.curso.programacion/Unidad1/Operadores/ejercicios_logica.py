# ejercicio de operadores logicos 

def operaradores():
    a = True
    b = False

    print (a and b)
    print (a or b)
    print (not a)
    print (not b)

    numero_1 = 10
    numero_2 = 20

    if numero_1 > numero_2:
        print ("numero 1 es mayor que numero 2")
    else:
        print ("numero 1 no es mayor que numero 2")

def main():
    operaradores()

if __name__ == "__main__":
    main()