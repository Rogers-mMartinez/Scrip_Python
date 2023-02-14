#Que lea un arcivo de texto y que identifique un patron, cuando hay secuencia de numeros


"""con esta funcion lo que hara es meterse a la carpeta que esta ubicado el programa y va a buscar el "archivo txt prueba" y luego que lo encuentra 
lo regresa como un objeto y python le va asignar como nombre file_objet con la palabra with cierra el archivo una vez que el acceso a este ya no es necesario"""

with open("txt de prueba.txt") as file_objet:
    leer = file_objet.read()
    print(leer)
    #  print(leerrstrip()) con esto borramos los espacios en blanco (Saltos de linea sin nada en ella)
    
