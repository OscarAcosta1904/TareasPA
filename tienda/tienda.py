from typing import List
from producto.producto import Producto
import tkinter as tk
from tkinter import messagebox

class Tienda:
    lista_productos: List [Producto] = []
    
    def __init__(self):
        jitomate = Producto(ide="123", nombre="Jitomate", precio="50", cantidad="6")
        lechuga = Producto(ide="1234", nombre="Lechuga", precio="40", cantidad="1")
        squirt = Producto(ide="1263", nombre="Squirt", precio="35", cantidad="8")
        chocolate = Producto(ide="12693", nombre="Chocolate", precio="16", cantidad="10")

        
        Tienda.lista_productos.append(jitomate)
        Tienda.lista_productos.append(lechuga)
        Tienda.lista_productos.append(squirt)
        Tienda.lista_productos.append(chocolate)
    
    def agregar_producto(nombre, precio, cantidad):
        try:
            nombreAdd = nombre.get().strip()
            precioAdd = precio.get().strip()
            cantidadAdd = cantidad.get().strip()

            if not nombreAdd or not precioAdd.isdigit() or not cantidadAdd.isdigit():
                raise MiError("Datos inválidos. Ingresa nombre y cantidades válidas.")

            ide = Producto.generar_id(nombreAdd)
            producto = Producto(ide=ide, nombre=nombreAdd, precio=precioAdd, cantidad=cantidadAdd)

            for p in Tienda.lista_productos:
                if p.nombre == producto.nombre:
                    raise MiError(f"El producto '{producto.nombre}' ya existe en la tienda.")

            Tienda.lista_productos.append(producto)
            messagebox.showinfo("Información", f"Producto '{producto.nombre}' agregado correctamente.")

        except MiError as e:
            messagebox.showerror("Error", e.mensaje)
                
class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)