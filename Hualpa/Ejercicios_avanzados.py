#Biblioteca estandar de python
import random
#Generar numeros estandar en python
tablero=[[random.randint(1,4) for _ in range(4)] for _ in range(4)]

#Primer muestra de tablero
for fila in tablero:
    print(fila)

def fila_valida(fila):
    # Convertimos la fila en un conjunto, que elimina duplicados
    return len(fila) == len(set(fila))

fila_1=[1,2,3,4]
fila_2=[1,2,3,4]

def columna_valida(columna):
    return len(columna) == len(set(columna))

# Ejemplo con un tablero de prueba
tablero = [
    [1,2,3,4],
    [2,1,4,3],
    [3,4,1,2],
    [4,3,2,1]
]

columna_1 = [tablero[fila][1] for fila in range(4)]
print(columna_valida(columna_1))  # True
