import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter import *
from tienda.tienda import agregar_producto
from tienda.tienda import Tienda

def ventana_agregar():
    root.withdraw()
    
    agregarw = tk.Toplevel(root)
    agregarw.title("Agregar Productos")
    agregarw.geometry("850x300")
    label1 = tk.Label(agregarw,text="Agregar Producuctos", fg="red",font=("Arial",28))
    label1.place(x=170,y=0)
    
    label_nombre = tk.Label(agregarw, text="Nombre: ", font=("Arial", 12))
    label_nombre.place(x=50, y=100)
    label_precio = tk.Label(agregarw, text="Precio: ", font=("Arial", 12))
    label_precio.place(x=50, y=150)
    label_cantidad = tk.Label(agregarw, text="Cantidad: ", font=("Arial", 12))
    label_cantidad.place(x=50, y=200)
    
    entry_nombre = tk.Entry(agregarw)
    entry_nombre.place(x=125, y=100)
    entry_precio = tk.Entry(agregarw)
    entry_precio.place(x=125, y=150)
    entry_cantidad = tk.Entry(agregarw)
    entry_cantidad.place(x=125, y=200)
    
    tk.Button(agregarw, text="Agregar Producto", command=agregar_producto, height=5, width=15, font=("Arial", 12)).place(x=300, y=107)
    tk.Button(agregarw, text="Regresar", command= lambda: regresar(agregarw), height=5, width=15, font=("Arial", 12)).place(x=500,y=107)
    
    

def ventana_buscar():
    root.withdraw()
    
    buscarw = tk.Toplevel(root)
    buscarw.title("Buscar Productos")
    

def ventana_editar():
    root.withdraw()
    
    editarw = tk.Toplevel(root)
    editarw.title("Agregar Productos")
    editarw.geometry("850x300")
    label1 = tk.Label(editarw,text="Editar Producuctos", fg="red",font=("Arial",28))
    label1.place(x=170,y=0)
    

def ventana_mostrar():
    root.withdraw()
    
    mostrarw = tk.Toplevel(root)
    mostrarw.title("Agregar Productos")
    mostrarw.geometry("1000x350")
    label1 = tk.Label(mostrarw,text="Mostrar Producuctos", fg="red",font=("Arial",28))
    label1.place(x=170,y=30)
    
    columnas = ("ID", "Nombre", "Precio", "Cantidad", "Valor Total")
    listbox = ttk.Treeview(mostrarw, columns=columnas, show="headings")
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=100)
        
    scrollbar = tk.Scrollbar(mostrarw, orient="vertical", command=listbox.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    listbox.config(yscrollcommand=scrollbar.set)
    
    # for i, producto in enumerate(tienda.lista_productos):
    #     valor_total = float(producto["precio"]) * int(producto["cantidad"])
    #     listbox.insert("", "end", iid=i, values=(i, producto["nombre"], producto["precio"], producto["cantidad"], valor_total))
        
    # for i, producto in enumerate(Tienda.lista_productos, start=1):
    #     valor_total = float(producto["precio"]) * int(producto["cantidad"])
    #     listbox.insert("", "end", id=i, values=(i, producto["nombre"], producto["precio"], producto["cantidad"], valor_total))
        
    for producto, (id, nombre, precio, cantidad) in Tienda.lista_productos:
        valor_total = float(producto["precio"]) * int(producto["cantidad"])
        listbox.insert("", "end", values=(id, nombre, precio, cantidad, valor_total))
        
    
    

        
    tk.Button(mostrarw, text="Regresar", command= lambda: regresar(mostrarw), height=3, width=15, font=("Arial", 12)).place(x=550,y=25)
    

def regresar(ventana):
    ventana.destroy()
    root.deiconify()

root = tk.Tk()
root.title("Menú")
root.geometry("850x300")
label1 = tk.Label(root,text="Menú de Productos ", fg="red",font=("Arial",28))
label1.place(x=170,y=0)


tk.Button(root, text="Agregar Producto", command=ventana_agregar, height=5, width=15, font=("Arial", 12)).place(x=50, y=100)
tk.Button(root, text="Buscar Producto", command=ventana_buscar, height=5, width=15, font=("Arial", 12)).place(x=250, y=100)
tk.Button(root, text="Editar Productos", command=ventana_editar, height=5, width=15, font=("Arial", 12)).place(x=450, y=100)
tk.Button(root, text="Mostrar Productos", command=ventana_mostrar, height=5, width=15, font=("Arial", 12)).place(x=650, y=100)

root.mainloop()