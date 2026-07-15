#!/usr/bin/python

# Proyecto: calcular el area de un cuadradi utilizando el operador para exponentes
# Creado por: NoobGoodLuck

try:
    lado=float(input("Introduce el valor del lado de un cuadrado: "))
    area=lado ** 2

    print(f"El área del cuadrado es: {area}")

except ValueError:
    print("Error: entrada no válida. Por favor introduce un número(ej: 5 o 2.5). ")
