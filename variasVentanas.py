import tkinter as tk

def abrir_segunda_ventana():
    ventana_principal.withdraw()
    
    ventana_sec = tk.Toplevel(ventana_principal)
    ventana_sec.title("Segunda Ventana")
    
    def regresar_a_principal():
        ventana_sec.destroy()  
        ventana_principal.deiconify()  

    boton_regresar = tk.Button(ventana_sec, text="Regresar a la ventana principal", command=regresar_a_principal)
    boton_regresar.pack(pady=20)

ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")

boton_abrir_segunda_ventana = tk.Button(ventana_principal, text="Abrir segunda ventana", command=abrir_segunda_ventana)
boton_abrir_segunda_ventana.pack(pady=20)

ventana_principal.mainloop()