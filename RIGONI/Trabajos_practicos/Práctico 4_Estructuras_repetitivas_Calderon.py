#Trabajo Practico 4 -Repetitivas - Calderon Ayrton
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
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
