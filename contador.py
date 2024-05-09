from tkinter import *
from tkinter import ttk
valor = 0

def click ():
  global valor
  valor = valor + 1
  texto1.configure(text=valor)

def click2 ():
  global valor
  valor = valor + 5
  texto1.configure(text=valor)
  
def click3 ():
  global valor
  valor = valor + 10
  texto1.configure(text=valor)

def c ():
  global valor
  valor = 0
  texto1.configure(text=valor)



janela = Tk ()
janela.title("botão adção de valores")

texto = Label(janela, text="click no botão")
texto.grid(column=1, row=0, padx=10, pady=10)

texto1 = Label(janela, text="0" )
texto1.grid(column=1, row=1, padx=10, pady=10)

botao1 = Button(janela, text='adcionar 1', command = click)
botao1.grid(column=0, row=2, padx=10, pady=10)

botao2 = Button(janela, text='adcionar 5', command = click2)
botao2.grid(column=1, row=2, padx=10, pady=10)

botao3 = Button(janela, text='adcionar 10', command = click3)
botao3.grid(column=2, row=2, padx=10, pady=10)

botao4 = Button(janela, text='limpar', command = c)
botao4.grid(column=1, row=3, padx=10, pady=10)

janela.mainloop()
