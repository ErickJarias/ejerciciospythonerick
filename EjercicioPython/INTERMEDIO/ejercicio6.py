class Organismo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.consumo_electricidad = 0

    def registrar_consumo(self, consumo):
        self.consumo_electricidad += consumo


def registrar_organismo(organismos):
    nombre_organismo = input("Ingrese el nombre del organismo: ")
    mi_organismo = Organismo(nombre_organismo)
    organismos.append(mi_organismo)
    print("Organismo registrado con éxito.")


def registrar_consumo_por_organismo(organismos):
    if not organismos:
        print("Primero debe registrar al menos un organismo.")
        return

    nombre_organismo = input("Ingrese el nombre del organismo: ")
    for organismo in organismos:
        if organismo.nombre.lower() == nombre_organismo.lower():
            consumo = float(input(f"Ingrese el consumo de electricidad para {organismo.nombre.lower()}: "))
            organismo.registrar_consumo(consumo)
            print("Consumo registrado con éxito.")
            return
    print("Organismo no encontrado.")


def ver_co2_producido(organismos):
    total_co2 = sum(organismo.consumo_electricidad * 0.537 for organismo in organismos)
    print(f"La cantidad total de CO2 producida es: {total_co2:.2f} kg")


def organismo_mayor_co2(organismos):
    if not organismos:
        print("No hay organismos registrados.")
        return

    mayor_co2 = max(organismos, key=lambda organismo: organismo.consumo_electricidad * 0.537)
    print(f"El organismo que produce mayor CO2 es: {mayor_co2.nombre}")


def menu():
    organismos = []

    while True:
        print("\nMenú:")
        print("1. Registrar Organismo")
        print("2. Registrar consumo por organismo")
        print("3. Ver CO2 producido")
        print("4. Organismo que produce mayor CO2")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            registrar_organismo(organismos)
        elif opcion == "2":
            registrar_consumo_por_organismo(organismos)
        elif opcion == "3":
            ver_co2_producido(organismos)
        elif opcion == "4":
            organismo_mayor_co2(organismos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    menu()
