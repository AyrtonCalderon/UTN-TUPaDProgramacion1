#TRABAJO PRACTICO 3
#Condicionales

#1-Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
edad=int(input("Ingrese su edad: "))

#Condicion
if edad>=18:
 print ("Es mayor de edad ")
else:
 print ("Es menor de edad ")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#2- Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota=int(input("Escriba la nota: "))

#Condicion
if nota>=6:
 print ("Aprobado")
else:
 print("Desaprobado")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#3-Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero=int(input("Ingrese un numero: "))

#Condicion
if numero % 2 ==0:
 print("Es un numero par")
else:
 print("Porfavor ingrese un numero par")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#4- Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

antiguedad=int(input("Ingrese la edad: "))

if antiguedad<12:
 print("Niño/a menor de edad")
elif antiguedad>=12 and antiguedad<18:
 print("Adolescente")
elif antiguedad>=18 and antiguedad<30:
 print("Adulto joven")
elif antiguedad>=30:
 print("Adulto")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#5-Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

contraseña=input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
 print("La contraseña ingresada es correcta")
else:
 print("Porfavor ingrese una contraseña")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#6-escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
#Lista de 50 numeros entre 1 y 100
numeros_aleatorios=[random.randint(1,100) for i in range(50)]

from statistics import mode,median,mean
mi_lista=[1,2,3,4,5]
mean(mi_lista)

m_media=mean(numeros_aleatorios)
m_mediana=median(numeros_aleatorios)
m_moda=mode(numeros_aleatorios)

# Determinar tipo de sesgo
if m_media > m_mediana > m_moda:
    print("La distribución tiene sesgo positivo.")
elif m_media < m_mediana < m_moda:
    print("La distribución tiene sesgo negativo.")
elif m_media == m_mediana == m_moda:
    print("La distribución no tiene sesgo.")
else:
    print("La distribución no cumple")
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#7-Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto=input("Ingrese una palabra o frase")

#Condicion
if texto[-1].lower() in "aeiou":
  resultado=texto +" ! "
else:
  resultado=texto

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#8-Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:

#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

name=input("Ingrese su nombre: ")
opcion=int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: "))

#Condicion
if opcion==1:
  print(name.upper())
elif opcion==2:
  print(name.lower())
elif opcion==3:
  print(name.title())
else:
  print("Opcion no valida")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#9-Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

terremoto=float(input("Ingrese la magnitud del terremoto: "))
# Menor que 3: "Muy leve" (imperceptible).
if terremoto<3:
  print("Muy leve")

# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
elif terremoto>=3 and terremoto<4:
  print("Leve,(Ligeramente imperceptible)")

# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
elif terremoto>=4 and terremoto<5:
  print("Moderado (sentido por personas pero no causa daños)")
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
elif terremoto>=5 and terremoto<6:
  print("Fuerte (puede causar daños en estructuras débiles).")
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
elif terremoto>=6 and terremoto<7:
  print("Muy fuerte, puede causar daños significativos")
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
elif terremoto>=7:
  print("Extremo")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#10-Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

#Pedir los datos al usuario:
#Hemisferio (N o S)
hemisferio=input("En que hemisferio se encuentra? (Ingrese N para norte o S para sur)").upper()
#Mes (número del 1 al 12)
mes=int(input("Ingrese el mes (En numeros) en el que se encuentra: "))
#Día (número del 1 al 31)
day=int(input("Ingrese el dia en numeros: "))

#CONDICIONES 
#HEMISFERIO NORTE Y SUR
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
if (mes==12 and day>=21 ) or (mes in (1,2)) or (mes==3 and day<=20):
  estacion_nor = "Invierno"
  estacion_sur = "Verano"
#Desde el 21 de marzo hasta el 20 de junio (incluidos)
elif (mes==3 and day>=21) or (mes in (4,5)) or (mes==6 and day<=20):
 estacion_nor="Primavera"
 estacion_sur="Otoño"
#Desde el 21 de junio hasta el 20 de septiembre (incluidos)
elif (mes==6 and day>=21) or (mes in (7,8)) or (mes==9 and day<=20):
 estacion_nor="Verano"
 estacion_sur="Invierno"
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
elif (mes==9 and day>=21) or (mes in (10,11)) or (mes==12 and day<=20):
 estacion_nor="Otoño"
 estacion_sur="Primavera"

 #Hemisferio seleccionado:
if hemisferio == "N":
    print("Estación:", estacion_nor)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio no válido. Ingrese N o S.")