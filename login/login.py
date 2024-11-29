import tkinter as tk
from tkinter import messagebox
import mysql.connector
from menu.menu_administrador import menu_administrador
from menu.menu_empleado import menu_empleados

def validar(usuario):
    if usuario[5] == "empleado":
        ventana_login.withdraw()
        menu_empleados()
        
    else:
        ventana_login.withdraw()
        print(":(")
        menu_administrador()

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
 
        cursor = conn.connect()
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios3 WHERE correo = %s AND contrasena = %s   
        ''', (correo, contrasena))
 
        usuario = cursor.fetchone()
 
        if usuario:
            messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
            validar(usuario=usuario)
                  
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

ventana_login.mainloop()