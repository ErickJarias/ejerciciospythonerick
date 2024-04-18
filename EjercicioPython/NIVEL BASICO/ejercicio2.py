nombre_estudiante = ''
edad_estudiante = 0
imc_estudiante = 0

for i in range(1):
    nombre_estudiante = input('Ingrese el nombre del estudiante: ')
    edad_estudiante = int(input('Ingrese la edad: '))
    peso_estudiante = float(input('Ingrese el peso: '))
    altura_estudiante = float(input('Ingrese la altura: '))
    imc_estudiante = peso_estudiante / (altura_estudiante ** 2)

print(f'El estudiante {nombre_estudiante}, con {edad_estudiante} años, tiene un IMC de {imc_estudiante} y su estado es:')

if imc_estudiante < 24.9:
    print('Normal')
elif 25 < 29.9:
    print('Sobrepeso')
elif 30 < 34.9:
    print('Obesidad 1')
elif 35 < 39.9:
    print('Obesidad 2')
elif 39.9 < 40:
    print('Obesidad 3')
