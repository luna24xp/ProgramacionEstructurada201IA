#Diseñar algoritmo para generar una serie de números impares que generan una lista secuencial de los primeros N números impares (comenzando desde el 1).

def contador_impares(N):
    contador = 0
    numero = 1
    while contador < N:
        print(numero)
        numero += 2
        contador += 1
    
def main():
    N = int(input("Ingrese un numero: "))
    contador_impares(N)

if __name__ == "__main__":
    main()