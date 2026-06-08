# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# FUNCIONES GENERADAS POR IA (Auditadas)
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Limpia una lista de lecturas de telemetría de un sensor LIDAR, 
    eliminando valores atípicos (errores de lectura).
    
    Parámetros:
    lista_datos (list): Lista de números flotantes que representan distancias.
    
    Retorna:
    list: Una nueva lista con valores válidos (entre 0.0 y 100.0 inclusive).
    """
    lista_filtrada = []
    # Uso de bucle tradicional en lugar de comprensión de listas para mantener estructura básica
    for lectura in lista_datos:
        # Validación de tipo y rango mediante condicionales (sin try-except)
        if type(lectura) == float or type(lectura) == int:
            if lectura >= 0.0 and lectura <= 100.0:
                lista_filtrada.append(float(lectura))
                
    return lista_filtrada

def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas están por debajo del umbral crítico de colisión.
    
    Parámetros:
    lista_filtrada (list): Lista de números flotantes (datos limpios).
    umbral_critico (float): Distancia mínima segura.
    
    Retorna:
    int: Número total de alertas detectadas.
    """
    total_alertas = 0
    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1
            
    return total_alertas

def generar_log_sistema(total_alertas):
    """
    Genera una cadena de texto de registro evaluando el estado del sistema 
    y la plataforma de ejecución.
    
    Parámetros:
    total_alertas (int): Número de alertas críticas detectadas.
    
    Retorna:
    str: Cadena de texto formateada con el registro de la acción a tomar.
    """
    sistema_os = sys.platform
    accion = "PERMITIDA"
    
    # Lógica de decisión estructural básica
    if total_alertas > 3:
        accion = "ABORTAR"
        
    return f"[{sistema_os}] Alertas críticas encontradas: {total_alertas}. Acción: [{accion}]"

# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    # Datos simulados de telemetría (con algunos errores de sensor)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0
    
    # Identificador del alumno y proyecto
    print("="*50)
    print(" AUTOR: Jesus Luna Mestizo (UX25II011)")
    print(" PROYECTO: Laboratorio de IA - Telemetría Autónoma")
    print("="*50 + "\n")
    
    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")
    
    # 1. Limpieza de datos
    datos_limpios = limpiar_lecturas(lecturas_raw)
    print(f"[*] Datos raw recibidos: {lecturas_raw}")
    print(f"[*] Datos tras filtrado LIDAR: {datos_limpios}")
    
    # 2. Cálculo de alertas
    alertas = calcular_alertas(datos_limpios, UMBRAL)
    print(f"[*] Procesando alertas con umbral de {UMBRAL}m...")
    
    # 3. Generación de log
    log_final = generar_log_sistema(alertas)
    
    print("\n=== LOG FINAL DEL SISTEMA ===")
    print(log_final)


"""
==========================================
RETO DE EVALUACIÓN Y ENTREGABLE
==========================================

1. El Prompt Utilizado:
"Actúa como un programador experto en Python Estructurado. Escribe el código de una función llamada 'limpiar_lecturas'. Recibe como parámetro una lista de números flotantes y debe retornar una nueva lista filtrada eliminando valores menores a 0.0 o mayores a 100.0. 
Restricciones estrictas: 
> 1. No utilices programación orientada a objetos (POO). 
> 2. No utilices manejo de excepciones (nada de bloques try-except). Gestiona los errores de datos usando condicionales if/else tradicionales. 
> 3. No utilices comprensiones de listas (list comprehensions); usa bucles for tradicionales. 
> 4. Incluye la documentación de la función mediante un Docstring descriptivo."
(Se repitió esta estructura exacta para las otras dos funciones adaptando Entradas y Salidas).

2. Tabla de Pruebas de Escritorio Manual (Trace Table):
- Caso de prueba al límite (Edge Case): Lista donde todos los valores son erróneos por sensor dañado.
- lecturas_raw = [-15.5, 105.0, -0.1]
- umbral_critico = 3.0

| Paso | Función Activa | Variables en Memoria | Evaluación Lógica | Salida / Cambio de Estado |
|---|---|---|---|---|
| 1 | limpiar_lecturas | lectura = -15.5 | -15.5 >= 0.0 (Falso) | Se ignora el valor. lista_filtrada = [] |
| 2 | limpiar_lecturas | lectura = 105.0 | 105.0 <= 100.0 (Falso) | Se ignora el valor. lista_filtrada = [] |
| 3 | limpiar_lecturas | lectura = -0.1 | -0.1 >= 0.0 (Falso) | Se ignora el valor. lista_filtrada = [] |
| 4 | calcular_alertas | lista_filtrada = [], umbral = 3.0 | El bucle 'for' no tiene elementos que iterar. | total_alertas = 0 |
| 5 | generar_log_sistema| total_alertas = 0, os = 'darwin' | 0 > 3 (Falso) | accion = "PERMITIDA" |
| 6 | MAIN | log_final | Formateo del string final | "[darwin] Alertas críticas... Acción: [PERMITIDA]" |
* Nota: El sistema operativo evaluado es 'darwin' dado que la ejecución se realiza sobre entorno macOS.

3. Auditoría de Código:
Durante la generación inicial, la IA intentó optimizar la función 'limpiar_lecturas' utilizando "List Comprehensions" (ej: `[x for x in lista_datos if 0.0 <= x <= 100.0]`). Aunque en entornos de producción en Python esto es un estándar por su eficiencia y legibilidad, en el contexto de esta práctica viola el paradigma puramente estructurado que busca evaluar la comprensión explícita del control de flujo (bucles iterativos paso a paso). 
Para solucionarlo, tuve que añadir una cuarta restricción estricta al prompt: "No utilices comprensiones de listas; usa bucles for tradicionales". Además, la IA intentó validar los tipos de datos usando bloques de `try: float(lectura) except ValueError:`, lo cual también fue auditado y sustituido por una comprobación condicional básica con `type()` para evitar el manejo de excepciones y ceñirse al contrato arquitectónico.
"""