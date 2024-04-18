import os

class Jugador:
    def __init__(self, id_jugador, nombre, edad, categoria):
        self.id_jugador = id_jugador
        self.categoria = categoria
        self.nombre = nombre
        self.edad = edad
        self.plus_puntos = 0
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0        

class TorneoTenisModificado:
    def __init__(self):
        self.categorias = {'Novato': [], 'Intermedio': [], 'Avanzado': []}

    def registro_jugador(self, id_jugador, nombre, edad, categoria):
        jugador = Jugador(id_jugador, nombre, edad, categoria)
        if categoria in self.categorias.keys():
            if (categoria == 'Novato' and 15 <= edad <= 16) or \
               (categoria == 'Intermedio' and 17 <= edad <= 20) or \
               (categoria == 'Avanzado' and edad > 20):
                self.categorias[categoria].append(jugador)
                print(f"{nombre} registrado en la categoría: {categoria}")
            else:
                print(f"{nombre} no cumple con los requisitos de edad para esta categoría.")
        else:
            print("Categoría no encontrada.")

    def inicio_torneo(self):
        for categoria, jugadores in self.categorias.items():
            if len(jugadores) < 5:
                print(f"Faltan jugadores en la categoría: {categoria} para comenzar el torneo.")
            else:
                print(f"Comenzó el torneo de la categoría: {categoria}")

    def registrar_partido(self, id_ganador, id_perdedor, punt_ganador, punt_perdedor):
        ganador = None
        perdedor = None

        for categoria, jugadores in self.categorias.items():
            for jugador in jugadores:
                if jugador.id_jugador == id_ganador:
                    ganador = jugador
                elif jugador.id_jugador == id_perdedor:
                    perdedor = jugador

        if ganador is not None and perdedor is not None:
            ganador.partidos_jugados += 1
            perdedor.partidos_jugados += 1
            ganador.partidos_ganados += 1
            perdedor.partidos_perdidos += 1
            ganador.plus_puntos += punt_ganador - punt_perdedor
            print("El resultado del partido ha sido registrado.")
        else:
            print("No se encontraron registros de ese jugador.")

    def mostrar_estadisticas(self):
        for categoria, jugadores in self.categorias.items():
            print(f"Categoría: {categoria} ")
            print("| ID | Jugador | Partidos Jugados | Partidos Ganados | Partidos Perdidos | Puntos a Favor |")
            for jugador in jugadores:
                print(f"| {jugador.id_jugador} | {jugador.nombre} | {jugador.partidos_jugados} | {jugador.partidos_ganados} | {jugador.partidos_perdidos} | {jugador.plus_puntos} |")

    def obtener_ganador_categoria(self, categoria):
        if categoria in self.categorias.keys():
            jugadores_categoria = self.categorias[categoria]
            if jugadores_categoria:
                ganador = max(jugadores_categoria, key=lambda jugador: jugador.plus_puntos)
                print(f"El ganador en la categoría {categoria} es: {ganador.nombre}, con {ganador.plus_puntos} puntos.")
            else:
                print(f"No hay jugadores registrados en la categoría {categoria}.")
        else:
            print("La categoría especificada no existe.")

def registro_jugador_manualmente(torneo):
    id_jugador = int(input("ID del jugador: "))
    nombre = input("Nombre del jugador: ")
    edad = int(input("Edad del jugador: "))
    categoria = input("Categoría (Novato/Intermedio/Avanzado): ")
    torneo.registro_jugador(id_jugador, nombre, edad, categoria)

def main():
    torneo = TorneoTenisModificado()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\t\t  Menú ")
        print("\t  1. Registrar un jugador                            ")
        print("\t  2. Iniciar el torneo                               ")
        print("\t  3. Registrar resultado de un partido               ")
        print("\t  4. Mostrar las estadísticas                        ")
        print("\t  5. Obtener el ganador de una categoría             ")
        print("\t  6. Salir                                           ")
        print(" ")
        opc = input("Seleccione una opción (1-6): ")

        continuar = input("¿Desea registrar un jugador? (s/n): ")

        if opc == "1":
            registro_jugador_manualmente(torneo)
        elif opc == "2":
            torneo.inicio_torneo()
        elif opc == "3":
            id_ganador = int(input("ID del jugador ganador: "))
            id_perdedor = int(input("ID del jugador perdedor: "))
            punt_ganador = int(input("Puntos del jugador ganador: "))
            punt_perdedor = int(input("Puntos del jugador perdedor: "))
            torneo.registrar_partido(id_ganador, id_perdedor, punt_ganador, punt_perdedor)
        elif opc == "4":
            torneo.mostrar_estadisticas()
        elif opc == "5":
            categoria = input("Categoría: ")
            torneo.obtener_ganador_categoria(categoria)
        elif opc == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 6.")

if __name__ == "__main__":
    main()
