tus_registros = []

def registrar_registro():
    registro = input("Ingrese el nombre del registro: ")
    tus_registros.append({"registro": registro, "sismos": []})
    print("Registro agregado exitosamente.")

def registrar_sismo():
    for registro in tus_registros:
        sismos = []
        n_sismos = int(input("Ingrese la cantidad de sismos para el registro " + registro['registro'] + ": "))
        for i in range(n_sismos):
            magnitud = float(input("Ingrese la magnitud del sismo " + str(i+1) + " del registro " + registro['registro'] + ": "))
            sismos.append(magnitud)
        registro['sismos'] = sismos

def buscar_sismos_por_registro():
    registro = input("Ingrese el nombre del registro a buscar: ")
    for r in tus_registros:
        if r['registro'] == registro:
            print("Sismos registrados en el registro " + registro + ":")
            for i, sismo in enumerate(r['sismos']):
                print("Sismo " + str(i+1) + ": " + str(sismo))
            return
    print("Registro no encontrado.")

def informe_riesgo():
    for registro in tus_registros:
        promedio = sum(registro['sismos']) / len(registro['sismos'])
        print("Informe de riesgo para el registro " + registro['registro'] + ":")
        if promedio <= 2.5:
            print("Riesgo: Amarillo (Sin riesgo)")
        elif 2.6 <= promedio <= 4.5:
            print("Riesgo: Naranja (Riesgo medio)")
        else:
            print("Riesgo: Rojo (Riesgo alto)")

def menu():
    while True:
        print("\n----- Centro de Prevención de Sismos -----")
        print("1. Registrar Registro")
        print("2. Registrar Sismo")
        print("3. Buscar sismos por registro")
        print("4. Informe de riesgo")
        print("5. Salir")
        opcion = int(input("Seleccione una opción (1-5): "))

        if opcion == 1:
            registrar_registro()
        elif opcion == 2:
            registrar_sismo()
        elif opcion == 3:
            buscar_sismos_por_registro()
        elif opcion == 4:
            informe_riesgo()
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
