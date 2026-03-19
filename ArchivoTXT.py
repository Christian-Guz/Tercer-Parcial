import os


"""
manejo de archivos de texto
Apertura de archivos
    open("archivo.txt", "r")
    

Modos principales:
r   Leer
w   Escribir (sobrescribir)
a   Agregar
x   Crear archivo

*****  Lectura de archivos
    *  archivo.read()
    *  archivo.readline()
    *  archivo.readlines() #Te generará una lista
    
*****  Escritura de archivos
    *  archivo.write("Texto a escribir")
    *  archivo.writelines(["Línea 1\n", "Línea 2\n"])
"""



def crear_archivo():
    nombre = input("Nombre del archivo: ")
    with open(nombre, "w") as archivo:
        print("Archivo creado correctamente")
        
crear_archivo()



def escribir_archivo():
    nombre = input("Nombre del archivo: ")
    texto = input("Escribir el texto a guardar: ")
    
    with open(nombre, "w") as archivo:
        archivo.write(texto)

    print("Texto guardado correctamente")
    
escribir_archivo()

print("Texto guardado correctamente")



def agregar_texto():
    nombre = input("Nombre del archivo: ")
    texto = input("Texto a agregar: ")
    
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)
        
    print("Texto agregado correctamente")
    
agregar_texto()

def leer_archivo():
    nombre = input("Nombre del archivo: ")
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")

leer_archivo()

def leer_archivo():
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

leer_archivo()

