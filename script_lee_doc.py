#Que lea un arcivo de texto y que identifique un patron, cuando hay secuencia de numeros
#importacion de la libreria necesaria para trabajar con expresiones regulares
import re
#Importacion de la libreria para poder manipular archivos 
import os

"""con esta funcion lo que hara es meterse a la carpeta que esta ubicado el programa y va a buscar el "archivo txt prueba" y luego que lo encuentra 
lo regresa como un objeto y python le va asignar como nombre file_objet con la palabra with cierra el archivo una vez que el acceso a este ya no es necesario"""
#Patron para encontrar numeros
patron1 = re.compile('[0-9]+')

# Patron para encontrar numeros con letras
patron2 = re.compile('([0-9]+[a-z]+)')

# Patron para encontrar vocales
patron3 = re.compile('([a,e,i,o,u]+)')

#Patron para encontrar simbolos especiales
patron4 = re.compile('([*,&,$,@,#])')

#leemos el archivo
with open("Scrip_Python/prueba.txt") as file_objet:

with open("txt de prueba.txt") as file_objet:
    leer = file_objet.read()
    print(leer)
    #  print(leerrstrip()) con esto borramos los espacios en blanco (Saltos de linea sin nada en ella)
    
