#TRABAJO PRACTICO 5 - CALDERON AYRTON
#EJEIRCICIO_1
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
numeros_mult=list(range(4, 101, 4))
print(numeros_mult)
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
favoritos=["perro", "gatos", "CSS", "música", "película"]
print("Ejercicio_2:",favoritos[-2])

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#3)Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
#Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
lista_vacia=[]
lista_vacia.append("Python")
lista_vacia.append("UTN")
lista_vacia.append("Programación")
print("Ejercicio_3:",lista_vacia)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

animales=["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print("Ejercicio_4:",animales)
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print(f"numeros=[8, 15, 3, 22, 7]")
print(f"números.remove(max(numeros))")
print("Crea una lista de numeros, encuentra el mas grande de la lista y lo borra y la lista queda igual pero sin el numero maximo")
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Ejercicio_6:", numeros[:2])
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

#Reemplazo de valores
autos[1] = "camion"
autos[2] = "mecanico"
#Imprimir en pantalla
print("Ejercicio_7:", autos)
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla
dobles = []
# Agregar los dobles usando append
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
# Mostrar en pantalla
print("Ejercicio 8:", dobles)
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
#["agua"]]

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
#d) Imprimir la lista resultante por pantalla
print("Ejercicio 9:", compras)
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Ejercicio 10: Lista anidada con distintos elementos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# Imprimir la lista resultante
print("Ejercicio 10:", lista_anidada)

