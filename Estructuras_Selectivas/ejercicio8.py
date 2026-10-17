#8. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico 
#determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la 
#sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el 
#rango que le corresponde, se determina su resultado como positivo y en caso contrario como 
#negativo. La tabla en la que el médico se basa para obtener el resultado es la siguiente: 
#EDAD NIVEL HEMOGLOBINA 
#0 - 1 mes               13 - 26 g% 
#> 1 y < = 6 meses       10 - 18 g% 
#> 6 y < = 12 meses     11 - 15 g% 
#> 1 y < = 5 años       11.5 - 15 g% 
#> 5 y < = 10 años     12.6 - 15.5 g% 
#> 10 y < = 15 años    13 - 15.5 g% 
#mujeres > 15 años    12 - 16 g% 
#hombres > 15 años   14 - 18 g%

edad = float(input("Ingrese la edad: "))
hemoglobina = float(input("Ingrese la hemoglobina: "))

if edad <= 1/12:
    if hemoglobina < 13:
        print("Positivo para anemia")
    else:
        print("Negativo para anemia")

elif edad <= 6/12:
    if hemoglobina < 10:
        print("Positivo para anemia")
    else:
        print("Negativo para anemia")

elif edad <= 1:
    if hemoglobina < 11:
        print("Positivo para anemia")
    else:
        print("Negativo para anemia")

elif edad <= 5:
    if hemoglobina < 11.5:
        print("Positivo para anemia")
    else:
        print("Negativo para anemia")

elif edad <= 10:
    if hemoglobina < 12.6:
        print("Positivo para anemia")
    else:
        print("Negativo para anemia")

elif edad <= 15:
    if hemoglobina < 13:
        print("Positivo para anemia")
    else:
        print("Negativo para anemia")

else:
    sexo = input("Ingrese sexo (M/F): ")

    if sexo == "F":
        if hemoglobina < 12:
            print("Positivo para anemia")
        else:
            print("Negativo para anemia")
    else:
        if hemoglobina < 14:
            print("Positivo para anemia")
        else:
            print("Negativo para anemia")
