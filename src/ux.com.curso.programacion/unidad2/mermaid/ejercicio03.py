#Diseñar algoritmo para generar una serie de números impares que generan una lista secuencial de los primeros N números impares (comenzando desde el 1).

N  = int(input("Ingrese el número de elementos de la serie de números impares: "))

contador = 0
numero= 1

while contador < N:
    print(numero)
    numero += 2
    contador += 1
