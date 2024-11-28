import tkinter as tk
from tkinter import messagebox
import mysql.connector

def verificar_usuario(correo, contrasena):
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
            SELECT * FROM usuarios3 WHERE correo = %s AND contraseña = %s
        ''', (correo, contrasena))
 
        usuario = cursor.fetchone()
 
        if usuario:
            messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
   
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()
            
def login():
    verificar_usuario()
    
    ventana_login.withdraw()
    
    menu_administrador = tk.Toplevel(ventana_login).title("Menú Administrador")

ventana_login = tk.Tk()
ventana_login.title("login")
ventana_login.geometry("200x200")

label1 = tk.Label(ventana_login, fg="red",text="-BIENVENIDO-", font=("Arial", 14)).place(x=35, y=10)

label_correo = tk.Label(ventana_login, text="Correo:", font=("Arial")).place(x=35, y=40)
entry_correo = tk.Entry(ventana_login).place(x=35, y=60)

label_contrasena = tk.Label(ventana_login, text="Contraseña:", font=("Arial")).place(x=35, y=90)
entry_contrasena = tk.Entry(ventana_login).place(x=35, y=110)


loginButton = tk.Button(ventana_login,text="login",command=login,height=2, width=6, font=("Arial",12)).place(x=60,y=140)

ventana_login.mainloop()