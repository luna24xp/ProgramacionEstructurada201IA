#ejercicio de induccion: pago de nomina 

numero_horas = float(input("Ingrese el numero de horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))
nombre_empleado = str(input("Ingrese el nombre del empleado: "))

# Las horas superiores a 35 se pagan como extra
if numero_horas > 35:
    horas_extra = numero_horas - 35
    pago_bruto = (35 * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)
else:
    pago_bruto = numero_horas * tarifa_hora
    
# Calculo de impuestos
if pago_bruto < 2000:
    impuestos =0
elif pago_bruto <= 2000:
    impuestos = (pago_bruto -2000) * 0.20
else:
    impuestos = (pago_bruto -2220) * 0.30 + 220 * 0.20

pago_neto = pago_bruto - impuestos

# Mostrar resultados
print(f"Empleado : {nombre_empleado}")
print(f"Pago bruto : ${pago_bruto:.2f}")
print(f"Impuestos : ${impuestos:.2f}")
print(f"Pago neto : ${pago_neto:.2f}")
    