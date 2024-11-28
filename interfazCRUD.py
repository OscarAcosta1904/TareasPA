import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *


def show():
    print("hola")

def mostrar():
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    micursos.execute("select * from usuarios")
    lista = micursos.fetchall()

    for i,(id,nombre,correo,contraseña) in enumerate(lista,start=1):
        listbox.insert("","end",values=(id,nombre,correo,contraseña))
        mysqlC.close()

def add():
    usuarioAdd = name.get()
    correoAdd = email.get()
    contraAdd = password.get()
    idAdd = identificador.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"insert into usuarios(id,nombre,correo,contraseña) values({idAdd},'{usuarioAdd}','{correoAdd}','{contraAdd}')")
        mysqlC.commit()
        name.delete(0,END)
        email.delete(0,END)
        password.delete(0,END)
        identificador.delete(0,END)
        messagebox.showinfo("informacion","usuario agregado")
        actualizar()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def actualizar():
    for i in listbox.get_children():
        listbox.delete(i)
    mostrar()

def edit():
    usuarioAdd = name.get()
    correoAdd = email.get()
    contraAdd = password.get()
    idAdd = identificador.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"UPDATE usuarios set nombre='{usuarioAdd}',correo='{correoAdd}',contraseña='{contraAdd}' where id={idAdd} ")
        mysqlC.commit()
        name.delete(0,END)
        email.delete(0,END)
        password.delete(0,END)
        identificador.delete(0,END)
        messagebox.showinfo("informacion","usuario editado")
        actualizar()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def delete():
    idAdd = identificador.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"DELETE FROM USUARIOS WHERE id={idAdd}")
        mysqlC.commit()
        name.delete(0,END)
        email.delete(0,END)
        password.delete(0,END)
        identificador.delete(0,END)
        messagebox.showinfo("informacion","usuario eliminado")
        actualizar()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def obtenerR(event):
    name.delete(0,END)
    email.delete(0,END)
    password.delete(0,END)
    identificador.delete(0,END)

    renglon = listbox.selection()[0]
    print(renglon)
    seleccion = listbox.set(renglon)
    print(seleccion)
    identificador.insert(0,seleccion["Id"])
    name.insert(0,seleccion["Nombre"])
    email.insert(0,seleccion["Correo"])
    password.insert(0,seleccion["Contraseña"])

root = tk.Tk()
root.geometry("800x500")

label1 = tk.Label(root,text="Registro de usuarios", fg="red",font=("Arial",28)).place(x=170,y=0)

global name
global email
global password
global identificador

labelid = tk.Label(root, text="ID", font=("Arial", 12))
labelid.place(x=100, y=50)

labelnombre = tk.Label(root, text="Nombre", font=("Arial", 12))
labelnombre.place(x=100, y=80)

labelcorreo = tk.Label(root, text="Correo", font=("Arial", 12))
labelcorreo.place(x=100, y=110)

labelcontrasena = tk.Label(root, text="Contraseña", font=("Arial", 12))
labelcontrasena.place(x=100, y=140)

identificador = tk.Entry(root)
identificador.place(x=270, y=50)

name = tk.Entry(root)
name.place(x=270, y=80)

email = tk.Entry(root)
email.place(x=270, y=110)

password = tk.Entry(root)
password.place(x=270, y=140)

tk.Button(root,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=170)
tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=170)
tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=170)

columnas = ("Id","Nombre","Correo","Contraseña")
listbox = ttk.Treeview(root,columns=columnas,show="headings")

for col in columnas:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=1)
    listbox.place(x=0, y=300)

mostrar()
listbox.bind("<Double-Button-1>",obtenerR)


root.mainloop()