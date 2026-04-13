"""
version 2 del clasificador de pixeles para 
"""

umbral_bajo = 0.3
umbral_alto = 0.7
    
def clasificar_pixel (intensidad): 
    """Clasifica una intensidad de pixel en fondo, gris, objeto o ruido."""
    if not intensidad_valida(intensidad):
        return None

    if fondo_oscuro(intensidad):
        return "(Fondo Oscuro)"

    if gris_ruido(intensidad):
        return "GRIS (Ruido)"

    if objeto_brillante(intensidad):
        return "Objeto brillante"


def intensidad_valida(intensidad):
    """Devuelve True si la intensidad está en el rango válido [0.0, 1.0]."""
    return 0.0 <= intensidad <= 1.0


def fondo_oscuro(intensidad):
    """Devuelve True si la intensidad corresponde a fondo oscuro."""
    return 0.0 <= intensidad <= umbral_bajo


def gris_ruido(intensidad):
    """Devuelve True si la intensidad corresponde a gris de ruido."""
    return umbral_bajo < intensidad < umbral_alto


def objeto_brillante(intensidad):
    """Devuelve True si la intensidad corresponde a un objeto brillante."""
    return intensidad >= umbral_alto


        
import os

def cargar_y_precesar(nombre_archivo):
    
    clasificacion = None
    
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0
    
    # Obtener la ruta del archivo
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)
    
    try: 
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                #convetir cada linea a numero flotante
                valor_crudo = float(linea.strip())
                
                #Clasificar el valor del pixel
                clasificacion = clasificar_pixel(valor_crudo)
                print(f"Valor crudo: {valor_crudo} - Clasificación: {clasificacion}")
                
                #agregamos la logica de clasificación
                if clasificacion is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append(clasificacion)
                    if clasificacion ==  "(Fondo Oscuro)":
                        fondo_oscuro += 1
                    elif clasificacion == "GRIS (Ruido)":
                        gris_ruido += 1
                    elif clasificacion == "Objeto brillante":
                        objeto_brillante += 1
                
        print("Resultados de clasificación:")
        print(f"Fondo Oscuro: {fondo_oscuro}")
        print(f"GRIS (Ruido): {gris_ruido}")
        print(f"Objeto brillante: {objeto_brillante}")
        print(f"Ruido detectado: {ruido_detectado}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")

def main():
    cargar_y_precesar("lecturas_sensores.txt")

if __name__ == "__main__":
    main()


