from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("500x500")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan = 4, padx = 1, pady=1)

#Operaciones

text = ""
done = False
def add_text(texto):
    global text
    text = text + str(texto)
    pantalla.delete(0, "end")
    pantalla.insert(0, text)
    

def calcular():
    global text
    try:
        resultado = eval(text)
        pantalla.delete(0, "end")
        pantalla.insert(0, resultado)
        text = ""
        global done
        done = True


    except:
        pantalla.delete(0, "end")
        pantalla.insert(0, "Error")
        text = ""

def clear():
    if done:
        global text
        text = ""
        pantalla.delete(0, "end")
        pantalla.insert(0, "0")
    

# Configuración botones
boton_1 = Button(root, text="1", command= lambda: add_text(1) , width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command= lambda: add_text(2) , width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command= lambda: add_text(3), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4",command= lambda: add_text(4), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5",command= lambda: add_text(5), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6",command= lambda: add_text(6), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7",command= lambda: add_text(7), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8",command= lambda: add_text(8), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9",command= lambda: add_text(9), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_0 = Button(root, text="0",command= lambda: add_text(0), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=4, column=0, padx=1, pady=1)


boton_igual = Button(root, text="=",command= lambda: calcular(), width=9, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=1, columnspan=1, padx=1, pady=1)
boton_punto = Button(root, text=".",command= lambda: add_text("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+",command= lambda: add_text("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-",command= lambda: add_text("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",command= lambda: add_text("*"),  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", command= lambda: add_text("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()