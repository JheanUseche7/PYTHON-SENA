#Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio 
#aeróbico; la fórmula que se aplica es: 
# cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10 
# y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10

edad = int(input("Ingrese la edad: "))
genero = int(input("ingresa el genero: 1=MASCULINO 2=FEMENINO: "))
if genero == 1:
    num_pul = (210 - edad)/10
    print("numero de pulsaciones en 10 segundos es de:",num_pul)
elif genero == 2:
    num_pul = (220 - edad)/10
    print("numero de pulsaciones en 10 segundos es de:",num_pul)
else:
    print("NO INGRESASTE LA INFORMACION REQUERIDA")


    


    
