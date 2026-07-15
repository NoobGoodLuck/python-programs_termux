#!/usr/bin/python

# Proyecto: recopila datos de diferentes tipos
# Creado por: NoobGoodLuck

# El try y el except es para que cuando el código falle no explote y en vez de eso mande un anuncio al usuario de texto o imagen de que no se cumplió la petición. A diferenciq del if else (que son controladores de desiciones), el try y el except son controladores de resultados.

try:

    nombre=input("Introduce tu nombre (texto): ")
    edad=int(input("Introduce tu edad (entero): "))
    altura=float(input("Introduce tu altura (decimal): "))

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Altura: {altura}m")

except ValueError:

    print("\n[!] ERROR CRÍTICO: ")
    print("Has introducido un texto donde se esperaba un número. ")
    print("Por favor, reinicia el programa e introduce datos válidos (ej: edad 20, altura 1.70). ")
