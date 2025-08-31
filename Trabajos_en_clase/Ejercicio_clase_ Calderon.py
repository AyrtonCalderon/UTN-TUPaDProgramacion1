#Ingreso de datos
dia_letra = str(input("Ingrese el día en letras: "))
mes_actual= int(input("Ingrese el número del mes: "))
dia_numero = int(input("Ingrese el número de día: "))

cant_alumnos = None
cant_aprobados = None
cant_desaprobados = None

promedio_aprobados = None
promedio_desaprobados = None

cant_alumnosCiclo = None

asistencia = None
auxDia_letra= False
auxDia_numero= False
auxMes_actual= False


dia_letra= dia_letra.lower()

#Validar dia de semana

if (dia_letra == "lunes" or dia_letra == "martes" or dia_letra == "miercoles" or dia_letra == "jueves" or dia_letra == "viernes"):
    auxDia_letra = True
else:
    print("Ingrese un dia válido (Lunes,Martes,Miercoles,Jueves,Viernes): ")

#Validacion dia de semana

if (dia_numero >=1 and dia_numero <= 31 ):
    auxDia_numero= True
else:
    print("Ingrese un número de dia entre 1 y 31: ")

#Validacion de mes
if (mes_actual >=1 and mes_actual <=12):
    auxMes_actual = True

if auxDia_letra == False or auxDia_numero == False or auxMes_actual == False:
    print("Error. El dia, numero de día o numero del mes es inválido")
    exit() #Finaliza la ejecucion

#Segun el dia

if dia_letra == "lunes" or dia_letra == "martes" or dia_letra=="miercoles": 

    #pruebas
    cant_aprobados = int(input("Ingrese la cantidad de aprobados: "))
    cant_desaprobados = int(input("Ingrese la cantidad de desaprobados: "))
    cant_alumnos = cant_aprobados + cant_desaprobados

    promedio_aprobados = cant_aprobados*100/cant_alumnos
    promedio_desaprobados = cant_desaprobados*100/cant_alumnos

    print(f"El promedio de alumnos desaprobados fue de: {promedio_desaprobados}% y el promedio de alumnos aprobados fue de: {promedio_aprobados} ")


elif dia_letra == "jueves":
    #practica hablada
    asistencia = float(input("Ingrese el procentajes de asistencia: "))
    if(asistencia > 50):
        print("Asistio a la mayoría de clase")
    else:
        print("No asistió a la mayoría de clases")
#viernes

else:
    #viernes
    if dia_numero == 1 and (mes_actual == 1 or mes_actual == 7):
        print("Comienzo de nuevo ciclo")
        cant_alumnosCiclo= int(input("Ingrese la cantidad de alumnos del ciclo: "))
        arancel = float(input("Ingrese el arancel por alumno: "))
        recaudacion = arancel * cant_alumnosCiclo
        print(f"La recaudación de {recaudacion}$")
