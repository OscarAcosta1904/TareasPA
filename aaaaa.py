import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *

def verificar_usuario():
    correo = entry_correo.get()
    contrasena = entry_contrasena.get() 
    
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='biblioteca'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios3 WHERE correo = %s AND contrasena = %s
        ''', (correo, contrasena))
 
        usuario = cursor.fetchone()
 
        if usuario:
            hola = "SELECT rol FROM usuarios3 WHERE correo = %s"
            cursor.execute(hola, (correo,))
            resultado = cursor.fetchone()
            rol = usuario[5]
            if rol.lower() == "administrador":
                messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
                ventana_login.withdraw()
                menu_administrador()
                
            else:
                 messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
                 ventana_login.withdraw()
                 menu_empleados()
                  
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
            return
        
   
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()
            
ventana_login = tk.Tk()
ventana_login.title("login")
ventana_login.geometry("200x200")

label1 = tk.Label(ventana_login, fg="red",text="-BIENVENIDO-", font=("Arial", 14)).place(x=35, y=10)

label_correo = tk.Label(ventana_login, text="Correo:", font=("Arial")).place(x=35, y=40)
entry_correo = tk.Entry(ventana_login)
entry_correo.place(x=35, y=60)

label_contrasena = tk.Label(ventana_login, text="Contraseña:", font=("Arial")).place(x=35, y=90)
entry_contrasena = tk.Entry(ventana_login,show="*")
entry_contrasena.place(x=35, y=110)


loginButton = tk.Button(ventana_login,text="login",command=verificar_usuario,height=2, width=6, font=("Arial",12)).place(x=60,y=140)

## ADMINISTRADOR ##

def show():
    print("hola")

def mostrar():
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    micursos.execute("select * from usuarios3")
    lista = micursos.fetchall()

    for i,(id,nombre, apellido, correo, contrasena, rol) in enumerate(lista,start=1):
        Listbox.insert("","end",values=(id,nombre, apellido, correo, contrasena, rol))
        mysqlC.close()

def add():
    nameAdd = name.get()
    surnameAdd = surname.get()
    correoAdd = email.get()
    contraAdd = password.get()
    idAdd = identificador.get()
    rolAdd = rol.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    
    if rolAdd.strip().lower() not in ["administrador", "empleado"]:
        messagebox.showerror("informacion", "Rol no válido")
        return
  

    else:
        try:
            micursos.execute(f"insert into usuarios3(id,nombre,apellido,correo,contrasena,rol) values({idAdd},'{nameAdd}','{surnameAdd}','{correoAdd}','{contraAdd}','{rolAdd}')")
            mysqlC.commit()
            name.delete(0,END)
            surname.delete(0,END)
            email.delete(0,END)
            password.delete(0,END)
            identificador.delete(0,END)
            rol.delete(0,END)
            messagebox.showinfo("informacion","usuario agregado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

def actualizar():
    for i in Listbox.get_children():
        Listbox.delete(i)
    mostrar()

def edit():
    nameAdd = name.get()
    surnameAdd = surname.get()
    correoAdd = email.get()
    contraAdd = password.get()
    idAdd = identificador.get()
    rolAdd = rol.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"UPDATE usuarios3 set nombre='{nameAdd}',apellido='{surnameAdd}',correo='{correoAdd}',contrasena='{contraAdd}',rol='{rolAdd}' where id={idAdd} ")
        mysqlC.commit()
        name.delete(0,END)
        surname.delete(0,END)
        email.delete(0,END)
        password.delete(0,END)
        identificador.delete(0,END)
        rol.delete(0,END)
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
        micursos.execute(f"DELETE FROM USUARIOS3 WHERE id={idAdd}")
        mysqlC.commit()
        name.delete(0,END)
        surname.delete(0,END)
        email.delete(0,END)
        password.delete(0,END)
        identificador.delete(0,END)
        rol.delete(0,END)
        messagebox.showinfo("informacion","usuario eliminado")
        actualizar()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def obtenerR(event):
    name.delete(0,END)
    surname.delete(0,END)
    email.delete(0,END)
    password.delete(0,END)
    identificador.delete(0,END)
    rol.delete(0,END)

    renglon = Listbox.selection()[0]
    print(renglon)
    seleccion = Listbox.set(renglon)
    print(seleccion)
    identificador.insert(0,seleccion["Id"])
    name.insert(0,seleccion["Nombre"])
    surname.insert(0,seleccion["Apellido"])
    email.insert(0,seleccion["Correo"])
    password.insert(0,seleccion["Contraseña"])
    rol.insert(0,seleccion["Rol"])
def menu_administrador():
    root = tk.Toplevel()
    root.geometry("1200x500")
    label1 = tk.Label(root,text="Registro de empleados", fg="red",font=("Arial",28))
    label1.place(x=170,y=0)
    global name
    global surname
    global email
    global password
    global identificador
    global rol
    labelid = tk.Label(root, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    labelnombre = tk.Label(root, text="Nombre", font=("Arial", 12))
    labelnombre.place(x=100, y=80)
    labelapellido = tk.Label(root, text="Apellido", font=("Arial", 12))
    labelapellido.place(x=100, y=110)
    labelcorreo = tk.Label(root, text="Correo", font=("Arial", 12))
    labelcorreo.place(x=100, y=140)
    labelcontrasena = tk.Label(root, text="Contraseña", font=("Arial", 12))
    labelcontrasena.place(x=100, y=170)
    labelrol = tk.Label(root, text="Rol", font=("Arial", 12))
    labelrol.place(x=100, y=200)
    identificador = tk.Entry(root)
    identificador.place(x=270, y=50)
    name = tk.Entry(root)
    name.place(x=270, y=80)
    surname = tk.Entry(root)
    surname.place(x=270, y=110)
    email = tk.Entry(root)
    email.place(x=270, y=140)
    password = tk.Entry(root)
    password.place(x=270, y=170)
    rol = tk.Entry(root)
    rol.place(x=270, y=200)
    tk.Button(root,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=600,y=80)
    tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=750,y=80)
    tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=900,y=80)
    columnas = ("Id","Nombre", "Apellido","Correo","Contraseña","Rol")
    Listbox = ttk.Treeview(root,columns=columnas,show="headings")
    for col in columnas:
        Listbox.heading(col, text=col)
        Listbox.grid(row=1, column=0, columnspan=1)
        Listbox.place(x=0, y=300)
    mostrar()
    Listbox.bind("<Double-Button-1>",obtenerR)
    
## EMPLEADO ##

def mostrare():
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
    micursos=mysqlC.cursor()
    micursos.execute("select * from libros")
    lista = micursos.fetchall()

    for i,(id,titulo,autor,editorial,ano_publicacion,precio) in enumerate(lista,start=1):
        Listbox.insert("","end",values=(id,titulo,autor,editorial,ano_publicacion,precio))
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
    for i in Listbox.get_children():
        Listbox.delete(i)
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

    renglon = Listbox.selection()[0]
    print(renglon)
    seleccion = Listbox.set(renglon)
    print(seleccion)
    identificador.insert(0,seleccion["Id"])
    titulo.insert(0,seleccion["Título"])
    autor.insert(0,seleccion["Autor"])
    editorial.insert(0,seleccion["Editorial"])
    ano_publicacion.insert(0,seleccion["Año de publicación"])
    precio.insert(0,seleccion["Precio"])

def menu_empleados():
    root = tk.Toplevel()
    root.geometry("1200x500")

    label1 = tk.Label(root,text="Registro de libros", fg="red",font=("Arial",28)).place(x=170,y=0)

    global titulo
    global autor
    global editorial
    global ano_publicacion
    global identificador
    global precio

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

    columnas = ("Id","Titulo", "Autor","Editorial","Año de publicación","Precio")
    Listbox = ttk.Treeview(root,columns=columnas,show="headings")

    for col in columnas:
            Listbox.heading(col, text=col)
            Listbox.grid(row=1, column=0, columnspan=1)
            Listbox.place(x=0, y=300)

    mostrare()
    Listbox.bind("<Double-Button-1>",obtenerRe)

ventana_login.mainloop()