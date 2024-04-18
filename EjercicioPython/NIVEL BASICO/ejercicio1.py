numeros_ingresados = []
sumatoria_positivos = 0

for i in range(3):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros_ingresados.append(numero)
    if numero > 0:
        sumatoria_positivos += numero

if sumatoria_positivos > 0:
    print(f"Los números ingresados son: {numeros_ingresados}")
    print(f"La sumatoria de los números positivos es: {sumatoria_positivos}")
else:
    print("No se ingresaron números positivos.")
