# importar libreria
import tkinter as tk
# inicializar ventana
ventana = tk.Tk()
# colocar titulo a ventana
ventana.title("Ejemplo tkinter")
# definir tamaño de ventana
ventana.geometry('450x700')
# bloquear cambio de tamano
ventana.resizable(width=0, height=0)
# agregar una etiqueta
lbl = tk.Label(ventana, text='Hola Mundo!')
lbl.grid(column=10, row=20)

tk.Button(ventana, text="Boton Ejemplo", width=0, anchor="c", font=("Arial", 12)).place(x=100, y=300)
ventana.mainloop()
