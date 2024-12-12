import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter import *
from tienda.tienda import Tienda
from producto.producto import Producto

tienda = Tienda()
        
def obtenerR(event, ide, nombre, precio, cantidad, listbox):
    ide.delete(0, END)
    nombre.delete(0, END)
    precio.delete(0, END)
    cantidad.delete(0, END)
    
    renglon = listbox.selection()[0]
    seleccion = listbox.item(renglon)
    
    ide.insert(0, seleccion["values"][0])
    nombre.insert(0, seleccion["values"][1])
    precio.insert(0, seleccion["values"][2])
    cantidad.insert(0, seleccion["values"][3])
def ventana_agregar():
    root.withdraw()
    
    ventana = tk.Toplevel(root)
    ventana.title("Agregar Productos")
    ventana.geometry("850x300")
    label1 = tk.Label(ventana,text="Agregar Producuctos", fg="red",font=("Arial",28))
    label1.place(x=170,y=0)
    
    label_nombre = tk.Label(ventana, text="Nombre: ", font=("Arial", 12))
    label_nombre.place(x=50, y=100)
    label_precio = tk.Label(ventana, text="Precio: ", font=("Arial", 12))
    label_precio.place(x=50, y=150)
    label_cantidad = tk.Label(ventana, text="Cantidad: ", font=("Arial", 12))
    label_cantidad.place(x=50, y=200)
    
    entry_nombre = tk.Entry(ventana)
    entry_nombre.place(x=125, y=100)
    entry_precio = tk.Entry(ventana)
    entry_precio.place(x=125, y=150)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.place(x=125, y=200)
    
    nombre = entry_nombre
    precio = entry_precio
    cantidad = entry_cantidad
    
    tk.Button(ventana, text="Agregar Producto", command= lambda: Tienda.agregar_producto(nombre, cantidad, precio), height=5, width=15, font=("Arial", 12)).place(x=300, y=107)
    tk.Button(ventana, text="Regresar", command= lambda: regresar(ventana), height=5, width=15, font=("Arial", 12)).place(x=500,y=107)

def ventana_buscar():
    root.withdraw()
    
    buscarw = tk.Toplevel(root)
    buscarw.title("Buscar Productos")
    

def ventana_editar():
    root.withdraw()
    
    ventana = tk.Toplevel(root)
    ventana.title("Agregar Productos")
    ventana.geometry("1000x450")
    label1 = tk.Label(ventana,text="Editar Productos", fg="red",font=("Arial",28))
    label1.place(x=170,y=0)
    
    label_id = tk.Label(ventana, text="ID: ", font=("Arial", 12))
    label_id.place(x=50, y=50)
    label_nombre = tk.Label(ventana, text="Nombre: ", font=("Arial", 12))
    label_nombre.place(x=50, y=80)
    label_precio = tk.Label(ventana, text="Precio: ", font=("Arial", 12))
    label_precio.place(x=50, y=110)
    label_cantidad = tk.Label(ventana, text="Cantidad: ", font=("Arial", 12))
    label_cantidad.place(x=50, y=140)
    
    entry_id = tk.Entry(ventana)
    entry_id.place(x=125, y=50)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.place(x=125, y=80)
    entry_precio = tk.Entry(ventana)
    entry_precio.place(x=125, y=110)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.place(x=125, y=140)
    
    tk.Button(ventana, text="Editar Producto", command= lambda: Tienda.editar_producto(ide=entry_id, nombre=entry_nombre, precio=entry_precio, cantidad=entry_cantidad), height=5, width=15, font=("Arial", 12)).place(x=350, y=52)
    tk.Button(ventana, text="Regresar", command= lambda: regresar(ventana), height=5, width=15, font=("Arial", 12)).place(x=550,y=52)
    
    columnas = ("ID", "Nombre", "Precio", "Cantidad", "Valor Total")
    listbox = ttk.Treeview(ventana, columns=columnas, show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=200)
        
    for producto in Tienda.lista_productos:
        ide = producto.ide
        nombre = producto.nombre
        precio = producto.precio
        cantidad = producto.cantidad
        valor_total = float(precio) * int(cantidad)
        listbox.insert("", "end", values=(ide, nombre, precio, cantidad, valor_total))
    
    listbox.bind("<Double-Button-1>", lambda event: obtenerR(event=event, ide=entry_id, nombre=entry_nombre, precio=entry_precio, cantidad=entry_cantidad, listbox=listbox))
    

def ventana_mostrar():
    root.withdraw()
    
    ventana = tk.Toplevel(root)
    ventana.title("Agregar Productos")
    ventana.geometry("1000x350")
    label1 = tk.Label(ventana,text="Mostrar Producuctos", fg="red",font=("Arial",28))
    label1.place(x=170,y=30)
    
    columnas = ("ID", "Nombre", "Precio", "Cantidad", "Valor Total")
    listbox = ttk.Treeview(ventana, columns=columnas, show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=100)
        
    for producto in Tienda.lista_productos:
        ide = producto.ide
        nombre = producto.nombre
        precio = producto.precio
        cantidad = producto.cantidad
        valor_total = float(precio) * int(cantidad)
        listbox.insert("", "end", values=(ide, nombre, precio, cantidad, valor_total))

    tk.Button(ventana, text="Regresar", command= lambda: regresar(ventana), height=3, width=15, font=("Arial", 12)).place(x=550,y=25)
    

def regresar(ventana):
    ventana.destroy()
    root.deiconify()

root = tk.Tk()
root.title("Menú")
root.geometry("850x300")
label1 = tk.Label(root,text="Menú de Productos ", fg="red",font=("Arial",28))
label1.place(x=170,y=0)

    
global ide 
global nombre
global precio
global cantidad 
global listbox



tk.Button(root, text="Agregar Producto", command=ventana_agregar, height=5, width=15, font=("Arial", 12)).place(x=50, y=100)
tk.Button(root, text="Buscar Producto", command=ventana_buscar, height=5, width=15, font=("Arial", 12)).place(x=250, y=100)
tk.Button(root, text="Editar Productos", command=ventana_editar, height=5, width=15, font=("Arial", 12)).place(x=450, y=100)
tk.Button(root, text="Mostrar Productos", command=ventana_mostrar, height=5, width=15, font=("Arial", 12)).place(x=650, y=100)

root.mainloop()