 #Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos 
#números.

suma = 0

for i in range(10):
    numeros = int(input(f"Ingresa el {i + 1} numero: "))
    if numeros <0:
     positivos = abs(numeros)
     suma += positivos
    else:
     print("El numero ingresado no es NEGATIVO")
print("La suma de los numeros es: ",suma)

