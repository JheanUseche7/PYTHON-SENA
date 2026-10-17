# 9. Calcular el promedio de edades de hombres,
# mujeres y de todo un grupo de alumnos.

suma_hombres = 0
suma_mujeres = 0
cant_hombres = 0
cant_mujeres = 0
opcion = 0
while opcion != 3:
    print(" MENU ")
    print("1. Ingresar datos")
    print("2. Ver promedios")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        n = int(input("Ingrese la cantidad de alumnos: "))
        for i in range(n):
            sexo = input(f"Ingrese el sexo del alumno {i+1} (H/M): ")
            edad = int(input("Ingrese la edad: "))
            if sexo == "H":
                suma_hombres += edad
                cant_hombres += 1
            else:
                suma_mujeres += edad
                cant_mujeres += 1
    elif opcion == 2:
        promedio_hombres = suma_hombres / cant_hombres
        promedio_mujeres = suma_mujeres / cant_mujeres
        promedio_grupo = (suma_hombres + suma_mujeres) / (cant_hombres + cant_mujeres)

        print("Promedio hombres:", promedio_hombres)
        print("Promedio mujeres:", promedio_mujeres)
        print("Promedio grupo:", promedio_grupo)

    elif opcion == 3:
        print("Programa finalizado")
    else:
        print("Opcion no valida")
