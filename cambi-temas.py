from ttkbootstrap import Window, ttk
from tkinter import StringVar

# Lista de temas disponibles
temas = ['flatly', 'darkly', 'minty', 'superhero', 'solar']

# Función que actualiza el tema al seleccionar una opción
def cambiar_tema(event=None):
    nuevo_tema = variable_tema.get()
    app.style.theme_use(nuevo_tema)

# Crear la ventana con tema inicial
app = Window(themename='flatly')
app.title("Selector de Tema Bootstrap")
app.geometry("400x200")

# Select para elegir el tema
variable_tema = StringVar(value=temas[0])
select = ttk.Combobox(app, textvariable=variable_tema, values=temas, state="readonly", bootstyle="info")
select.pack(pady=20)
select.bind("<<ComboboxSelected>>", cambiar_tema)

# Etiqueta para mostrar algo en pantalla
etiqueta = ttk.Label(app, text="Cambia el tema desde el selector", font=("Helvetica", 14))
etiqueta.pack(pady=10)

app.mainloop()