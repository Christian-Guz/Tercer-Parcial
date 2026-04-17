import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#CÓDIGO

total_sumado = 0
def agregar():
    global tamaños
    global ingrediente
    global subprecio_total 
    subprecio_total = 0
    ingrediente = 0
    nombre = ent_nombre.get().title()
    direccion = ent_direccion.get()
    telefono = ent_telefono.get().strip()
    if nombre and direccion and telefono: #opciones de Radio Botones
        if not telefono.isdigit():
            messagebox.showerror("Error", "El número de teléfono no es válido...")
            return
        if tamaño.get() != 0:
            if tamaño.get() == 1:
                subprecio_total += 40
                tamaños = "Chica"
            elif tamaño.get() == 2:
                subprecio_total += 80
                tamaños = "Mediana"
            elif tamaño.get() == 3:
                subprecio_total += 120
                tamaños = "Grande"
        else:
            messagebox.showerror("Error", "No se ha registrado un tamaño de pizza...")
            return
        opcion = False
        if jamon.get(): #Opciones de sabores
            subprecio_total += 10
            opcion = True
            ingrediente = "Jamón"
        if piña.get():
            subprecio_total += 10
            opcion = True
            ingrediente = f"{ingrediente} / Piña"
        if champiñones.get():
            subprecio_total += 10
            opcion = True
            ingrediente = f"{ingrediente} / Champiñones"
        if opcion == False:
            messagebox.showerror("Error", "No se ha registrado un ingrediente...")
            return
    else:
        messagebox.showerror("Error", "No se ha registrado un dato correctamente...")
        return
    try:
        global num_pizza
        num_pizza = int(ent_pizzas.get())
        if num_pizza <= 0:
            messagebox.showerror("Error", "No se pueden registrar números inválidos o negativos...")
            return
        else:
            global precio_total
            precio_total = subprecio_total * num_pizza
    except ValueError:
        messagebox.showerror("Error", "El número de pizzas es inválido...")
        return

    #Proceso para poner la información en las columnas
    dato = ("°", tamaños, ingrediente, num_pizza, f"${precio_total}")
    tabla.insert("", tk.END, values=dato)
    global total_sumado
    total_sumado += precio_total
    tamaño.set(0)
    jamon.deselect()
    piña.deselect()
    champiñones.deselect()
    ent_pizzas.delete(0, "end")
    
def eliminar():
    if tabla.selection():
        respuesta = messagebox.askyesno("Eliminar", "¿Quiere eliminar esta orden?")
        if respuesta:
            seleccion = tabla.selection()
            for item in seleccion:
                tabla.delete(item)
            calculo_por_eliminacion()
        else:
            pass
    else:
        messagebox.showerror("Error", "No se ha seleccionado una orden...")

def calculo_por_eliminacion():
    global total_sumado
    total_sumado = 0
    for item in tabla.get_children():
        valores = tabla.item(item, "values")
        sub = int(valores[4].replace("$", ""))
        cantidad = int(valores[3])
        total_sumado += sub 
        
#Botón de terminar
ventas_tot_dia = 0 
ventas = []     
def terminar():
    global ventas_tot_dia
    guardar_total()
    global ventas
    global total_sumado
    if total_sumado == 0:
        messagebox.showerror("Error", "No se ha generado ningún registro...")
        return
    else:
        nombre = ent_nombre.get().title()
        ventas.append(f"{nombre} total ${total_sumado}")
        if len(ventas) > 4:
            ventas.pop(0)
        etiquetas = [nom1, nom2, nom3, nom4]
        for x, v in enumerate(ventas):
            etiquetas[x].configure(text=v)
        ventas_tot_dia += total_sumado
        ventas_tot.configure(text=f"Ventas total del día: ${ventas_tot_dia}")  
        agregar_compras()   
        agregar_total()
        ticket = ctk.CTkToplevel()
        ticket.title("Ticket")
        ticket.geometry("300x200")
        ticket.transient(ventana)
        ticket.grab_set()
        ticket.focus()
        ctk.CTkLabel(ticket, text="¡Gracias por su compra!", font=("Arial", 18, "bold")).pack(pady=(40,0))
        ctk.CTkLabel(ticket, text=f"El precio a pagar es de: ${total_sumado}", font=("Arial", 17, "bold")).pack(pady=(40,0))
        ent_nombre.delete(0, "end")
        ent_direccion.delete(0, "end")
        ent_telefono.delete(0, "end")
        total_sumado = 0
        tabla.delete(*tabla.get_children())

def agregar_compras():
    with open("pedido.txt", "a") as archivo:
        archivo.write(f"Cliente: {ent_nombre.get()}\n\nOrden de pizza(s):\n")
        for item in tabla.get_children():
            valores = tabla.item(item, "values")
            tamaño_t = valores[1]
            ingrediente_t = valores[2]
            num_pizzas_t = valores[3]
            sub_total_t = valores[4]
            archivo.write(f"|Tamaño: {tamaño_t}|Ingrediente(s): {ingrediente_t}|Num. de pizzas: {num_pizzas_t}|Total: {sub_total_t}\n")
        archivo.write("-----------------------------------------------\n")
        
def agregar_total():
    with open("pedido.txt", "r+") as archivo:
        lineas = archivo.readlines()
        archivo.seek(0)
        global con_registro
        con_registro = False
        for linea in lineas:
            if "Ventas totales:" not in linea:
                archivo.write(linea)
        archivo.write(f"\nVentas totales: ${ventas_tot_dia}\n")
        archivo.truncate()

def guardar_total():
    global ventas_tot_dia
    with open("pedido.txt", "r") as archivo:
        lineas = archivo.readlines()
        archivo.seek(0)
        for linea in lineas:
            if "Ventas totales:" in linea:
                ventas_tot_dia = int(linea.strip().split("$")[1])
            
#DISEÑO

ventana = ctk.CTk()
ventana.geometry("1300x650")
ventana.title("Maquina de pizzas")

#Ventanas
ctk.CTkLabel(ventana, fg_color="#99B4D1", corner_radius=0, text="").place_configure(x=0, y=0, width=1626, height=300)
ctk.CTkLabel(ventana, fg_color="#99B4D1", corner_radius=0, text="").place_configure(x=0, y=310, width=1626, height=502)

#Nombre
ctk.CTkLabel(ventana, text="Nombre:", font=("Arial", 15, "bold"), 
             fg_color="#99B4D1", text_color="black", bg_color="#99B4D1").place_configure(x=60, y=50)
ent_nombre = ctk.CTkEntry(ventana, font=("Arial", 15, "bold"), bg_color="#99B4D1", fg_color="white", text_color="black")
ent_nombre.place_configure(x=150, y=50, width=250)

fr_tamaño = ctk.CTkFrame(ventana, border_color="white", border_width=2, fg_color="#99B4D1", bg_color="#99B4D1")
fr_tamaño.place_configure(x=50, y=120, width=400, height=160)
ctk.CTkLabel(ventana, text="Tamaño Pizza", fg_color="#99B4D1", bg_color="#99B4D1", text_color="white", 
             font=("Arial", 13, "bold", "italic")).place_configure(x=60, y=105, width=115)
tamaño = ctk.IntVar()
ctk.CTkRadioButton(fr_tamaño, text="Chica $40", variable=tamaño, value=1, font=("Arial", 14, "bold"), text_color="white").place_configure(x=40, y=30)
ctk.CTkRadioButton(fr_tamaño, text="Mediana $80", variable=tamaño, value=2, font=("Arial", 14, "bold"), text_color="white").place_configure(x=40, y=70)
ctk.CTkRadioButton(fr_tamaño, text="Grande $120", variable=tamaño, value=3, font=("Arial", 14, "bold"), text_color="white").place_configure(x=40, y=110)

ctk.CTkLabel(ventana, text="Dirección:", font=("Arial", 15, "bold"), 
             fg_color="#99B4D1", text_color="black", bg_color="#99B4D1").place_configure(x=500, y=50)
ent_direccion = ctk.CTkEntry(ventana, font=("Arial", 15, "bold"), bg_color="#99B4D1", fg_color="white", text_color="black")
ent_direccion.place_configure(x=610, y=50, width=250)

fr_ingredientes = ctk.CTkFrame(ventana, border_color="white", border_width=2, fg_color="#99B4D1", bg_color="#99B4D1")
fr_ingredientes.place_configure(x=650, y=120, width=400, height=160)
ctk.CTkLabel(ventana, text="Ingredientes", fg_color="#99B4D1", bg_color="#99B4D1", text_color="white", 
             font=("Arial", 13, "bold", "italic")).place_configure(x=660, y=105, width=115)

jamon = ctk.CTkCheckBox(fr_ingredientes, text="Jamón $10", font=("Arial", 14, "bold"), text_color="white")
jamon.place_configure(x=40, y=30)
piña = ctk.CTkCheckBox(fr_ingredientes, text="Piña $10", font=("Arial", 14, "bold"), text_color="white")
piña.place_configure(x=40, y=70)
champiñones = ctk.CTkCheckBox(fr_ingredientes, text="Champiñones $10",  font=("Arial", 14, "bold"), text_color="white")
champiñones.place_configure(x=40, y=110)
ctk.CTkLabel(ventana, text="Teléfono:", font=("Arial", 15, "bold"), 
             fg_color="#99B4D1", text_color="black", bg_color="#99B4D1").place_configure(x=1150, y=50)
ent_telefono = ctk.CTkEntry(ventana, font=("Arial", 15, "bold"), bg_color="#99B4D1", fg_color="white", text_color="black")
ent_telefono.place_configure(x=1250, y=50, width=250)

ctk.CTkLabel(ventana, text="Num. de pizzas:", font=("Arial", 15, "bold"), 
             fg_color="#99B4D1", text_color="black", bg_color="#99B4D1").place_configure(x=1150, y=120)
ent_pizzas = ctk.CTkEntry(ventana, font=("Arial", 15, "bold"), bg_color="#99B4D1", fg_color="white", text_color="black")
ent_pizzas.place_configure(x=1150, y=160, width=150)

ctk.CTkButton(ventana, text="Agregar", font=("Arial", 12, "bold"), 
              fg_color="white", text_color="black", bg_color="#99B4D1", border_color="black", border_width=2, command=agregar).place_configure(x=1180, y=230, width=120)

#Cuadro
frame = ctk.CTkFrame(ventana)
frame.place_configure(x=40, y=350, width=800, height=300)
#Tabla
tabla = ttk.Treeview(frame)

#Scroll
barra = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=barra.set)

#Posición
tabla.pack(side="left", fill="both", expand=True)
barra.pack(side="right", fill="y")

#Columnas
tabla["columns"] = ("°", "Tamaño", "Ingredientes", "Num. Pizzas", "Sub Total")
tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("°", anchor=tk.CENTER, width=20)
tabla.column("Tamaño", anchor=tk.W, width=150)
tabla.column("Ingredientes", anchor=tk.W, width=150)
tabla.column("Num. Pizzas", anchor=tk.W, width=150)
tabla.column("Sub Total", anchor=tk.W, width=150)

tabla.heading("#0", text="")
tabla.heading("°", text="")
tabla.heading("Tamaño", text="Tamaño", anchor=tk.W)
tabla.heading("Ingredientes", text="Ingredientes", anchor=tk.W)
tabla.heading("Num. Pizzas", text="Num. Pizzas", anchor=tk.W)
tabla.heading("Sub Total", text="Sub Total", anchor=tk.W)

#Botones de registros
quitar =ctk.CTkButton(ventana, text="Quitar", fg_color="white", bg_color="#99B4D1", text_color="black", border_color="black", border_width=2, command=eliminar)
quitar.place_configure(x=180, y=700, width=120)
terminar_bot = ctk.CTkButton(ventana, text="Terminar", fg_color="white", bg_color="#99B4D1", text_color="black", border_color="black", border_width=2, command=terminar)
terminar_bot.place_configure(x=540, y=700, width=120)
#Cuadro de ventas
ctk.CTkLabel(ventana, fg_color="grey", text="").place_configure(x=910, y=335, width=680, height=450)
fr_ventas = ctk.CTkFrame(ventana, border_color="white", border_width=2, fg_color="grey", bg_color="grey")
fr_ventas.place_configure(x=935, y=360, width=630, height=340)
ctk.CTkLabel(ventana, text="Venta del día", fg_color="grey", bg_color="grey", text_color="white", font=("Arial", 15, "bold", "italic")).place_configure(x=955, y=345, width=130)
nom1 = ctk.CTkLabel(fr_ventas, text="", font=("Arial", 20, "bold"))
nom1.pack(pady=(20, 0))
nom2 = ctk.CTkLabel(fr_ventas, text="", font=("Arial", 20, "bold"))
nom2.pack(pady=(20, 0))
nom3 = ctk.CTkLabel(fr_ventas, text="", font=("Arial", 20, "bold"))
nom3.pack(pady=(20, 0))
nom4 = ctk.CTkLabel(fr_ventas, text="", font=("Arial", 20, "bold"))
nom4.pack(pady=(20, 0))
guardar_total()
ventas_tot = ctk.CTkLabel(fr_ventas, text=f"Ventas totales del día: ${ventas_tot_dia}", font=("Arial", 20, "bold"))
ventas_tot.pack(pady=(30, 0))
ctk.CTkLabel(ventana, text="Ventas totales por día", fg_color="#E1E1E1", bg_color="#E1E1E1", text_color="black", font=("Arial", 12, "bold")).place_configure(x=1000, y=720, width=500)

ventana.mainloop()