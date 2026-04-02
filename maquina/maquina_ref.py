import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

#CODIGO

#Sección de surtir
dic_ref ={
    "coca" : 0,
    "fanta" : 0,
    "sprite" : 0,
    "aga" : 0,
    "jarrito" : 0,
    "mundet" : 0
}

def surtir_ref(event):
    emergente = tk.Toplevel()
    emergente.title("Surtir Refrescos")
    emergente.geometry("550x200")
    tk.Label(emergente, text="Ingrese la cantidad a surtir", font=("Arial", 11, "bold")).place(x=20, y=20) 
    surtida = tk.Entry(emergente, font=("Arial", 11, "bold"))
    surtida.place(x=10, y=170, width=520)
    def aceptar_sur():
        refresco = surtir.get().lower()
        try:
            valor = int(surtida.get())
            valor = valor + dic_ref[refresco]
            if valor < 0 :
                messagebox.showerror("Error", "El número para retirar es mayor de la existente...") 
            else:
                dic_ref[refresco] = valor
                etiq_ref[refresco].config(text=dic_ref[refresco])
                activacion_radio()
                emergente.destroy()
        except ValueError:
            messagebox.showerror("Error", "Solo se pueden ingresar número enteros o valores válidos...")
    def cancelar_sur():
        emergente.destroy()
    tk.Button(emergente, text="Aceptar", font=("Arial", 10), command=aceptar_sur).place(x=470, y=20, width=63)
    tk.Button(emergente, text="Cancelar", font=("Arial", 10), command=cancelar_sur).place(x=470, y=60)

#Sección de cambio de precio

dic_ref_pre ={
    "coca" : 5,
    "fanta" : 5,
    "sprite" : 5,
    "aga" : 5,
    "jarrito" : 5,
    "mundet" : 5
}

def cambio_precio(event):
    emergente = tk.Toplevel()
    emergente.title("Cambio de precio")
    emergente.geometry("550x200")
    tk.Label(emergente, text="Ingrese el nuevo precio del producto", font=("Arial", 11, "bold")).place(x=20, y=20)
    cambio = tk.Entry(emergente, font=("Arial", 11, "bold"))
    cambio.place(x=10, y=170, width=520)
    def aceptar_cam():
        precio = float(cambio.get())
        if precio < 0:
            messagebox.showerror("Error", "No se pueden ingresar precios negativos...")
        else:
            refresco = cambiar.get().lower()
            dic_ref_pre[refresco] = precio
            activacion_radio()
            emergente.destroy()
    def cancelar_cam():
        emergente.destroy()
    tk.Button(emergente, text="Aceptar", font=("Arial", 10), command=aceptar_cam).place(x=470, y=20, width=63)
    tk.Button(emergente, text="Cancelar", font=("Arial", 10), command=cancelar_cam).place(x=470, y=60)

#Dinero entrante

dinero_ent = 0

def din_ent():
    try:    
        dinero = float(din_entrada.get())
        if dinero == 0.5 or dinero == 1 or dinero == 2 or dinero == 5 or dinero == 10:
            global dinero_ent
            dinero_ent = dinero_ent + dinero
            din_cont.config(text=f"${dinero_ent}")
            din_camb.config(text="Cambio: $0.0")
        else:
            messagebox.showwarning("Valor no aceptado", "El valor que se ingresó no coincide con el aceptado...")
        activacion_radio()
        din_entrada.delete(0, "end")
    except ValueError:
        messagebox.showerror("Error", "No se ingreso un valor...")

#Activación de radio botones
def activacion_radio():
    for refresco,precio in dic_ref_pre.items(): #Activación de radio botones
        if dic_ref[refresco] == 0:
            r_ref[refresco].config(state="disabled")
        elif dinero_ent >= precio:
            r_ref[refresco].config(state="active")
        else:
            r_ref[refresco].config(state="disabled")

#Funciones de radiobotones

valores = {
    1 : "coca",
    2 : "fanta",
    3 : "sprite",
    4 : "aga",
    5 : "jarrito",
    6 : "mundet"
}

im_ref = ["coca.jpg", "fanta.jpg", "sprite.jpg", "aga.jpg", "jarrito.jpg", "mundet.jpg"]

def cambio_etiqueta_valor():
    val = opcion_refrescos.get()
    ref = valores[val]
    precio = dic_ref_pre[ref]
    prec.config(text=f"Precio: ${precio}")
    imagen = Image.open(im_ref[(val - 1)])
    fondo = ImageTk.PhotoImage(imagen)
    cuadro.config(image=fondo)
    cuadro.image = fondo
    
#Proceso de compra

im_peq = ["cocapeq.jpg", "fantapeq.jpg", "spritepeq.jpg", "agapeq.jpg", "jarritopeq.jpg", "mundetpeq.jpg"]

def compra():
    val = opcion_refrescos.get()
    if val:
        ref = valores[val]
        global dinero_ent
        cambio = dinero_ent - dic_ref_pre[ref]
        din_camb.config(text=f"Cambio: ${cambio}")
        dinero_ent = 0
        din_cont.config(text=f"${dinero_ent}")
        dic_ref[ref] -= 1
        etiq_ref[ref].config(text=dic_ref[ref])
        
        gracias = tk.Toplevel()
        gracias.title("Gracias por su compra")
        gracias.geometry("380x380")
        tk.Label(gracias, text="Gracias por su compra", font=("Arial", 14, "bold")).pack(pady=20) 
        tk.Label(gracias, text=f"Su cambio es: ${cambio}", font=("Arial", 12, "bold")).pack(pady=0)
        tk.Label(gracias, text="Su prodcuto:", font=("Arial", 10, "bold")).pack(pady=20)
        cuadro_peq = tk.Label(gracias, fg="black", bg="white", relief="solid")
        cuadro_peq.place(x=113, y=140, width=150, height=220)
        imagen_peq = Image.open(im_peq[(val - 1)])
        fondo_peq = ImageTk.PhotoImage(imagen_peq)
        cuadro_peq.config(image=fondo_peq)
        cuadro_peq.image = fondo_peq
        cuadro.config(image="")
        cuadro.image = None
        opcion_refrescos.set(0)
        activacion_radio()
    else:
        messagebox.showwarning("Sin elección", "No se ha seleccionado un refresco...")

#Cuadro de agradecimiento
"""def cuadro_gracias():
    gracias = tk.Toplevel()
    gracias.title("Gracias por su compra")
    gracias.geometry("380x380")
    tk.Label(gracias, text="Gracias por su compra", font=("Arial", 14, "bold")).pack(pady=20) 
    tk.Label(gracias, text=f"Su cambio es: ${}", font=("Arial", 12, "bold")).pack(pady=20)""" 
    
#DISEÑO

#Ventana
ventana = tk.Tk()
ventana.title("Máquina de refrescos")
ventana.geometry("500x700")

#Opción de surtir productos
surt = ["Coca", "Fanta", "Sprite", "Aga", "Jarrito", "Mundet"]
surtir = ttk.Combobox(ventana, values=surt)
surtir.set("Surtir")
surtir.place(x=0,y=0, width=60)
tk.Label(ventana, text="Surtir", font=("Arial", 9), bg="white").place(x=0,y=1,width=43, height=18)

surtir.bind("<<ComboboxSelected>>", surtir_ref)

#Opción de cambiar precio
camb = ["Coca", "Fanta", "Sprite", "Aga", "Jarrito", "Mundet"]
cambiar = ttk.Combobox(ventana, values=camb)
cambiar.set("Cambiar Percio")
cambiar.place(x=59, y=0, width=110)
tk.Label(ventana, text="Cambiar Precio", font=("Arial", 9), bg="white").place(x=61,y=1,width=85, height=18)

cambiar.bind("<<ComboboxSelected>>", cambio_precio)

#Etiquetas
tk.Label(ventana, text="0.5, 1, 2, 5, 10", font=("Arial", 15, "bold")).place(x=12, y=30)
din_cont = tk.Label(ventana, text="$0.0", font=("Arial", 15, "bold"))
din_cont.place(x=280, y=30)

#Entrada de dinero
din_entrada = tk.Entry(ventana, font=("Arial", 12, "bold"), justify="center")
din_entrada.place(y=33, x=155, width=120)

#Botón
tk.Button(ventana, text="Ingresar", font=("Arial", 10, "bold"), command=din_ent).place(y=80, x=35, width=110)
prec = tk.Label(ventana, text="Precio: $0", font=("Arial", 15, "bold"))
prec.place(x=240, y=78)

#Etiqueta de cambio
din_camb = tk.Label(ventana, text="Cambio: $0.0", font=("Arial", 15, "bold"))
din_camb.place(x=170, y=130)

#Cuadro de refrescos
refrescos = tk.LabelFrame(ventana, text="Refrescos", font=("Arial", 15, "bold", "italic"))
refrescos.place(x=30, y=160, width=440, height=500)

#Radio botones junto con sus etiquetas
opcion_refrescos = tk.IntVar()
r_coca = tk.Radiobutton(refrescos, text="Coca", variable=opcion_refrescos, value=1, font=("Arial", 15, "bold"),
                        command=cambio_etiqueta_valor, state="disabled")
r_coca. place(x=30, y=50)
val_coca = tk.Label(refrescos, text="0", font=("Arial", 15, "bold"))
val_coca.place(x=160, y=54)

r_fanta = tk.Radiobutton(refrescos, text="Fanta", variable=opcion_refrescos, value=2, font=("Arial", 15, "bold"), 
                         command=cambio_etiqueta_valor, state="disabled")
r_fanta. place(x=30, y=100)
val_fanta = tk.Label(refrescos, text="0", font=("Arial", 15, "bold"))
val_fanta.place(x=160, y=104)

r_sprite = tk.Radiobutton(refrescos, text="Sprite", variable=opcion_refrescos, value=3, font=("Arial", 15, "bold"), 
                          command=cambio_etiqueta_valor, state="disabled")
r_sprite. place(x=30, y=150)
val_sprite= tk.Label(refrescos, text="0", font=("Arial", 15, "bold"))
val_sprite.place(x=160, y=154)

r_aga = tk.Radiobutton(refrescos, text="Aga", variable=opcion_refrescos, value=4, font=("Arial", 15, "bold"), 
                       command=cambio_etiqueta_valor, state="disabled")
r_aga. place(x=30, y=200)
val_aga = tk.Label(refrescos, text="0", font=("Arial", 15, "bold"))
val_aga.place(x=160, y=204)

r_jarrito = tk.Radiobutton(refrescos, text="Jarrito", variable=opcion_refrescos, value=5, font=("Arial", 15, "bold"), 
                           command=cambio_etiqueta_valor, state="disabled")
r_jarrito. place(x=30, y=250)
val_jarrito = tk.Label(refrescos, text="0", font=("Arial", 15, "bold"))
val_jarrito.place(x=160, y=254)

r_mundet = tk.Radiobutton(refrescos, text="Mundet", variable=opcion_refrescos, value=6, font=("Arial", 15, "bold"), 
                          command=cambio_etiqueta_valor, state="disabled")
r_mundet. place(x=30, y=300)
val_mundet = tk.Label(refrescos, text="0", font=("Arial", 15, "bold"))
val_mundet.place(x=160, y=304)

etiq_ref = {
    "coca" : val_coca,
    "fanta" : val_fanta,
    "sprite" : val_sprite,
    "aga" : val_aga,
    "jarrito" : val_jarrito,
    "mundet" : val_mundet
}
r_ref = {
    "coca" : r_coca,
    "fanta" : r_fanta,
    "sprite" : r_sprite,
    "aga" : r_aga,
    "jarrito" : r_jarrito,
    "mundet" : r_mundet
}

#Imagen de refrescos
cuadro = tk.Label(refrescos, fg="black", bg="white", relief="solid")
cuadro.place(x=220, y=55, width=190, height=275)

#Boton para tomar refresco
tk.Button(refrescos, text="Tomar Refresco", font=("Arial", 12, "bold"), command=compra).place(x=120, y=380, width=180)

ventana.mainloop()