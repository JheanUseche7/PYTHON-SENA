# CALCULAR LA CANTIDAD DE HOMBRES Y MUJERES PRESENTES EN UN SALÓN DE CLASES

# MODIFICACIÓN 1:
# Se cambió la finalización del programa.
# Ahora se utiliza un menú y termina cuando se selecciona la opción 5.

# MODIFICACIÓN 2:
# Se agregó un menú para consultar los resultados de forma individual.

# MODIFICACIÓN 3:
# Se incorporó .upper() para aceptar mayúsculas y minúsculas.

# MODIFICACIÓN 4:
# Se incorporó continue para ignorar datos incorrectos.

hombres = 0
mujeres = 0
opcion = 0

print("SISTEMA DE REGISTRO DEL SALON")

while opcion != 5:
    print("MENU")
    print("1. Registrar personas")
    print("2. Ver cantidad de hombres")
    print("3. Ver cantidad de mujeres")
    print("4. Ver todos los resultados")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        hombres = 0
        mujeres = 0
        n = int(input("Ingrese la cantidad de personas: "))
        # MODIFICACIÓN 5:
        # Se reemplazó el ciclo for por un ciclo while.

        contador = 1
        while contador <= n:
            sexo = input(f"Ingrese el sexo de la persona {contador} (H/M): ").upper()
            if sexo != "H" and sexo != "M":
                print("Sexo no valido")
                continue
            if sexo == "H":
                hombres += 1
            else:
                mujeres += 1
            contador += 1
        print("Datos registrados correctamente")

    elif opcion == 2:
        print("Cantidad de hombres:", hombres)
    elif opcion == 3:
        print("Cantidad de mujeres:", mujeres)
    elif opcion == 4:
        total = hombres + mujeres
        print("Cantidad de hombres:", hombres)
        print("Cantidad de mujeres:", mujeres)
        print("Total de personas:", total)
    elif opcion == 5:
        print("Gracias por utilizar el sistema")
    else:
        print("Opcion no valida")
