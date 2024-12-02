import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter import *
from producto.producto import calcular_valor_total, mostrar_detalles, agregar_producto

root = tk.Tk()
root.title("Menú")
root.geometry("800x500")
label1 = tk.Label(root,text="Menú de Productos ", fg="red",font=("Arial",28))
label1.place(x=170,y=0)

#nombre
label_nombre = tk.Label(root, text="Nombre:", font=("Arial", 12))
label_nombre.place(x=100, y=50)
entry_nombre = tk.Entry(root)
entry_nombre.place(x=220, y=50)

#precio
label_precio = tk.Label(root, text="Precio:", font=("Arial", 12))
label_precio.place(x=100, y=80)
entry_precio = tk.Entry(root)
entry_precio.place(x=220, y=80)

#cantidad
label_cantidad = tk.Label(root, text="Cantidad:", font=("Arial", 12))
label_cantidad.place(x=100, y=110)
entry_cantidad = tk.Entry(root)
entry_cantidad.place(x=220, y=110)

tk.Button(root, text="Agregar Producto", command=agregar_producto, height=5, width=15, font=("Arial", 12)).place(x=50, y=150)
tk.Button(root, text="Valor de Inventario", command=calcular_valor_total, height=5, width=15, font=("Arial", 12)).place(x=250, y=150)
tk.Button(root, text="Mostrar Detalles", command=mostrar_detalles, height=5, width=15, font=("Arial", 12)).place(x=450, y=150)

columnas = ("ID", "Nombre", "Cantidad", "Precio Total")
listbox = ttk.Treeview(root, columns=columnas, show="headings")
for col in columnas:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=1)
    listbox.place(x=0, y=300)
# mostrar()

root.mainloop()