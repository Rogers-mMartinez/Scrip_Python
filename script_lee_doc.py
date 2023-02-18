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

   #asignamos el contenido encontrado a la variable file_object 
   leer = file_objet.read()
   print(leer)

   #Como el metodo findall nos devuelve tuplas simplemente almacenamos el resultado segun el patron de busqueda
  
   a1=patron1.findall(leer)
   a2=patron2.findall(leer)
   a3=patron3.findall(leer)
   a4=patron4.findall(leer)

   """ DESCOMENTE ESTO PARA VER LAS SALIDAS POR SEPARADO
   print (patron1.findall(leer))
   print (patron2.findall(leer))
   print (patron3.findall(leer))
   print (patron4.findall(leer))
   """
   #luego concatenamos el resultado obtenido de cada patron a la variable a1 
   a1.extend(a2)
   a1.extend(a3)
   a1.extend(a4)

   #mostramos toda la informacion junta
   print(a1)

""" Preparamos la tupla para poder almacenarla en el archivo """
output = " ".join(a1)

#Abrimos el archivo con el que vamos a trabajar
archivofinal = open("Scrip_Python/archivoFinal.txt", "w")

# Escribimos la informacion en el archivo
archivofinal.write( output + os.linesep)

#Cerramos el archivo
archivofinal.close()

   #REFERENCIA: https://platzi.com/blog/expresiones-regulares-python/
   