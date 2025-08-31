#EJERCICIO_1
#Ingreso de datos
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input(f"Ingrese su edad: "))

#PROMEDIO
promedio=float(input("Ingrese su promedio (0-10): "))

if promedio <0 or promedio > 10:
    print(f"Error, el promedio debe estar entre 0 y 10")
else:
    print(f"Promedio permitido: {promedio}")

#Promedio
promedio=float(input("Ingrese su promedio general:(0 y 10): "))

#Si el promedio es menor a 6 → automáticamente rechazado.
if promedio<6:
    print(f"Rechazado")
#Si el promedio es menor a 6 → automáticamente rechazado.
else:
    print(f"Valido: {promedio}")

    ingreso=float(input("Ingrese el monto que se aporto: "))
#Si los ingresos familiares < $300.000 → beca completa.
    if ingreso<300000:
        print(f"Beca completa")
        #Si los ingresos entre $300.000 y $600.000 → media beca.
    elif ingreso>= 300000 or ingreso <= 600000:
            print(f"Media beca")
    else: 
        print(f"Rechazado")

#----------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#EJERCICIO 2 
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
dni=int(input(f"Ingrese su DNI: "))
edad=int(input(f"Ingrese su edad: "))
obra_social=input(f"¿Tiene obra social?").lower()
prioridad=int(input("Ingrese prioridad medica: (1=emergencia,2=urgente,3=control): "))

#Prioridad
if prioridad == 1:
    turno = "Inmediato"
elif prioridad == 2:
    turno= "Urgente"
    if obra_social == "Si":
        turno="Turno en menos de 24 horas"
    else:
        turno="Turno en menos de 48 horas"
elif prioridad==3:
    if edad>65:
        turno="Turno preferencial en 72hs"
    else:
        turno="Turno normal en 7 dias"
else: "Invalida"
print(f"Nombre y apellido: ",{nombre}, {apellido})
print(f"DNI: ",{dni})
print("Prioridad: ",{prioridad})
#----------------------------------------------------
#----------------------------------------------------
#Ejercicio_3
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
cuit=int(input(f"Ingrese su CUIT: "))
ingreso_men=float(input(f"Ingreso mensual: "))
antiguedad_laboral=int(input("Ingrese su años de antiguedad"))
historial_crediticio=input(f"Bueno/regular/malo").lower()
dinero_ingresado=float(input("Ingrese la cantidad de dinero ingresado:" ))
#Condicion print("Credito aprobado")
if historial_crediticio=="malo":
    print("Historial malo, rechazado")
elif ingreso_men<200000:
    print("Ingreso insuficiente")
elif ingreso_men >= 200000 and antiguedad_laboral>=2:
    if historial_crediticio == "regular":
        print ("Credito aprobado hasta 1.000.000")
elif historial_crediticio == "bueno":
        print ("Credito aprobado hasta 3.000.000")
else:
    print("Invalido")

print("Condicion no prevista")

#Resultado por pantalla
print(f"Cliente: ",{nombre}, {apellido})
print("CUIT:", cuit)
print("Ingresos: $", ingreso_men)
print("Antigüedad:", antiguedad_laboral, "años")
print("Historial:", historial_crediticio)
