# 5. Una persona debe realizar un muestreo con 50 personas para determinar
# el promedio de peso de los niños, jóvenes, adultos y ancianos que existen
# en su zona.

# Las categorías se determinarán de acuerdo a la siguiente tabla:

# Niños:    0 - 12 años
# Jóvenes:  13 - 29 años
# Adultos:  30 - 59 años
# Ancianos: 60 años en adelante
pesoniños=0
pesojovenes=0
pesoadultos=0
pesoancianos=0

nume_niños=0
nume_jovenes=0
nume_adultos=0
nume_ancianos=0
peso=0
for i in range(50):
    edad=int(input(f"ingresa la edad {i+1}:"))
    peso=float(input(f"ingresa el peso {i+1}:"))
    if edad >=0 and edad <=12:
        pesoniños += peso
        nume_niños +=1
    elif edad >=13 and edad <=29:
        pesojovenes += peso
        nume_jovenes +=1
    elif edad >=30 and edad <=59:
        pesoadultos += peso
        nume_adultos +=1
    elif edad >=60:
        pesoancianos += peso
        nume_ancianos +=1

if nume_niños >0:
    promedioniños = pesoniños/nume_niños
else:
    promedioniños =0
if nume_jovenes >0:
    promediojovenes = pesojovenes/nume_jovenes
else:
    promediojovenes=0
if nume_adultos >0:
    promedioadultos= pesoadultos/nume_adultos
else:
    promedioadultos=0
if nume_ancianos>0:
    promedioancianos = pesoancianos/nume_ancianos
else:
    promedioancianos=0
print("Promedio de peso niños:", promedioniños)
print("Promedio de peso jóvenes:", promediojovenes)
print("Promedio de peso adultos:", promedioadultos)
print("Promedio de peso ancianos:", promedioancianos)
opcion = 0

while opcion != 5:
    print(" MENU ")
    print("1. Ver promedio de peso niños")
    print("2. Ver promedio de peso jóvenes")
    print("3. Ver promedio de peso adultos")
    print("4. Ver promedio de peso ancianos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print("Promedio de peso niños:", promedioniños)
    elif opcion == 2:
        print("Promedio de peso jóvenes:", promediojovenes)
    elif opcion == 3:
        print("Promedio de peso adultos:", promedioadultos)
    elif opcion == 4:
        print("Promedio de peso ancianos:", promedioancianos)
    elif opcion == 5:
        print("Gracias por utilizar el sistema")
    else:
        print("Opción no válida")








