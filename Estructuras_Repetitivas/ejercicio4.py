# Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se 
#digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.

numero = int(input("Ingresa el numero que desea tener la tabla de multiplicar: "))
for i in range(10):
    tabla= numero*(i+1)
    print(f"{numero} X {i+1}={tabla}")
