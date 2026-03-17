import math

# demostracion del uso de funciones de math

def mostrar_funciones_math(numero):
    #crear una variable
    
    sen_x = math.sin(numero)
    cos_x = math.cos(numero)
    
    print(f"El seno de {numero} es: {sen_x}")
    print(f"El coseno de {numero} es: {cos_x}")

    resultado = sen_x ** 2 + cos_x ** 2
    print(f"El resultado de sen^2 + cos^2 es: {resultado}")
    
def main():
    numero = float(input("Ingrese un numero para calcular su seno y coseno: "))
    mostrar_funciones_math(numero)
    
if __name__ == "__main__":
    main()
