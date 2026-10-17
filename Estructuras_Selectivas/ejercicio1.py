#Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobará 
# si su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario

print("Hola bienvenido")
nota1 = int (input("ingresa la nota N1 del aprendiz: "))
nota2 = int (input("Ingresa la nota N2 del aprendiz: "))
nota3 = int (input("Ingrese la nota N3 del aprendiz: "))

promedio =  (nota1 + nota2 + nota3)/3
if promedio > 70:
    print("APROBO EL APRENDIZ")
else:
    print("REPROBO EL APRENDIZ")

    
    


