from tkinter import *
from math import *

def btnclick(num):
    global operador
    operador = operador+str(num)
    input_text.set(operador)
    
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("Syntax Error")
    operador=""

def clear():
    global operador
    operador=("")
    input_text.set("0")
    
ventana =Tk()
ventana.title("Calculadora")
ventana.geometry("392x600")
ventana.configure(background="Skyblue4")

color_boton=("gray77")
color_boton1=("#99ccff")
color_boton2=("#ff6666")
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=10,y=60)

Button(ventana, text="%", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("%")).place(x=17, y=180)
Button(ventana, text="EXP", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("**")).place(x=107, y=180)
Button(ventana, text="Sqrt", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("sqrt(")).place(x=197, y=180)
Button(ventana, text="C", bg=color_boton2, width=ancho_boton, height=alto_boton, command=clear).place(x=287, y=180)
Button(ventana, text="(", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("(")).place(x=17, y=240)
Button(ventana, text=")", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(")")).place(x=107, y=240)
Button(ventana, text="pi", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("pi")).place(x=197, y=240)
Button(ventana, text="/", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("/")).place(x=287, y=240)
Button(ventana, text="7", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(7)).place(x=17, y=300)
Button(ventana, text="8", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(8)).place(x=107, y=300)
Button(ventana, text="9", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(9)).place(x=197, y=300)
Button(ventana, text="*", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("*")).place(x=287, y=300)
Button(ventana, text="4", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(4)).place(x=17, y=360)
Button(ventana, text="5", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(5)).place(x=107, y=360)
Button(ventana, text="6", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(6)).place(x=197, y=360)
Button(ventana, text="-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("-")).place(x=287, y=360)
Button(ventana, text="1", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(1)).place(x=17, y=420)
Button(ventana, text="2", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(2)).place(x=107, y=420)
Button(ventana, text="3", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(3)).place(x=197, y=420)
Button(ventana, text="+", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("+")).place(x=287, y=420)
Button(ventana, text="Log", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick("log(")).place(x=17, y=480)
Button(ventana, text="0", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(0)).place(x=107, y=480)
Button(ventana, text=".", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: btnclick(".")).place(x=197, y=480)
Button(ventana, text="=", bg=color_boton1, width=ancho_boton, height=alto_boton, command=resultado).place(x=287, y=480)

ventana.mainloop()
