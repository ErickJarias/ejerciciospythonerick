def main():
    lista_numeros = []
    total_numeros = 0
    total_pares = 0
    total_impares = 0
    suma_pares = 0
    suma_impares = 0
    menores_10 = 0
    entre_20_y_50 = 0
    mayores_100 = 0

    while True:
        num = int(input('Ingrese un número positivo (ingrese un negativo para salir): '))

        if num < 0: 
            break

        lista_numeros.append(num)
        total_numeros += 1

        if num % 2 == 0:
            total_pares += 1
            suma_pares += num
        else:
            total_impares += 1
            suma_impares += num

        if num < 10:
            menores_10 += 1
        elif 20 <= num <= 50:
            entre_20_y_50 += 1
        elif num > 100:
            mayores_100 += 1 

    promedio_pares = suma_pares / total_pares if total_pares > 0 else 0
    promedio_impares = suma_impares / total_impares if total_impares > 0 else 0

    print('\nReporte:')
    print('a. Total de números ingresados:', total_numeros)
    print('b. Total de números pares ingresados:', total_pares)
    print('c. Promedio de los números pares:', promedio_pares)
    print('d. Promedio de los números impares:', promedio_impares)
    print('e. Cuántos números son menores que 10:', menores_10)
    print('f. Cuántos números están entre 20 y 50:', entre_20_y_50)
    print('g. Cuántos números son mayores que 100:', mayores_100)

if __name__ == '__main__':
    main()
