import tkinter as tk
from tp_P1 import cifrado_cesar, descifrado_cesar
from tp_P2 import cifrado_atbash

# --- Creamos la funcion para la ventana principal

def ventana_bienvenida():
    
    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.resizable(0, 0)
    ventana_bienvenida.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_bienvenida.iconbitmap('mensaje.ico')
    ventana_bienvenida.config(bg="light sky blue")

    mensaje_bienvenida = tk.Label(ventana_bienvenida, text="Bienvenido a la aplicación de mensajes \nsecretos del grupo BIT. Para continuar,\n presione Continuar, de lo contrario \ncierre la ventana" ,font=("Comic sans MS",14))
    mensaje_bienvenida.config(bg="light sky blue")
    mensaje_bienvenida.pack()

    integrantes_grupo = ['Eduardo Villagomez', 'Francisco Albinati', 'Cindy Calderón', 'Francisca Gaillard']

    lista_integrantes = tk.Label(ventana_bienvenida, text="Construída por:")
    lista_integrantes.config(bg="light sky blue")
    lista_integrantes.pack()

    for integrante in integrantes_grupo:
        label_integrante = tk.Label(ventana_bienvenida, text=integrante)
        label_integrante.config(bg="light sky blue")
        label_integrante.pack()

    boton_continuar = tk.Button(ventana_bienvenida, text="Continuar", command=ventana_mensajes)
    boton_continuar.config(bg="deep sky blue")
    boton_continuar.pack(padx=10,pady=15)

    ventana_bienvenida.mainloop()

def ventana_mensajes():
    fun_decifrar_cesar = lambda: label_resultado.config(text=descifrado_cesar(entrada_mensaje.get(),int(entrada_clave.get())))

    fun_cifrar_cesar = lambda: label_resultado.config(text=cifrado_cesar(entrada_mensaje.get(),int(entrada_clave.get())))
    
    fun_cifrado_atbash = lambda: label_resultado.config(text=cifrado_atbash(entrada_mensaje.get()))

    ventana_mensajes = tk.Tk()
    ventana_mensajes.resizable(0, 0)
    ventana_mensajes.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_mensajes.config(bg="navajo white")

    label_mensaje = tk.Label(ventana_mensajes, text="Ingrese el mensaje:")
    label_mensaje.config(bg="navajo white")
    label_mensaje.pack()

    entrada_mensaje = tk.Entry(ventana_mensajes)
    entrada_mensaje.pack()

    label_clave = tk.Label(ventana_mensajes, text="Ingrese la clave (solo para Cifrado César):")
    label_clave.config(bg="navajo white")
    label_clave.pack()

    entrada_clave = tk.Entry(ventana_mensajes)
    entrada_clave.pack()

    boton_cifrar_cesar = tk.Button(ventana_mensajes, text="Cifrar mensaje César", command=fun_cifrar_cesar)
    boton_cifrar_cesar.config(bg="orange")
    boton_cifrar_cesar.pack(padx=5,pady=10)

    boton_cifrar_atbash = tk.Button(ventana_mensajes, text="Cifrar mensaje Atbash", command=fun_cifrado_atbash)
    boton_cifrar_atbash.config(bg="orange")
    boton_cifrar_atbash.pack(padx=5,pady=5)

    boton_descifrar_cesar = tk.Button(ventana_mensajes, text="Descifrar mensaje César", command=fun_decifrar_cesar)
    boton_descifrar_cesar.config(bg="orange")
    boton_descifrar_cesar.pack(padx=5,pady=10)

    boton_descifrar_atbash = tk.Button(ventana_mensajes, text="Descifrar mensaje Atbash", command=fun_cifrado_atbash)
    boton_descifrar_atbash.config(bg="orange")
    boton_descifrar_atbash.pack(padx=5,pady=10)

    label_resultado = tk.Label(ventana_mensajes, text="",font=("Comic sans MS",12))
    label_resultado.config(bg="navajo white")
    label_resultado.pack()

    ventana_mensajes.mainloop()

ventana_bienvenida()