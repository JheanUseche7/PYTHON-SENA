#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
#Realizar un algoritmo para calcular el promedio  y la calificación más alta y  más baja 
#de todo el grupo. 

suma = 0
for i in range(20):
    notas = int(input(f"Ingresa la {i + 1} nota: "))
    suma += notas

    if i == 0:
        mayor = notas
        menor = notas
    else:
        if notas > mayor:
            mayor = notas
        if notas < menor:
            menor = notas

promedio = suma / 20
opcion = 0
while opcion != 5:
    print("\n--- MENU ---")
    print("1. Ver promedio")
    print("2. Ver nota mayor")
    print("3. Ver nota menor")
    print("4. Ver todos los resultados")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("El promedio es:", promedio)
    elif opcion == 2:
        print("La nota mayor es:", mayor)
    elif opcion == 3:
        print("La nota menor es:", menor)
    elif opcion == 4:
        print("Promedio:", promedio)
        print("Mayor:", mayor)
        print("Menor:", menor)
    elif opcion == 5:
        print("Gracias por utilizar el sistema")
    else:
        print("Opcion no valida")
