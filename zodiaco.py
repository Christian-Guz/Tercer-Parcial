import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#CÓDIGO

#Registro de texto
def saludar():
    saludo = nombre.get()
    paterno = a_paterno.get()
    materno = a_materno.get()
    if saludo and paterno and materno:
        saludo_efe.config(text=f"Hola {saludo} {paterno} {materno}", font=("Arial", 15, "bold"))
        return
    else:
        messagebox.showerror("Error", "Uno de los datos no fue registrado...")
        return

def años_signos():
    try:
        mes = int(ing_mes.get())
        año = int(ing_año.get())
        dia = int(ing_dia.get())
        edad = 0
        edad = 2026 - año
        if mes >= 3:
            edad = edad - 1
        edad_efe.config(text=f"Tienes {edad} años", font=("Arial", 15, "bold"))
        animal = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", 
              "Caballo", "Cabra", "Mono", "Gallo","Perro", "Cerdo"]
        imagenes = ["Rata.jpg","Buey.jpg","Tigre.jpg","Conejo.jpg","Dragon.jpg","Serpiente.jpg",
                    "Caballo.jpg","Cabra.jpg","Mono.jpg","Gallo.jpg","Perro.jpg","Cerdo.jpg"]
        i = 0
        for x in range(1864,2027):
            if x == año:
                signo_efe.config(text=f"Tu signo zodiacal\nes {animal[i]}", font=("Arial", 15, "bold"))
                imagen_signo = tk.Label(cuadro)
                imagen_signo.place(y=270, x=120, height=120, width=153)
                imagen = Image.open(imagenes[i])
                fondo = ImageTk.PhotoImage(imagen)
                imagen_signo.config(image=fondo)
                imagen_signo.image = fondo
            i += 1
            if i == 12:
                i = 0
        return
    except ValueError:
        messagebox.showerror("Error", "Una de las fechas no se ha registrado correctamente...")
        return
def generos():
    gen = genero.get()
    if gen == 1 or gen == 2:
        pass
    else:
        messagebox.showerror("Error", "No se ha seleccionado el género...")
    
def acciones():
    saludar()
    años_signos()
    generos()

#DISEÑO

#Ventana
ventana = tk.Tk()
ventana.title("Zodiaco")
ventana.geometry("1000x500")

#Línea central
tk.Label(ventana, bg="black").place(x=500,y=2,height=480)

#Etiquetas (Lado izquierdo)
tk.Label(ventana, text="Datos personales", font=("Arial", 15, "bold")).place(x=165, y=15)
tk.Label(ventana, text="Nombre:", font=("Arial", 12, "bold")).place(x=106, y=70)
tk.Label(ventana, text="Apellido Paterno:", font=("Arial", 12, "bold")).place(x=40, y=100)
tk.Label(ventana, text="Apellido Materno:", font=("Arial", 12, "bold")).place(x=38, y=130)
tk.Label(ventana, text="Fecha de Nacimiento", font=("Arial", 15, "bold")).place(x=151, y=180)
tk.Label(ventana, text="Día", font=("Arial", 12, "bold")).place(y=220, x=150)
tk.Label(ventana, text="Mes", font=("Arial", 12, "bold")).place(y=220, x=232)
tk.Label(ventana, text="Año", font=("Arial", 12, "bold")).place(y=220, x=314)
tk.Label(ventana, text="Sexo", font=("Arial", 12, "bold")).place(y=290, x=100)

#Entradas de texto
nombre = tk.Entry(ventana, font=("Arial", 12, "bold"))
nombre.place(x=180, y=72, width=200)

a_paterno = tk.Entry(ventana, font=("Arial", 12, "bold"))
a_paterno.place(x=180, y=102, width=200)

a_materno = tk.Entry(ventana, font=("Arial", 12, "bold"))
a_materno.place(x=180, y=132, width=200)

ing_dia = tk.Entry(ventana, font=("Arial", 12, "bold"), justify="center")
ing_dia.place(y=250, x=130, width=70)
tk.Label(ventana, text="/", font=("Arial",15, "bold")).place(y=247, x=201)

ing_mes = tk.Entry(ventana, font=("Arial", 12, "bold"), justify="center")
ing_mes.place(y=250, x=214, width=70)
tk.Label(ventana, text="/", font=("Arial",15, "bold")).place(y=247, x=285)

ing_año = tk.Entry(ventana, font=("Arial", 12, "bold"), justify="center")
ing_año.place(y=250, x=298, width=70)

#Radio Botones
genero = tk.IntVar()
tk.Radiobutton(ventana, text="Masculino", variable=genero, value=1, font=("Arial", 10, "bold")).place(y=320, x=100)
tk.Radiobutton(ventana, text="Femenino", variable=genero, value=2, font=("Arial", 10, "bold")).place(y=350, x=100)

#Botón
tk.Button(ventana, text="Imprimir", font=("Arial", 12, "bold"), command=acciones).place(y=400, x=180, width=150)

#Etiquetas (Lado derecho)
cuadro = tk.LabelFrame(ventana)
cuadro.place(height=450, width=400, x=560, y=20)

saludo_efe = tk.Label(cuadro, text="")
saludo_efe.pack(pady=50)

edad_efe = tk.Label(cuadro, text="")
edad_efe.pack(pady=0)

signo_efe = tk.Label(cuadro, text="")
signo_efe.pack(pady=50)

ventana.mainloop()