# 11. Pedir los datos de los alumnos, estos son:
# sexo, edad y altura.
# Al final del programa se deberá mostrar:
# - La cantidad de hombres.
# - La cantidad de mujeres.
# - La altura promedio.
# - La cantidad de alumnos que tienen una altura mayor a 1.70 m.
# - La cantidad de alumnos que tienen una altura menor o igual a 1.50 m.
# El programa debe finalizar cuando la edad sea igual a 0.

hombres = 0
mujeres = 0
suma_alturas = 0
cantidad_alumnos = 0
mayor170 = 0
menor150 = 0

opcion = 0
while opcion != 3:
    print(" MENU ")
    print("1. Ingresar alumnos")
    print("2. Ver resultados")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        edad = 1
        while edad != 0:
            edad = int(input("Ingrese la edad (0 para terminar): "))
            if edad != 0:
                sexo = input("Ingrese el sexo (H/M): ")
                altura = float(input("Ingrese la altura: "))
                cantidad_alumnos += 1
                suma_alturas += altura
                if sexo == "H":
                    hombres += 1
                else:
                    mujeres += 1
                if altura > 1.70:
                    mayor170 += 1
                if altura <= 1.50:
                    menor150 += 1
    elif opcion == 2:
        promedio = suma_alturas / cantidad_alumnos
        print("Cantidad de hombres:", hombres)
        print("Cantidad de mujeres:", mujeres)
        print("Altura promedio:", promedio)
        print("Cantidad de alumnos con altura mayor a 1.70:", mayor170)
        print("Cantidad de alumnos con altura menor o igual a 1.50:", menor150)

    elif opcion == 3:
        print("Programa finalizado")
    else:
        print("Opcion no valida")