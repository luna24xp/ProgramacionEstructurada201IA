# programa para simular la configuración de frecuencias multi-agente
"""
Se define la función
"""
def frecuencias_multi_agente():
    
    """
    Se solicita al usuario ingresar las frecuencias de los agentes
    """
    while True:
        frecuencia1 = int(input("Ingrese la frecuencia del agente A (en Hz): "))
        frecuencia2 = int(input("Ingrese la frecuencia del agente B (en Hz): "))
        
        """
        Se establece la condición para verificar si las frecuencias son divisores  entre si 
        """
        if frecuencia1 % frecuencia2 == 0 or frecuencia2 % frecuencia1 == 0:
            print("Relación de sincronización de ciclos perfecta para el intercambio de mensajes.")
            break
        else:
            print("Las frecuencias no son validas. Intente de nuevo.")
        

# Definición de la función main para iniciar el programa
"""
Definicion de la funcion principal del programa
"""
def main():
    frecuencias_multi_agente()
    
# Llamada a la funcion main para iniciar el programa

if __name__ == "__main__":
    main()
    
    