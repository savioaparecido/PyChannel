from tkinter import *
from Quadrada import *
from Trapezoidal import *
from Sobre import *

class Janela:

    def __init__(self, Tk):
        Tk.resizable(width=False, height=False)
        self.frame1 = Frame(Tk)
        self.frame2 = Frame(Tk)
        self.frame3 = Frame(Tk)
        self.frame4 = Frame(Tk)

        self.frame1.pack()
        self.frame2.pack(pady=5)
        self.frame3.pack(pady=5)
        self.frame4.pack(pady=5)

        self.lb1 = Label(self.frame1, text='CALCULADORA DE VAZÃO')
        self.lb1['fg'] = 'blue'
        self.lb1['font'] = ('Arial', 16)
        self.lb1['height'] = 3
        self.lb1.pack()

        self.lb2 = Label(self.frame1, text='Selecione o tipo de seção do canal: ')
        self.lb2['fg'] = 'black'
        self.lb2['font'] = ('Arial', 14, 'bold')
        self.lb2.pack()

        self.bt1 = Button(self.frame2, text='Quadrada', command=self.abrir_j1)
        self.bt1['bg'] = 'red'
        self.bt1['fg'] = 'white'
        self.bt1['font'] = ('Arial', 12)
        self.bt1.focus_force()
        self.bt1.pack()

        self.bt2 = Button(self.frame4, text='Trapezoidal com constante Z', command=self.abrir_j2)
        self.bt2['bg'] = 'red'
        self.bt2['fg'] = 'white'
        self.bt2['font'] = ('Arial', 12)
        self.bt2.pack()

        self.principal = Menu(raiz)
        self.principal.add_command(label='Sobre o Programa', command=self.sobre)
        raiz.configure(menu=self.principal)

    def abrir_j1(self):
        raiz = Tk()
        Janela1(raiz)
        raiz.title('Vazão Quadrada')
        raiz.mainloop()

    def abrir_j2(self):
        raiz = Tk()
        Janela2(raiz)
        raiz.title('Vazão Trapezoidal')
        raiz.mainloop()

    def sobre(self):
        raiz = Tk()
        Janela3(raiz)
        raiz.title('Sobre o Programa')
        raiz.mainloop()

raiz = Tk()
Janela(raiz)
raiz.title('PyChannel')
raiz.mainloop()
