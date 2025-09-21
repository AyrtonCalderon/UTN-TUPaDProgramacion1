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



