from faker import Faker
faker = Faker("es_MX")

# 1. Declaracion de un vector vacio
ciudades_ia = []

#Operación de llenado (Ciclo)
for _ in range(5):
    ciudades_ia.append(faker.city())
    
# 3. Escritura de arreglos (mostrar resultados)
print("\n--- DATASET DE CIUDADES GENERADO ---")
for i in range(len(ciudades_ia)):
    print(f"Ciudad {i+1}: {ciudades_ia[i]}")