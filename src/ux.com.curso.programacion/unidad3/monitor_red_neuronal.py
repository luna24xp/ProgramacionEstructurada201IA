class MonitorEntrenamiento:

    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        """Registra el valor del error y verifica la convergencia."""
        self.historial_errores.append(valor_error)
        
        if valor_error < self.umbral_convergencia:
            print(f"[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")

def main():
    
    monitor = MonitorEntrenamiento(umbral_convergencia=0.05)
    
    print("--- Iniciando Monitor de Red Neuronal ---")


    for i in range(1, 6):
        try:
            entrada = input(f"Ingrese el error de la Época {i}: ")
            valor_error = float(entrada)

            if valor_error < 0:
                print("> [ERROR] El error no puede ser un número negativo.")
                continue

            monitor.registrar_epoca(valor_error)
            print("> Registro exitoso.")

        except ValueError:

            print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")


    print("\n--- Resumen de Entrenamiento ---")
    
    if monitor.historial_errores:
        historial = monitor.historial_errores
        promedio = sum(historial) / len(historial)
        mejor_error = min(historial)

        print(f"Historial: {historial}")
        print(f"Promedio de Error: {promedio:.4f}")
        print(f"Mejor resultado obtenido: {mejor_error}")
    else:
        print("No se registraron datos válidos para generar un resumen.")

if __name__ == "__main__":
    main()