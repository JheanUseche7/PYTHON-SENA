# 8. Un grupo de 23 estudiantes presentan un examen de algoritmia.
# Leer la calificación de cada estudiante y mostrar:
# - Cantidad de estudiantes con nota menor a 50.
# - Cantidad de estudiantes con nota entre 50 y 69.
# - Cantidad de estudiantes con nota entre 70 y 79.
# - Cantidad de estudiantes con nota de 80 o más.
# La nota debe estar entre 1 y 100.

menor50 = 0
entre50y69 = 0
entre70y79 = 0
mayor80 = 0

opcion = 0

while opcion != 3:
    print(" MENU ")
    print("1. Registrar notas")
    print("2. Ver resultados")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        menor50 = 0
        entre50y69 = 0
        entre70y79 = 0
        mayor80 = 0

        for i in range(23):
            nota = int(input(f"Ingrese la nota del estudiante {i+1}: "))
            if nota < 50:
                menor50 += 1
            elif nota < 70:
                entre50y69 += 1
            elif nota < 80:
                entre70y79 += 1
            else:
                mayor80 += 1
        print("Notas registradas correctamente")

    elif opcion == 2:
        print(" RESULTADOS ")
        print("Menores a 50:", menor50)
        print("Entre 50 y 69:", entre50y69)
        print("Entre 70 y 79:", entre70y79)
        print("80 o más:", mayor80)

    elif opcion == 3:
        print("Gracias por utilizar el sistema")
    else:
        print("Opcion no valida")
