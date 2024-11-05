import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es {suma}")
        
    except ValueError:
        messagebox.showinfo("Error", "Por favor, ingresa número válidos")
        
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es {resta}")
        
    except ValueError:
        messagebox.showinfo("Error", "Por favor, ingresa número válidos")
        
def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        mul = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicación es {mul}")
        
    except ValueError:
        messagebox.showinfo("Error", "Por favor, ingresa número válidos")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        div = num1 / num2
        messagebox.showinfo("Resultado", f"La división es {div}")
        
    except ValueError:
        messagebox.showinfo("Error", "Por favor, ingresa número válidos")
        
    except ZeroDivisionError:
        messagebox.showinfo("Error", "Por favor, ingresa número válidos")
        
ventana = tk.Tk()

ventana.title("Calculadora")
ventana.geometry("300x200")

label_num1 = tk.Label(ventana, text="Número 1.")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)

label_num2 = tk.Label(ventana, text="Número 2.")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)        

boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_sumar.pack(pady=20)

boton_restar = tk.Button(ventana, text="-", command=restar)
boton_restar.pack(pady=20)

boton_multiplicar = tk.Button(ventana, text="*", command=multiplicar)
boton_multiplicar.pack(pady=20)

boton_dividir = tk.Button(ventana, text="/", command=dividir)
boton_dividir.pack(pady=20)

ventana.mainloop()