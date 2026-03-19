import os

"""def crear_archivo():
    nombre = input("Nombre del archivo: ")
    with open(nombre, "w") as archivo:
        print("Archivo creado correctamente")
        
crear_archivo()"""

"""def escribir_archivo():
    nombre = input("Nombre del archivo: ")
    texto = input("Escribir el texto a guardar: ")
    
    with open(nombre, "w") as archivo:
        archivo.write(texto)

    print("Texto guardado correctamente")
    
escribir_archivo()"""

"""def agregar_texto():
    nombre = input("Nombre del archivo: ")
    texto = input("Texto a agregar: ")
    
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)

    print("Texto agregado correctamente")
    
agregar_texto()"""

"""def leer_archivo():
    #nombre = input("Nombre del archivo: ")
    nombre = "ejemplo.txt"
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            os.system("cls")
            print("\nContenido del archivo:")
            print(contenido)
            print("-----------------------")
            archivo.seek(0)
            contenido = archivo.read()
            print(contenido)
            
    except FileNotFoundError:
        print("El archivo no existe")

leer_archivo()"""

"""def leer_archivo():
    #nombre = input("Nombre del archivo: ")
    nombre = "ejemplo.txt"
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.readline()
            os.system("cls")
            print("\nContenido del archivo:")
            print(contenido)
            contenido = archivo.readline()
            print(contenido)
            
    except FileNotFoundError:
        print("El archivo no existe")

leer_archivo()"""

def leer_archivo():
    #nombre = input("Nombre del archivo: ")
    nombre = "ejemplo.txt"
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.readlines()
            os.system("cls")
            print("\nContenido del archivo:")
            print(contenido)
            
            for line in contenido:
                print(line.strip())
            
    except FileNotFoundError:
        print("El archivo no existe")

leer_archivo()
