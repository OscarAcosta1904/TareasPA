from typing import List
from producto.producto import Producto
import tkinter as tk
from tkinter import messagebox

class Tienda:
    lista_productos: List [Producto] = []
    
    def __init__(self):
        jitomate = Producto(ide="123", nombre="Jitomates", precio="50", cantidad="6")
        lechuga = Producto(ide="1234", nombre="Lechuga", precio="40", cantidad="1")
        squirt = Producto(ide="1263", nombre="Squirt", precio="35", cantidad="8")
        chocolate = Producto(ide="12693", nombre="Chocolate", precio="16", cantidad="10")

        
        Tienda.lista_productos.append(jitomate)
        Tienda.lista_productos.append(lechuga)
        Tienda.lista_productos.append(squirt)
        Tienda.lista_productos.append(chocolate)
        
    def actualizar_tabla(listbox):
        for item in listbox.get_children():
            listbox.delete(item)
        for producto in Tienda.lista_productos:
            listbox.insert("", "end", values=(producto.ide, producto.nombre, producto.precio, producto.cantidad))
    
    def agregar_producto(nombre, precio, cantidad):
        nombreAdd = nombre.get()
        precioAdd = precio.get()
        cantidadAdd = cantidad.get()
        
        ide = Producto.generar_id(nombreAdd)
        
        producto = Producto(ide=ide, nombre=nombreAdd, precio=precioAdd, cantidad=cantidadAdd)
        
        Tienda.lista_productos.append(producto) 
        
        nuevo_producto = producto
        
        for producto in Tienda.lista_productos:
            if nuevo_producto == producto:
                messagebox.showinfo("informacion", "Producto agregado correctamente")
                
    def editar_producto(ide, nombre, precio, cantidad):
        
        global listbox
        
        ideAdd = ide.get()
        nombreAdd = nombre.get()
        precioAdd = precio.get()
        cantidadAdd = cantidad.get()
        
        for producto in Tienda.lista_productos:
            if producto.ide == ideAdd:
             
                producto.nombre = nombreAdd
                producto.precio = precioAdd
                producto.cantidad = cantidadAdd
                messagebox.showinfo("Información", "Producto actualizado correctamente")
                Tienda.actualizar_tabla(listbox)
                return producto  
            
        messagebox.showerror("Error", "Producto no encontrado")
        return None
    
            
        
        


        
    
    

            
        
        
    

    