import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

#CÓDIGO

#Sección de surtir
dic_ref ={
    "coca" : 5,
    "fanta" : 5,
    "sprite" : 5,
    "aga" : 5,
    "jarrito" : 5,
    "mundet" : 5
}

def surtir_ref(event):
    emergente = ctk.CTkToplevel()
    emergente.title("Surtir Refrescos")
    emergente.geometry("550x200")
    emergente.transient(ventana)
    emergente.grab_set()
    emergente.focus()
    refresco = surtir.get()
    ctk.CTkLabel(emergente, text=f"Ingrese la cantidad de {refresco} a surtir", font=("Arial", 15, "bold")).place_configure(x=30, y=15) 
    surtida = ctk.CTkEntry(emergente, font=("Arial", 15, "bold"))
    surtida.place_configure(x=10, y=205, width=650)
    def aceptar_sur():
        refresco = surtir.get().lower()
        try:
            valor = int(surtida.get())
            valor = valor + dic_ref[refresco]
            if valor < 0 :
                messagebox.showerror("Error", "El número para retirar es mayor de la existente...")
                surtida.delete(0, "end") 
                return
            else:
                dic_ref[refresco] = valor
                etiq_ref[refresco].configure(text=dic_ref[refresco])
                activacion_radio()
                emergente.destroy()
        except ValueError:
            messagebox.showerror("Error", "Solo se pueden ingresar número enteros o valores válidos...")
            surtida.delete(0, "end")
            return
    def cancelar_sur():
        emergente.destroy()
    ctk.CTkButton(emergente, text="Aceptar", font=("Arial", 12, "bold"),
                  fg_color="#242424", border_color="white", border_width=1, command=aceptar_sur).place_configure(x=550, y=20, width=100)
    ctk.CTkButton(emergente, text="Cancelar", font=("Arial", 12, "bold"),
                  fg_color="#242424", border_color="white", border_width=1, command=cancelar_sur).place_configure(x=550, y=80, width=100)

#Sección de cambio de precio

dic_ref_pre = 5

def cambio_precio():
    emergente = ctk.CTkToplevel()
    emergente.title("Cambio de precio")
    emergente.geometry("550x200")
    emergente.transient(ventana)
    emergente.grab_set()
    emergente.focus()
    ctk.CTkLabel(emergente, text="Ingrese el nuevo precio del producto", font=("Arial", 15, "bold")).place_configure(x=30, y=15)
    cambio = ctk.CTkEntry(emergente, font=("Arial", 15, "bold"))
    cambio.place_configure(x=10, y=205, width=650)
    def aceptar_cam():
        try:
            precio = float(cambio.get())
            if precio < 0:
                messagebox.showerror("Error", "No se pueden ingresar precios negativos...")
                cambio.delete(0, "end")
                return
            else:
                global dic_ref_pre
                dic_ref_pre = precio
                prec.configure(text=f"Precio: ${dic_ref_pre}")
                activacion_radio()
                emergente.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número...")
            cambio.delete(0, "end")
            return
    def cancelar_cam():
        emergente.destroy()
    ctk.CTkButton(emergente, text="Aceptar", font=("Arial", 12, "bold"), 
                  fg_color="#242424", border_color="white", border_width=1, command=aceptar_cam).place_configure(x=550, y=20, width=100)
    ctk.CTkButton(emergente, text="Cancelar", font=("Arial", 12, "bold"), 
                  fg_color="#242424", border_color="white", border_width=1, command=cancelar_cam).place_configure(x=550, y=80, width=100)

#Dinero entrante

dinero_ent = 0

def din_ent():
    try:    
        dinero = float(din_entrada.get())
        if dinero == 0.5 or dinero == 1 or dinero == 2 or dinero == 5 or dinero == 10:
            global dinero_ent
            dinero_ent = dinero_ent + dinero
            din_cont.configure(text=f"${dinero_ent}")
            din_camb.configure(text="Cambio: $0.0")
        else:
            messagebox.showwarning("Valor no aceptado", "El valor que se ingresó no coincide con el aceptado...")
            din_entrada.delete(0, "end")
        activacion_radio()
        din_entrada.delete(0, "end")
    except ValueError:
        messagebox.showerror("Error", "No se ingreso un valor...")
        din_entrada.delete(0, "end")

#Activación de radio botones
def activacion_radio():
    for refresco_act, refresco_num in dic_ref.items(): #Activación de radio botones
        if refresco_num == 0:
            r_ref[refresco_act].configure(state="disabled")
            opcion_refrescos.set(0)
            cuadro.configure(image=None)
            cuadro.image = None
        elif dinero_ent >= dic_ref_pre:
            r_ref[refresco_act].configure(state="normal")
        else:
            r_ref[refresco_act].configure(state="disabled")
            opcion_refrescos.set(0)
            cuadro.configure(image=None)
            cuadro.image = None

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
    #ref = valores[val]
    imagen = Image.open(im_ref[(val - 1)])
    fondo = ctk.CTkImage(imagen, size=(90, 275))
    cuadro.configure(image=fondo)
    cuadro.image = fondo

#Proceso de compra

im_peq = ["cocapeq.jpg", "fantapeq.jpg", "spritepeq.jpg", "agapeq.jpg", "jarritopeq.jpg", "mundetpeq.jpg"]

def compra():
    val = opcion_refrescos.get()
    if val:
        ref = valores[val]
        global dinero_ent
        cambio = dinero_ent - dic_ref_pre
        din_camb.configure(text=f"Cambio: ${cambio}")
        dinero_ent = 0
        din_cont.configure(text=f"${dinero_ent}")
        dic_ref[ref] -= 1
        etiq_ref[ref].configure(text=dic_ref[ref])
        
        gracias = ctk.CTkToplevel()
        gracias.title("Gracias por su compra")
        gracias.geometry("380x380")
        gracias.transient(ventana)
        gracias.grab_set()
        gracias.focus()
        ctk.CTkLabel(gracias, text="¡Gracias por su compra!", font=("Arial", 20, "bold")).pack(pady=20) 
        ctk.CTkLabel(gracias, text=f"Su cambio es: ${cambio}", font=("Arial", 17, "bold")).pack(pady=0)
        ctk.CTkLabel(gracias, text="Su prodcuto:", font=("Arial", 15, "bold")).pack(pady=20)
        cuadro_peq = ctk.CTkLabel(gracias, fg_color="white", text="")
        cuadro_peq.place_configure(x=167, y=200, width=150, height=220)
        imagen_peq = Image.open(im_peq[(val - 1)])
        fondo_peq = ctk.CTkImage(imagen_peq, size=(50, 150))
        cuadro_peq.configure(image=fondo_peq)
        cuadro_peq.image = fondo_peq
        cuadro.configure(image=None)
        cuadro.image = None
        opcion_refrescos.set(0)
        activacion_radio()
    else:
        messagebox.showwarning("Sin elección", "No se ha seleccionado un refresco...")

#DISEÑO

ventana = ctk.CTk()
ventana.title("Maquina de Refrescos")
ventana.geometry("500x700")

#Opción de susrtir productos

surt = ["Coca", "Fanta", "Sprite", "Aga", "Jarrito", "Mundet"]
surtir = ctk.CTkOptionMenu(ventana, corner_radius=0, fg_color="#242424", button_color="#242424", values=surt, command=surtir_ref)
surtir.place_configure(x=0,y=0, width=90, height=30)
ctk.CTkLabel(ventana, text="Surtir", bg_color="#242424").place_configure(x=0,y=0,width=60, height=30)

ctk.CTkButton(ventana, text="Cambiar Precio", command=cambio_precio, fg_color="#242424", corner_radius=0).place_configure(x=90, y=0, width=120, height=30)

#Etiquetas
ctk.CTkLabel(ventana, text="0.5, 1, 2, 5, 10", font=("Arial", 20, "bold")).place_configure(x=25, y=42)
din_cont = ctk.CTkLabel(ventana, text="$0.0", font=("Arial", 20, "bold"))
din_cont.place_configure(x=370, y=42)

#Entrada de dinero
din_entrada = ctk.CTkEntry(ventana, font=("Arial", 18, "bold"), justify="center")
din_entrada.place_configure(y=42, x=200, width=150)

#Botón
ctk.CTkButton(ventana, text="Ingresar", command=din_ent, font=("Arial", 14, "bold"), 
              border_color="white", border_width=1, fg_color="#242424").place_configure(y=110, x=50, width=130)
prec = ctk.CTkLabel(ventana, text="Precio: $5", font=("Arial", 20, "bold"))
prec.place_configure(x=320, y=108)

#Etiqueta de cambio
din_camb = ctk.CTkLabel(ventana, text="Cambio: $0.0", font=("Arial", 20, "bold"))
din_camb.place_configure(x=210, y=170)

#Cuadro de refrescos
refrescos = ctk.CTkFrame(ventana, border_width=2, border_color="white", fg_color="#242424")
refrescos.place_configure(x=35, y=225, width=550, height=610)
ctk.CTkLabel(ventana, text="Refrescos", font=("Arial", 20, "bold", "italic"), bg_color="#242424").place_configure(x=65, y=210, width=130)

#Radio botones junto con sus etiquetas
opcion_refrescos = ctk.IntVar()
r_coca = ctk.CTkRadioButton(refrescos, text="Coca", variable=opcion_refrescos, value=1, font=("Arial", 20, "bold"),
                        command=cambio_etiqueta_valor, state="disabled")
r_coca. place_configure(x=60, y=70)
val_coca = ctk.CTkLabel(refrescos, text="5", font=("Arial", 20, "bold"))
val_coca.place(x=170, y=55)

r_fanta = ctk.CTkRadioButton(refrescos, text="Fanta", variable=opcion_refrescos, value=2, font=("Arial", 20, "bold"), 
                         command=cambio_etiqueta_valor, state="disabled")
r_fanta. place(x=48, y=110)
val_fanta = ctk.CTkLabel(refrescos, text="5", font=("Arial", 20, "bold"))
val_fanta.place(x=170, y=109)

r_sprite = ctk.CTkRadioButton(refrescos, text="Sprite", variable=opcion_refrescos, value=3, font=("Arial", 20, "bold"), 
                          command=cambio_etiqueta_valor, state="disabled")
r_sprite. place(x=48, y=168)
val_sprite = ctk.CTkLabel(refrescos, text="5", font=("Arial", 20, "bold"))
val_sprite.place(x=170, y=166)

r_aga = ctk.CTkRadioButton(refrescos, text="Aga", variable=opcion_refrescos, value=4, font=("Arial", 20, "bold"), 
                       command=cambio_etiqueta_valor, state="disabled")
r_aga. place(x=48, y=225)
val_aga = ctk.CTkLabel(refrescos, text="5", font=("Arial", 20, "bold"))
val_aga.place(x=170, y=225)

r_jarrito = ctk.CTkRadioButton(refrescos, text="Jarrito", variable=opcion_refrescos, value=5, font=("Arial", 20, "bold"), 
                           command=cambio_etiqueta_valor, state="disabled")
r_jarrito. place(x=48, y=284)
val_jarrito = ctk.CTkLabel(refrescos, text="5", font=("Arial", 20, "bold"))
val_jarrito.place(x=170, y=284)

r_mundet = ctk.CTkRadioButton(refrescos, text="Mundet", variable=opcion_refrescos, value=6, font=("Arial", 20, "bold"), 
                          command=cambio_etiqueta_valor, state="disabled")
r_mundet. place(x=48, y=340)
val_mundet = ctk.CTkLabel(refrescos, text="5", font=("Arial", 20, "bold"))
val_mundet.place(x=170, y=339)

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
cuadro = ctk.CTkLabel(refrescos, fg_color="white", text="")
cuadro.place_configure(x=280, y=90, width=230, height=340)

#Boton para tomar refresco
ctk.CTkButton(refrescos, text="Tomar Refresco", font=("Arial", 14, "bold"), 
              fg_color="#242424", border_color="white", border_width=1, command=compra).place_configure(x=177, y=510, width=210, height=40)
ventana.mainloop()