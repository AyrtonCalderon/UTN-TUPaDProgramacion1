#EJERCICIO_1
#Ingreso de datos
nombre = input("Ingrese su nombre: ")
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
antiguedad_laboral=int(input("Ingrese su años de antiguedad: "))
historial_crediticio=input(f"Bueno/regular/malo: ").lower()
dinero_ingresado=float(input("Ingrese la cantidad de dinero ingresado: " ))
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
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Ejercicios de Tarea — Programación 1 (Condicionales)

#Ejercicio_4: Ejercicio 1 — Clasificación de impuestos
#El programa debe calcular el impuesto anual que debe pagar una persona en función de sus ingresos y edad:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese su ingreso anual: "))

# Cálculo del impuesto según ingresos
if ingresos < 500000:
    impuesto = 0
elif ingresos < 2000000:
    impuesto = ingresos * 0.10
elif ingresos < 5000000:
    impuesto = ingresos * 0.20
else:
    impuesto = ingresos * 0.35

# Reducción por edad (>65 años)
if edad > 65:
    impuesto = impuesto / 2

# Resultado
print(f"Contribuyente: {nombre}, {apellido}")
print(f"Edad: {edad} años")
print(f"Ingresos anuales: ${ingresos:,.2f}")
print(f"Impuesto a pagar: ${impuesto:,.2f}")
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#Ejercicio_2: Se desea determinar el estado académico de un alumno en base a 3 notas parciales.

# Códigos de colores ANSI
rojo = "\033[91m"
amarillo = "\033[93m"
verde = "\033[92m"
reset = "\033[0m"  # Para volver al color normal

#Ingreso de datos
nombre_usuario=input("Ingrese su nombre: ")
n_legajo=input("Ingrese numero de legajo: ")

#Notas
nota_1=float(input("Ingrese la nota 1: "))
nota_2=float(input("Ingrese la nota 2: "))
nota_3=float(input("Ingrese la nota 3: "))

#Calculo de promedio
promedio=(nota_1+nota_2+nota_3)/3
print(f"El promedio es de: {promedio:,.2f}")
#Condicion
if nota_1<4 or nota_2<4 or nota_3 < 4:
    print(f"{rojo},Desaprobado directo{reset}")
elif promedio<6:
    print(f"{rojo}Desaprobado{reset}")
elif 6 <= promedio <8:
    print(f"{amarillo}Aprobado con final{reset}")
elif promedio >=8:
    print(f"{verde}Promocionado{reset}")
#----------------------------------------------------------
#----------------------------------------------------------
#Ejercicio_3: El sistema debe administrar retiros de dinero de un cajero.
nombre=input("Ingrese su nombre: ")

#Ingreso de pin
# PIN correcto
PIN_CORRECTO = "1234"

# Primer intento
pin = input("Ingrese su PIN: ")

if pin == PIN_CORRECTO:
    print("PIN correcto. Acceso permitido.")
else:
    print("PIN incorrecto. Intento 1 de 3")
    
    # Segundo intento
    pin = input("Ingrese su PIN nuevamente: ")
    if pin == PIN_CORRECTO:
        print("PIN correcto. Acceso permitido.")
    else:
        print("PIN incorrecto. Intento 2 de 3")
        
        # Tercer intento
        pin = input("Ingrese su PIN nuevamente: ")
        if pin == PIN_CORRECTO:
            print("PIN correcto. Acceso permitido.")
        else:
            print("PIN incorrecto. Se alcanzó el máximo de intentos. Acceso bloqueado.")
#SALDO INICIAL
saldo_inicial = 50000

monto = float(input("Ingrese el monto a retirar: "))

if monto > 20000:
    comision = monto * 0.02         # 2% de comisión
    total = monto + comision        # monto + comisión
    if total > saldo_inicial:
        print("No tiene saldo suficiente para cubrir retiro + comisión.")
    else:
        saldo_inicial -= total
        print(f"Retiro de ${monto:,.2f} realizado con comisión de ${comision:,.2f}.")
else:
    if monto > saldo_inicial:
        print("No tiene saldo suficiente para cubrir el retiro.")
    else:
        saldo_inicial -= monto
        print(f"Retiro de ${monto:,.2f} realizado correctamente.")

print(f"Saldo actualizado: ${saldo_inicial:,.2f}")

