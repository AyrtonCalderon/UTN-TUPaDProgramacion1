#Calculadora de propinas en un restaurante

#Pedir al usuario el monto total de la cuenta.
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