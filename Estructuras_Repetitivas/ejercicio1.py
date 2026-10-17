# 1. Leer 20 números e imprimir cuantos son  positivos, cuantos negativos y cuantos 
#neutros

positivos = 0
negativos = 0
neutros = 0

for i in range(20):
    numeros = float(input(f"Ingresa el numero {i + 1}: "))
    if numeros <0:
     negativos += 1
    elif numeros >0:
     positivos +=1
    else:
     neutros +=1

print("numeros positivos", positivos)
print("numeros negativos", negativos)
print("numeros neutros", neutros)

