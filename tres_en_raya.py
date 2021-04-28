import numpy as np
import pandas as pd

from collections import deque

#%%
while True:
    N = input("Ingresa el tamaño del tablero\n")
    if N.isdigit() == True and int(N) >= 3:
        N = int(N)
        break
    
#%%

def condicion_victoria():
    for i in range(1,N+1):
        if set(tablero[i]).issubset("O") == True or set(tablero[i]).issubset("X") == True:
            return True
        if set(tablero.loc[i]).issubset("O") == True or set(tablero.loc[i]).issubset("X") == True:
            return True
    if set(np.diag(tablero)).issubset("O") == True or set(np.diag(tablero)).issubset("X") == True:
        return True
    if set(np.diag(tablero[list(range(N,0,-1))])).issubset("O") == True or set(np.diag(tablero[list(range(N,0,-1))])).issubset("X") == True:
        return True
    
#%%    
tablero = pd.DataFrame(np.reshape([" " for x in range(0,N**2)],(N,N)),index=range(1,N+1),columns=range(1,N+1))
turno = deque(["O","X"])
salida = True
while salida:
    print(tablero)
    while True:    
        while True:
            fila = input(f"Jugador {turno[0]} ingresa número de fila. 'Salir' para terminar.\n")
            if fila.lower() == "salir":
                print(f"Saliendo. Pierde jugador {turno[0]}")
                salida = False
                break
            elif fila.isdigit() == False or int(fila) < 1 or int(fila) > N:
                print("Valor de fila inválido")
            else:
                break
        if salida == False:
            break
    
        while True:
            columna = input(f"Jugador {turno[0]} ingresa número de columna. 'Salir' para terminar.\n")
            if columna.lower() == "salir":
                print(f"Saliendo. Pierde jugador {turno[0]}")
                salida = False
                break
            elif columna.isdigit() == False or int(columna) < 1 or int(columna) > N:
                print("Valor de columna inválido")
            else:
                break
        if salida == False:
            break
        
        if tablero[int(columna)].loc[int(fila)] != " ":
            print(tablero)
            
            print("Casilla ocupada. Elige nuevamente las posiciones")
        else:
            break
    
    if salida == False:
            break
        
    tablero[int(columna)].loc[int(fila)] = turno[0]
    
    if condicion_victoria() == True:
        print(tablero)
        print(f"\nEl juego terminó. Gana jugador {turno[0]}")
        break

    if set(np.ravel(tablero)).issubset({"O","X"}) == True:
        print(tablero)
        print(f"\nEl juego se declara en empate")
        break
    
    turno.rotate()
