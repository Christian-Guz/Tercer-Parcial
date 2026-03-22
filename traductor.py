import tkinter as tk
from tkinter import messagebox

#CODIGO

#Diccionario
libro = {}
x = 0

#Cargar archivo
def cargar_archivo():
    with open("traducciones.txt", "r") as archivo:
        for texto in archivo:
            if ":" in texto:
                español, ingles = texto.strip().split(":")
                libro[español] = ingles
                
cargar_archivo()

#Espacio para escribir la palabra
def traducir():
    palabra_ = palabra.get("1.0", tk.END).strip()
    if libro:
        if palabra_:
            #Espacio para opciones de radiobotones
            opc = idioma.get()
            if opc == 1:
                for español in libro.keys():
                    if español.lower() == palabra_:
                        respuesta.config(text=libro[español])
                        return
                respuesta.config(text="No hay traducción")
            elif opc == 2:
                for español, ingles in libro.items():
                    if ingles.lower() == palabra_:
                        respuesta.config(text=español)
                        return
                respuesta.config(text="No hay traducción")
            else:
                messagebox.showerror("Error", "No se ha seleccionado una opción...")
                return
        else:
            messagebox.showerror("Error", "No se ha colocado una palabra...")
            return
    else:
        messagebox.showinfo("Sin existencia", "No existe una traducción para esta palabra...")
        return

#Agregar nueva palabra

def agregar_palabra():
    nueva_palabra_e = palabra_e.get("1.0", tk.END).strip()
    nueva_palabra_i = palabra_i.get("1.0", tk.END).strip()
    for español, inlges in libro:
        if español == nueva_palabra_e or inlges == nueva_palabra_i:
            messagebox.showinfo("Palabra repetido", "La palabra ya se encuentra registrada...")
            return
    if nueva_palabra_e and nueva_palabra_i:
        libro[f"{nueva_palabra_e}"] = nueva_palabra_i
        global x 
        x +=1
        with open("traducciones.txt", "a") as archivo:
            archivo.write(nueva_palabra_e + ":" + nueva_palabra_i + "\n")
    else:
        messagebox.showerror("Error","No se ha agregado una palabra")


#DISEÑO

#Creación de ventana
ventana = tk.Tk()
ventana.title("Traductor")
ventana.geometry("300x400")

#Creación de cuadro y botones de traducción
palabra = tk.Text(ventana, height=1, width=15)
palabra.pack(pady=20)

#Radio botones
idioma = tk.IntVar()

tk.Radiobutton(ventana, text="Españo-Inglés", variable=idioma, value=1).pack(pady=0)
tk.Radiobutton(ventana, text="Inglés-Español", variable=idioma, value=2).pack()

#Boton de traducción
ac_traducir = tk.Button(ventana, text="Traducir", command=traducir)
ac_traducir.pack(pady=20)

#Etiqueta de respuesta
respuesta = tk.Label(ventana, text="", font=("Arial", 12))
respuesta.pack(pady=10)

#Espacio para agregar nueva palabra
tk.Label(ventana, text="Agregar nueva palabra").pack(pady=0)
tk.Label(ventana, text="Español:").place(x=37, y=236)
palabra_e = tk.Text(ventana, height=1, width=15)
palabra_e.pack(pady=0)
tk.Label(ventana, text="Inglés:").place(x=40, y=255)
palabra_i = tk.Text(ventana, height=1, width=15)
palabra_i.pack(pady=0)
agergar = tk.Button(ventana, text="Agregar", command=agregar_palabra)
agergar.pack(pady=10)

ventana.mainloop()