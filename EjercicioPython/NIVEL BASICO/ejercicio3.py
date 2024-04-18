peso_ideal_count = 0
obesidad_grado_1_count = 0
obesidad_grado_2_count = 0
obesidad_grado_3_count = 0
sobrepeso_count = 0

for i in range(20):
    nombre = input(f'\nIngrese el nombre del estudiante {i + 1}: ')
    edad = int(input('Ingrese la edad: '))
    peso = float(input('Ingrese el peso: '))
    altura = float(input('Ingrese la altura: '))

    imc = peso / (altura ** 2)

    print('IMC:', imc)

    if imc <= 18.5:
        peso_ideal_count += 1
    elif imc <= 24.9:
        peso_ideal_count += 1
    elif imc <= 29.9:
        sobrepeso_count += 1
    elif imc <= 34.9:
        obesidad_grado_1_count += 1
    elif imc <= 40:
        obesidad_grado_2_count += 1
    else:
        obesidad_grado_3_count += 1

print('\nReporte de estudiantes:')
print('a. Peso ideal:', peso_ideal_count)
print('b. Obesidad grado 1:', obesidad_grado_1_count)
print('c. Obesidad grado 2:', obesidad_grado_2_count)
print('d. Obesidad grado 3:', obesidad_grado_3_count)
print('e. Sobrepeso:', sobrepeso_count)
