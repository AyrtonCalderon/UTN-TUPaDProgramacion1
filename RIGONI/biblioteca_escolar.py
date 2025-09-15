#CASO 1 - Biblioteca escolar
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles.
#Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]).
# Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
#Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.

#PENSAR LAS LISTAS
titulos = [] #Guardar los nombre de los libros
ejemplares = [] #Guarda la cantidad de copias del libro

opcion=0
#Estructura de menu con while 
while opcion != 5:
    print("1. Agregar libro")
    print("2. Mostrar catálogo")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")

    opcion=int(input("Elige una opcion: "))

    #Estructura Si
    if opcion == 1:
        titulo=input("Ingrese el titulo del libro: ")
        cantidad=int(input("Ingrese la cantidad: "))
        #append() es un método de las listas que se utiliza para agregar un único elemento al final de la lista existente
        titulos.append(titulo)
        ejemplares.append(cantidad)
        print("Agregado con exito")
    elif opcion == 2:
        print("Catalogo de libros")
    #len() en Python sirve para obtener la cantidad de elementos dentro de un objeto, como el número de caracteres en una cadena de texto, el número de elementos en una lista o tupla, o el número de claves en un diccionario.
        for i in range(len(titulos)):
            print(f"{titulos[i]} - Ejemplares: {ejemplares[i]}")
    elif opcion == 3:
        libro =input("Titulo del libro a prestar: ")
        if libro in titulos:
            i.index(libro)
            if ejemplares[i] > 0:
                ejemplares[i] -= 1
                print("Prestamo realizado")
            else:
                print("Libro no encontrado.")
        elif opcion == 4:
            libro=input("Titulos de libros a devolver: ")
            if libro in titulos:
                i=titulos.index(libro)
                ejemplares[i]+=1
                print("Libro devuelto")
            else:
                print("Libro no encontrado")
        elif opcion == 5:
            print("Salir del sistema")
        else:
            print("Opcion invalida, reintente de nuevo")
