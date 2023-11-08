import tkinter as tk
import customtkinter as ctk
import turtle
import pathlib
from turtle import *
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry, CTkSlider, CTkComboBox
from tkinter import filedialog, PhotoImage, messagebox as mb

gramaticaX = ['+', 'Y', 'F', '-', 'X', 'F', 'X', '-', 'F', 'Y', '+']     # X -> + Y F - X F X - F Y +
gramaticaY = ['-', 'X', 'F', '+', 'Y', 'F', 'Y', '+', 'F', 'X', '-']     # Y -> - X F + Y F Y + F X -
cadenaNew = []
#cadenaR = []     
cadenaR = ['+', 'Y', 'F', '-', 'X', 'F', 'X', '-', 'F', 'Y', '+']

def configGrafico():
    colorBack = str(selectBackColor.get())
    colorLinea = str(selectLineaColor.get())
    tamañoLinea = str(sliderLinea.get())
    varGrado.set(int(inputGrado.get()))
    #bgcolor(str(colorBack))
    #pencolor(str(colorLinea))
    #pensize(int(tamañoLinea))
    #

def dibujar(cadena):
    tortuga = turtle.Screen()
    tortuga.title('Aguante la ACADEMIA')
    print("------En Metodo Dibujar")
    print(cadena)
    configGrafico()
    for d in range(0,len(cadena)):
        if cadena[d] == '+':
            left(int(varGrado.get()))
        elif cadena[d] == '-':
            right(int(varGrado.get()))
        elif cadena[d] == 'F':
            forward(100)
        elif cadena[d] == 'Y':
            continue
        elif cadena[d] == 'X':
            continue
    tortuga.update()
    tortuga.delay(2000)
    #mainloop()
    
def newNivel():
    print("------En Metodo newNivel")
    print(cadenaR)
    for i in range(0,len(cadenaR)):
        if cadenaR[i] == '+':
            cadenaNew.append('+')
        if cadenaR[i] == '-':
            cadenaNew.append('-')
        if cadenaR[i] == 'F':
            cadenaNew.append('F')
        if cadenaR[i] == 'Y':
            for y in range(0,len(gramaticaY)):
                cadenaNew.append(gramaticaY[y])
        if cadenaR[i] == 'X':
            for x in range(0,len(gramaticaX)):
                cadenaNew.append(gramaticaX[x])
    print(cadenaNew)

def remplazar():
    print("------En Metodo Remplazar")
    print(cadenaNew)
    print(cadenaR)
    # colocamos a cadena nueva en cadena resultante
    #global cadenaR
    cadenaR.clear()
    for i in range(0,len(cadenaNew)):
        if cadenaNew[i] == '+':
            cadenaR.append('+')
        if cadenaNew[i] == '-':
            cadenaR.append('-')
        if cadenaNew[i] == 'F':
            cadenaR.append('F')
        if cadenaNew[i] == 'Y':
            cadenaR.append('Y')
        if cadenaNew[i] == 'X':
            cadenaR.append('X') 
    #global cadenaNew
    cadenaNew.clear()

def ejecucion():       # depende de las iteraciones que nos de las hacemos
    numeroI = int(inputNivel.get())
    if numeroI == 0:
        dibujar(gramaticaX)
    if numeroI >= 1:
        #cadenaR = gramaticaX.copy()
        #cadenaR = list(gramaticaX)
        for i in range(numeroI):    
            newNivel()
            remplazar()
    dibujar(cadenaR)
    cadenaR.clear()

def sliderEvent(value):
    print(value)
    #labelTextSlider.configure(text=str(lambda: sliderLinea.get()))
    textSlider.set(f"{int(sliderLinea.get())}")

#Las ventana principal de la aplicacion y los Widgets
menu = ctk.CTk()
menu.title("Curva de Hilbert")
menu.geometry("290x340+534+200") #290x340
menu.config(bg='gray10')
menu.iconbitmap('logo_fi_J9A_icon.ico')
lineasInit = tk.StringVar(menu)

frame = ctk.CTkFrame(menu, fg_color='gray10')
frame.grid(column = 0, row = 0, sticky = 'nsew', padx=10, pady=15)
frame.columnconfigure([0,1,2], weight=1)
frame.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12], weight=1)

menu.columnconfigure(0, weight=1)
menu.rowconfigure(0, weight=1)

labelBackColor = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Color de fondo", fg_color='gray10')
labelBackColor.grid(columnspan=2, row=0)

optionBackColor = ctk.StringVar(menu, value="black")
selectBackColor = ctk.CTkComboBox(frame, values=["black", "green", "yellow"], variable=optionBackColor)
selectBackColor.grid(columnspan=2, row=1)

labelLineaColor = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Color de la linea", fg_color='gray10')
labelLineaColor.grid(columnspan=2, row=2)

optionLineaColor = ctk.StringVar(menu, value="white")
selectLineaColor = ctk.CTkComboBox(frame, values=["black", "white", "green", "yellow"], variable=optionLineaColor)
selectLineaColor.grid(columnspan=2, row=3)

labelAnchoLinea = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Ancho de linea", fg_color='gray10')
labelAnchoLinea.grid(columnspan=2, row=4)

textSlider = ctk.StringVar(value="")
sliderLinea = ctk.CTkSlider(frame, width=160, height=16, border_width=5.5, from_=1, to=10, command=sliderEvent) #falta poner el comando
sliderLinea.set(1)
sliderLinea.grid(columnspan=2, row=5, padx=4, pady=4)
labelTextSlider = ctk.CTkLabel(frame, textvariable= textSlider, font=('sans rerif', 12))    # text=str(lambda: sliderLinea.get())
labelTextSlider.grid(columnspan=2, column=0, row=5)

varGrado = ctk.StringVar(menu)
labelGrado = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Grado de angulo", fg_color='gray10')
labelGrado.grid(columnspan=2, row=6)

inputGrado = ctk.CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Nivel', border_color='deep sky blue', fg_color='gray10', width=220, height=40)
inputGrado.insert(0, "90")
inputGrado.grid(columnspan=2, row=7, padx=4, pady=4)

labelDerivacion = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Ingrese el nivel de derivacion", fg_color='gray10')
labelDerivacion.grid(columnspan=2, row=8)

inputNivel = ctk.CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Nivel', border_color='deep sky blue', fg_color='gray10', width=220, height=40)
inputNivel.insert(0, "0")
inputNivel.grid(columnspan=2, row=9, padx=4, pady=4)

botonDibujar = ctk.CTkButton(frame, font=('sans rerif', 12), text="Dibujar", border_color='deep sky blue', fg_color='gray10', hover_color='DeepSkyBlue3', border_width=2, command=ejecucion)
botonDibujar.place_configure(relx=0.5, rely=0.5, anchor=ctk.CENTER)
botonDibujar.grid(columnspan=2, row=10, padx=4, pady=4)

menu.mainloop()