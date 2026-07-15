#!/usr/bin/python

# Proyecto: conversor de yuanes chinos a lempiras tomar en cuenta que estos valores son de 14/06/2026
# Creado por: NoobGoodLuck

float tasa_de_cambio=3.94

try:
    yuanes=float(input("Introduce la cantidad de yuanes a convertir a lempiras "))

    lempiras=tasa_de_cambio*yuanes

    print(f"{yuanes} yuanes equivalen a {lempiras: .2f} lempiras ")

    # en la variable lempiras dentro de las llaves dentro del print el : .f 
    # el . indica que se ajustara las decimales del float y el 2f indica que se redondeara a 2 dígitos despues del .

except ValueError:
    print("Error: Entrada no válida. Por favor, introduzca un valor numérico. ")
