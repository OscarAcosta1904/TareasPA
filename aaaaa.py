import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *

def show():
    print("hola")

def mostrare():
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    micursos.execute("select * from libros")
    lista = micursos.fetchall()

    for i,(id,titulo,autor,editorial,ano_publicacion,precio) in enumerate(lista,start=1):
        listbox.insert("","end",values=(id,titulo,autor,editorial,ano_publicacion,precio))
        mysqlC.close()

def adde():
    tituloAdd = titulo.get()
    autorAdd = autor.get()
    editorialAdd = editorial.get()
    ano_publicacionAdd = ano_publicacion.get()
    idAdd = identificador.get()
    precioAdd = precio.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"insert into libros(id,titulo,autor,editorial,ano_publicacion,precio) values({idAdd},'{tituloAdd}','{autorAdd}','{editorialAdd}','{ano_publicacionAdd}','{precioAdd}')")
        mysqlC.commit()
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        ano_publicacion.delete(0,END)
        identificador.delete(0,END)
        precio.delete(0,END)
        messagebox.showinfo("informacion","libro agregado")
        actualizare()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def actualizare():
    for i in listbox.get_children():
        listbox.delete(i)
    mostrare()

def edite():
    tituloAdd = titulo.get()
    autorAdd = autor.get()
    editorialAdd = editorial.get()
    ano_publicacionAdd = ano_publicacion.get()
    idAdd = identificador.get()
    precioAdd = precio.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"UPDATE libros set titulo='{tituloAdd}',autor='{autorAdd}',editorial='{editorialAdd}',ano_publicacion='{ano_publicacionAdd}',precio='{precioAdd}' where id={idAdd} ")
        mysqlC.commit()
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        ano_publicacion.delete(0,END)
        identificador.delete(0,END)
        precio.delete(0,END)
        messagebox.showinfo("informacion","libro editado")
        actualizare()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def deletee():
    idAdd = identificador.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"DELETE FROM libros WHERE id={idAdd}")
        mysqlC.commit()
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        ano_publicacion.delete(0,END)
        identificador.delete(0,END)
        precio.delete(0,END)
        messagebox.showinfo("informacion","libro eliminado")
        actualizare()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def obtenerRe(event):
    titulo.delete(0,END)
    autor.delete(0,END)
    editorial.delete(0,END)
    ano_publicacion.delete(0,END)
    identificador.delete(0,END)
    precio.delete(0,END)

    renglon = listbox.selection()[0]
    print(renglon)
    seleccion = listbox.set(renglon)
    print(seleccion)
    identificador.insert(0,seleccion["Id"])
    titulo.insert(0,seleccion["Titulo"])
    autor.insert(0,seleccion["Autor"])
    editorial.insert(0,seleccion["Editorial"])
    ano_publicacion.insert(0,seleccion["Año de publicación"])
    precio.insert(0,seleccion["Precio"])

def filtro():
    def aplicar_filtro():
        filtro = entryFiltro.get()
        
        try:
            conn = mysql.connector.connect(
                host='localhost',      
                user='root',          
                password='',  
                database='biblioteca'    
            )
 
            # cursor = conn.connect()
            cursor = conn.cursor()
 
            cursor.execute('''
                SELECT * FROM libros WHERE ano_publicacion = %s 
            ''', (filtro,))
 
            lista = cursor.fetchall()
            listbox.delete(*listbox.get_children())
 
            if lista:
                for i,(id,titulo,autor,editorial,ano_publicacion,precio) in enumerate(lista,start=1):
                    listbox.insert("","end",values=(id,titulo,autor,editorial,ano_publicacion,precio))
                    conn.close()
                  
            else:
                messagebox.showerror("Error", "Libros no encontrados.")
                return
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión", f"Error: {err}")
   
        finally:
            if conn.is_connected():
                conn.close()
               
    ventana_filtro = tk.Toplevel(root)
    ventana_filtro.title("Filtro")
    ventana_filtro.geometry("1200x300")
        
    labelTitulo = tk.Label(ventana_filtro,text="Filtro de Libros", fg="red",font=("Arial",14))
    labelTitulo.place(x=50,y=0)
    labelFiltro = tk.Label(ventana_filtro, text="Fecha:", font=("Arial", 12))
    labelFiltro.place(x=5,y=50)
    entryFiltro = tk.Entry(ventana_filtro)
    entryFiltro.place(x=65,y=50)
        
    columnas = ("Id","Titulo", "Autor","Editorial","Año de publicación","Precio")
    listbox = ttk.Treeview(ventana_filtro,columns=columnas,show="headings")

    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=100)
        
    def regresar():
            ventana_filtro.destroy()
            root.deiconify()
            
    boton_filtrar = tk.Button(ventana_filtro, text="Filtrar", command=aplicar_filtro)
    boton_filtrar.place(x=200,y=30)
        
    boton_regresar = tk.Button(ventana_filtro, text="Regresar", command=regresar)
    boton_regresar.place(x=200,y=60)
    
root = tk.Tk()
root.title("Registro Libros")
root.geometry("1200x500")

label1 = tk.Label(root,text="Registro de libros", fg="red",font=("Arial",28)).place(x=170,y=0)

global titulo
global autor
global editorial
global ano_publicacion
global identificador
global precio
global listbox

labelid = tk.Label(root, text="ID", font=("Arial", 12))
labelid.place(x=100, y=50)

labelnombre = tk.Label(root, text="Título", font=("Arial", 12))
labelnombre.place(x=100, y=80)

labelapellido = tk.Label(root, text="Autor", font=("Arial", 12))
labelapellido.place(x=100, y=110)

labelcorreo = tk.Label(root, text="Editorial", font=("Arial", 12))
labelcorreo.place(x=100, y=140)

labelcontrasena = tk.Label(root, text="Año de publicación", font=("Arial", 12))
labelcontrasena.place(x=100, y=170)

labelrol = tk.Label(root, text="Precio", font=("Arial", 12))
labelrol.place(x=100, y=200)

identificador = tk.Entry(root)
identificador.place(x=270, y=50)

titulo = tk.Entry(root)
titulo.place(x=270, y=80)

autor = tk.Entry(root)
autor.place(x=270, y=110)

editorial = tk.Entry(root)
editorial.place(x=270, y=140)

ano_publicacion = tk.Entry(root)
ano_publicacion.place(x=270, y=170)

precio = tk.Entry(root)
precio.place(x=270, y=200)

tk.Button(root,text="Crear",command=adde, height=5, width=10, font=("Arial",12)).place(x=600,y=80)
tk.Button(root,text="Editar",command=edite, height=5, width=10, font=("Arial",12)).place(x=750,y=80)
tk.Button(root,text="Eliminar",command=deletee, height=5, width=10, font=("Arial",12)).place(x=900,y=80)
tk.Button(root,text="Filtrar",command=filtro, height=5, width=10, font=("Arial",12)).place(x=1050,y=80)

columnas = ("Id","Titulo", "Autor","Editorial","Año de publicación","Precio")
listbox = ttk.Treeview(root,columns=columnas,show="headings")

for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=300)

mostrare()
listbox.bind("<Double-Button-1>",obtenerRe)

root.mainloop()