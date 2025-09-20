#Trabajo Practico 4 -Repetitivas - Calderon Ayrton
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Ejercicio_1")
for i in range(101):
    print(i)
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
print("Ejercicio_2")
num=int(input("ingrese un numero:" ))
#Contador
cont=0

#Caso: Si el numero ingresado es 0, tiene 1 digito
if num==0:
    cont=1
else:
    while num>0:
        num=num//10
        cont+=1
        
print(f"El numero tiene {cont} digitos.")

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
print("Ejercicio_3")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = 0

#Orden (menor, mayor)
men = min(a, b)
may = max(a, b)

# Recorremos los números entre menor y mayor, sin incluirlos
for i in range(men + 1, may):
    suma += i

print(f"La suma de los números entre {a} y {b}, excluyéndolos, es: {suma}")
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#4)Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("Ejercicio_4")
sum=0
while True:
    resul=int(input("Ingrese un numero: "))
    if resul==0:
        print("Fin del ciclo")
    break

    sum+=resul
print(f"La suma total es: {sum}")

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("Ejercicio_5")
import random

numero_secreto=random.randint(0,9)
intentos=0

while True:
    adivina=input("Adivina el número del 0 al 9 (o escribe salir para terminar): ")
    if adivina.lower() == "salir":
        print(f"Juego terminado. El numero secreto era: {numero_secreto}")
        break

    # Verificamos si es un número válido
    elif adivina.isdigit():
        adivina = int(adivina)
        intentos += 1

    if adivina == numero_secreto:
            print(f"Correcto, Necesitaste {intentos} intentos.")
            break
    else:
            print("Error, intenta de nuevo.")

    # Entrada inválida
else:
        print("Entrada inválida, ingrese un número del 0 al 9 o 'salir'.")

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
print("Ejercicio_6")
for itera in range(100,-1,-1):
    if itera%2==0:
        print(itera)
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#7)Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
print("Ejercicio_7")
n=int(input("Ingrese un numero entero positivo: "))
sum=0

for ite in range(0,n +1):
    sum=sum+ite
    print(f"La suma es: {sum}")
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
print("Ejercicio_8")
#Variables
pares=0
impares=0
positivos=0
negativos=0

#Bucle
for i in range(100):
    val=int(input("Ingrese un numero: "))

#Es par o impar
if val%2==0:
    pares+=1
else:
    impares+=1

#Positivo o negativo
if val>0:
    positivos+=1
elif val<0:
    negativos+=1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#9)Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
print("Ejercicio_9")
su=0
for itera in range(100):
    valo=int(input("Ingrese un numero: "))
    su=su+valo

media = suma / 100
print(f"La media es: {media}")

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("Ejercicio_10")
nume=int(input("Ingrese un número: "))

invertido=0

while nume>0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print(f"El número invertido es: {invertido}")