import numpy as np

def colocar_barcos(tablero, barcos):
    for longitud, cantidad in barcos.items():
        for _ in range(cantidad):
            barco_colocado = False
            while not barco_colocado:
                fila = np.random.randint(0, 10)
                columna = np.random.randint(0, 10)
                direccion = np.random.choice(["horizontal", "vertical"])
                if direccion == "horizontal":
                    if columna + longitud <= 10 and np.all(tablero[fila, columna:columna+longitud] == 0):
                        tablero[fila, columna:columna+longitud] = 1
                        barco_colocado = True
                else:
                    if fila + longitud <= 10 and np.all(tablero[fila:fila+longitud, columna] == 0):
                        tablero[fila:fila+longitud, columna] = 1
                        barco_colocado = True
def mostrar_tablero(tablero):
    print(tablero)
def barco_hundido(tablero, fila, columna):
    if tablero[fila, columna] == 1:
        if columna < 9 and tablero[fila, columna+1] == 1:
            inicio = columna
            fin = columna + 1
            while fin < 9 and tablero[fila, fin+1] == 1:
                fin += 1
            return np.all(tablero[fila, inicio:fin+1] == -1)
        elif fila < 9 and tablero[fila+1, columna] == 1:
            inicio = fila
            fin = fila + 1
            while fin < 9 and tablero[fin+1, columna] == 1:
                fin += 1
            return np.all(tablero[inicio:fin+1, columna] == -1)
    return False
tablero_jugador = np.zeros((10, 10))
tablero_maquina = np.zeros((10, 10))
barcos_jugador = {1: 4, 2: 3, 3: 2, 4: 1}
barcos_maquina = {1: 4, 2: 3, 3: 2, 4: 1}
colocar_barcos(tablero_jugador, barcos_jugador)
colocar_barcos(tablero_maquina, barcos_maquina)
# Juego
while True:
    print("----- TURNO DEL JUGADOR -----")
    mostrar_tablero(tablero_jugador)
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    if tablero_maquina[fila, columna] == 1:
        tablero_maquina[fila, columna] = -1
        if barco_hundido(tablero_maquina, fila, columna):
            print("Tocado y hundido")
            barcos_maquina[1] -= 1
            if barcos_maquina[1] == 0:
                print("¡Has ganado!")
                break
        else:
            print("Tocado")
    else:
        print("Agua")
    print("----- TURNO DE LA MÁQUINA -----")
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 10)
    if tablero_jugador[fila, columna] == 1:
        tablero_jugador[fila, columna] = -1
        if barco_hundido(tablero_jugador, fila, columna):
            print("Tocado y hundido")
            barcos_jugador[1] -= 1
            if barcos_jugador[1] == 0:
                print("¡La máquina ha ganado!")
                break
        else:
            print("Tocado")
    else:
        print("Agua")