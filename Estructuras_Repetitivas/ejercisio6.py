#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un 
#total de n personas. 
# Calcular la cantidad de hombres y mujeres

hombres = 0
mujeres = 0

n = int(input("Ingrese la cantidad de personas: "))
for i in range(n):
    sexo = input(f"Ingrese el sexo de la persona {i+1} (H/M): ")
    if sexo == "H":
        hombres += 1
    else:
        mujeres += 1
opcion = 0
while opcion != 2:
    print("\nMENU")
    print("1. Ver resultados")
    print("2. Salir")
    
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("Cantidad de hombres:", hombres)
        print("Cantidad de mujeres:", mujeres)
    elif opcion == 2:
        print("Programa finalizado")
    else:
        print("Opcion no valida")