from tkinter import *

class Janela3:
    def __init__(self, Tk):
        Tk.resizable(width=False, height=False)
        self.frame1 = Frame(Tk)
        self.frame2 = Frame(Tk)
        self.frame1.pack()
        self.frame2.pack()


        self.label = Label(self.frame1, text='Calculadora de Vazão Versão 1.0', font = ('Arial', 16, 'bold'))
        font = ('Arial', 14)
        self.lb1 = Label(self.frame2, text = 'Este Programa foi criado baseado no Artigo: "SOBRE A IMPLEMENTAÇÃO NUMÉRICA DA FÓRMULA DE CHÉZY-MANNING" - Costa, Jordana Fernandes', font = font)
        self.lb2 = Label(self.frame2, text= 'Obrigado a todos que contribuíram para o Minicurso!!', font = font)
        self.lb3 = Label(self.frame2, text = 'Obrigado, também, aos organizadores do evento, por ceder o espaço!', font = font)
        self.lb4 = Label(self.frame2, text = 'e Obrigado aos nossos professores orientadores Arlam e Diogo!', font = font)
        self.lb5 = Label(self.frame2, text = 'Programa desenvolvido por Sávio e Iury', font = font)
        self.lb6 = Label(self.frame2, text='Obrigado a Jordana, pela contribuição com as fórmulas!', font=font)
        self.lb1.pack()
        self.lb2.pack()
        self.lb4.pack()
        self.lb3.pack()
        self.lb6.pack()
        self.lb5.pack()


