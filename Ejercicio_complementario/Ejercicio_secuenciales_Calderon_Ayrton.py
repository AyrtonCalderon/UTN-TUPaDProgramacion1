#CALCULADORA DE PROPINAS EN UN RESTAURANTE

#Pedir al usuario el monto total de la cuenta.
print("CALCULADORA DE PROPINAS EN UN RESTAURANTE")
total_mont=float(input("Ingrese el monto total: "))

#Propina sugerida al 10%
propina_10=total_mont*0.10

#Propina sugerida al 15%
propina_15=total_mont*0.15

#Calcular el total a pagar en ambos casos (cuenta + propina).
total_pagar_10=total_mont+propina_10
total_pagar_15=total_mont+propina_15

#Muestra por pantalla la propina sugerida y el total a pagar al 10%
print(f"Propina sugerida al 10%: {propina_10}")
print(f"Total a pagar al 10%: {total_pagar_10}")

#Muestra por pantalla la propina sugerida y el total a pagar al 15%
print(f"Propina sugerida al 15%: {propina_15}")
print(f"Total a pagar al 15%: {total_pagar_15}")
#----------------------------------------------------------------------------

#Ejercicio 1: Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
print("Ejercicios complementarios")
print("Ejercicio_1")
numero1=float(int(input("Ingrese un numero entero: ")))

#----------------------------------------------------------------------------
#Ejercicio 2:No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.
print("Ejercicio_2")
numero2=float(int(input("Ingrese un numero: ")))

#----------------------------------------------------------------------------
#Ejercicio 3: Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma=(numero1+numero2)
print(f"El resultado de la suma entre numero1 y numero 2 es de: {suma}")

#Ejercicio 4: Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para multiplicación y otra para división. Imprime estas variables.
#RESTA
resta=(numero1-numero2)
#MULTIPLICACION
producto=(numero1*numero2)
#DIVISION
division=(numero1/numero2)

#Valores mostrados por pantalla
print(f"La resta entre numero1 y numero2 es de: {resta}")
print(f"La multiplicacion entre numero1 y numero2 es de: {producto}")
print(f"La division entre numero1 y numero2 es de: {division}")

#----------------------------------------------------------------------------
#Ejercicio 5: Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre= "Ayrton"
print(f"El nombre ingresado es: {nombre}")

#----------------------------------------------------------------------------
#Ejercicio 6: Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio.
precio=float(input("Ingrese el precio de un producto: "))

#----------------------------------------------------------------------------
#Ejercicio 7: Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 100% y el valor 0 al 0%.
descuento=float(input("Ingrese el valor de descuento: "))
#----------------------------------------------------------------------------

#Ejercicio 8: Ahora, intenta calcular el precio final aplicando el descuento al precio original y
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que aplicar la lógica de matemáticas.
precio_final = precio * (1 - descuento)
#descuento: Si el descuento es 0.25 → 1 - 0.25 = 0.75
#Eso significa que vas a pagar el 75% del precio original.
print(f"El precio final con descuento es: {precio_final}")

#----------------------------------------------------------------------------
#Ejercicio 9:Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string.

cadena="Soy ayrton calderon, tengo 28 años y vivo en Mendoza, Argentina"
print(f"Se ha escrito: {cadena}")

#----------------------------------------------------------------------------
#Ejercicio 10: Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
# a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de Python.
longitud=len(cadena)
print(f"La longitud de la cadena es: {longitud}")

#-------------------------------------------------------------------------------
#Ejercicio 11:Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
# conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo mismo.

precio=float(3.5)
precio_entero=int(precio)
precio=print(precio_entero)

#-------------------------------------------------------------------------------
#Ejercicio 12: Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
nombre_completo=nombre+ " " + apellido
print(f"Seria: {nombre_completo}")
#-------------------------------------------------------------------------------

#Ejercicio 13: Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad=28
edad=edad+5

print("Despues de sumar 5",edad)

edad=edad-10
print("Despues de restas 10 años",edad)
#-------------------------------------------------------------------------------

#Ejercicio 14: Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
#centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3
altura=float(input("Ingrese su altura en decimales: "))
print(f"La altura es de: {altura} metros")

altura_mult=altura*4
altura_div=altura_mult/3

print(f"El resultado de multiplicar por 4 y dividir por 3 es de: {altura_div}")

#-------------------------------------------------------------------------------
#Ejercicio 15: Crea una variable que contenga tu nombre completamente en mayúsculas. Después
#transfórmalo todo en minúsculas con algún método o función de Python.
nombre_mayus="AYRTON CALDERON"
print("Nombre en mayusculas:",nombre_mayus)

nombre_minus=nombre_mayus.lower()
print("Nombre en minuscula:",nombre_minus)

#-------------------------------------------------------------------------------
#Ejercicio 16:Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#para que se transforme todo en minúsculas excepto la primera letra.

nombre_modif=nombre_mayus.capitalize()

print("Nombre modificado:",nombre_modif)

