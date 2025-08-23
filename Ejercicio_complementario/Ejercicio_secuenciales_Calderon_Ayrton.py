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