from tkinter import *
#from Materiais import *

class Janela2:
    def __init__(self, Tk):
        Tk.resizable(width=False, height=False)
        self.tp1 = Toplevel(Tk)
        self.frame1 = Frame(Tk)
        self.frame2 = Frame(Tk)
        self.frame3 = Frame(Tk)
        self.frame4 = Frame(Tk)
        self.frame5 = Frame(Tk)
        self.frame6 = Frame(Tk)
        self.frame7 = Frame(Tk)

        self.frame1.pack(pady=5)
        self.frame2.pack(pady=5)
        self.frame3.pack(pady=5)
        self.frame4.pack(pady=5)
        self.frame5.pack(pady=5)
        self.frame6.pack(pady=5)
        self.frame7.pack(pady=5)

        self.fr1 = Frame(self.tp1)
        self.fr2 = Frame(self.tp1)
        self.fr3 = Frame(self.tp1)

        self.tx1 = Frame(self.tp1)
        self.tx2 = Frame(self.tp1)
        self.tx3 = Frame(self.tp1)
        self.tx4 = Frame(self.tp1)

        self.fr4 = Frame(self.tp1)
        self.fr5 = Frame(self.tp1)

        self.fr1.pack(pady=5)
        self.fr2.pack()
        self.fr3.pack(pady=5)

        self.tx1.pack()
        self.tx2.pack()
        self.tx3.pack()
        self.tx4.pack()

        self.fr6 = Frame(self.tp1)

        self.fr4.pack(pady=5)
        self.fr5.pack(pady=5)

        self.fr6.pack()

        self.lb6 = Label(self.frame1, text='Selecionar Coeficiente de Rugosidade de Manning : ')
        self.lb6['fg'] = 'black'
        self.lb6['font'] = ('Arial', 12)
        self.lb6.pack(side=LEFT)
        self.bt1 = Button(self.frame1, text='...', command=self.selecionar, width=3)
        self.bt1['bg'] = 'red'
        self.bt1['fg'] = 'white'
        self.bt1['font'] = ('Arial', 12)
        self.bt1.pack(side=LEFT)

        '''Recebe a altura da seção quadrada'''

        self.lb1 = Label(self.frame2, text='Digite a Altura da Seção (m): ')
        self.lb1['fg'] = 'black'
        self.lb1['font'] = ('Arial', 12)
        self.lb1.pack(side=LEFT)
        self.altura = Entry(self.frame2)
        self.altura['width'] = 5
        self.altura['font'] = ('Arial', 12)
        self.altura.pack(side=LEFT)

        '''Recebe a Declividade, em m/m'''

        self.lb2 = Label(self.frame3, text='Digite a Declividade, em m/m: ')
        self.lb2['fg'] = 'black'
        self.lb2['font'] = ('Arial', 12)
        self.lb2.pack(side=LEFT)
        self.declividade = Entry(self.frame3)
        self.declividade['width'] = 5
        self.declividade['font'] = ('Arial', 12)
        self.declividade.pack(side=LEFT)

        '''Recebe o valor da base maior da seção'''
        self.lb3 = Label(self.frame4, text='Digite a medida da Base Maior da Seção (m): ')
        self.lb3['fg'] = 'black'
        self.lb3['font'] = ('Arial', 12)
        self.lb3.pack(side=LEFT)
        self.base = Entry(self.frame4)
        self.base['width'] = 5
        self.base['font'] = ('Arial', 12)
        self.base.pack(side=LEFT)

        '''Recebe o valor da base menor da seção'''

        self.lb4 = Label(self.frame5, text='Digite a medida da Base Menor da Seção (m): ')
        self.lb4['fg'] = 'black'
        self.lb4['font'] = ('Arial', 12)
        self.lb4.pack(side=LEFT)
        self.menor = Entry(self.frame5)
        self.menor['width'] = 5
        self.menor['font'] = ('Arial', 12)
        self.menor.pack(side=LEFT)
        '''Botão de Calcular'''

        self.bt2 = Button(self.frame6, text='CALCULAR', command=self.calculo2)
        self.bt2['bg'] = 'red'
        self.bt2['fg'] = 'white'
        self.bt2['font'] = ('Arial', 12)
        self.bt2.focus_force()
        self.bt2.pack()
    def selecionar(self):
        self.dic_materiais = {'Alvenaria de pedra argamassada': [0.017, 0.020, 0.025, 0.030],
                                  'Alvenaria de pedra aparelhada': [0.013, 0.014, 0.015, 0.017],
                                  'Alvenaria de pedra seca': [0.025, 0.033, 0.033, 0.035],
                                  'Alvenaria de tijolos': [0.012, 0.013, 0.015, 0.017],
                                  'Canais abertos em rocha (irregular)': [0.035, 0.040, 0.045, 0.045],
                                  'Canais c/ fundo em terra e talude c/ pedras': [0.028, 0.030, 0.033, 0.035],
                                  'Canais c/ leito pedregoso e talude vegetado': [0.025, 0.030, 0.035, 0.040],
                                  'Canais com revestimento de concreto': [0.012, 0.014, 0.016, 0.018],
                                  'Canais de terra (retilíneos e uniformes)': [0.017, 0.020, 0.023, 0.025],
                                  'Canais dragados': [0.025, 0.028, 0.030, 0.033],
                                  'Condutos de barro (drenagem)': [0.011, 0.012, 0.014, 0.017],
                                  'Condutos de prancha de madeira aplainada': [0.010, 0.012, 0.013, 0.014],
                                  'Gabião': [0.022, 0.030, 0.035, 0.035],
                                  'Superfícies de argamassa de cimento': [0.011, 0.012, 0.013, 0.015],
                                  'Superfícies de cimento alisado': [0.010, 0.011, 0.012, 0.013],
                                  'Córregos e rios Limpos, retilíneos e uniformes': [0.025, 0.028, 0.030, 0.033],
                                  'Igual anterior porém c/ pedras e vegetação': [0.030, 0.033, 0.035, 0.040],
                                  'Com meandros, bancos e poços, limpos': [0.035, 0.040, 0.045, 0.050],
                                  'Margens espraiadas, pouca vegetação': [0.050, 0.060, 0.070, 0.080],
                                  'Margens espraiadas, muita vegetação': [0.075, 0.100, 0.125, 0.150]
                                  }



        self.lb = Label(self.fr1, text='Selecione o Material do Canal:')
        self.lb['font'] = ('Arial', 14, 'bold')
        self.lb.pack()

        self.scb1 = Scrollbar(self.fr2)
        self.scb1.pack(side=RIGHT, fill=Y)

        self.lbx1 = Listbox(self.fr2, yscrollcommand=self.scb1.set, width=50, selectmode=SINGLE)

        self.l_materiais = ['Alvenaria de pedra argamassada', 'Alvenaria de pedra aparelhada',
                                'Alvenaria de pedra seca',
                                'Alvenaria de tijolos', 'Canais abertos em rocha (irregular)',
                                'Canais c/ fundo em terra e talude c/ pedras',
                                'Canais c/ leito pedregoso e talude vegetado', 'Canais com revestimento de concreto',
                                'Canais de terra (retilíneos e uniformes)', 'Canais dragados',
                                'Condutos de barro (drenagem)',
                                'Condutos de prancha de madeira aplainada', 'Gabião',
                                'Superfícies de argamassa de cimento',
                                'Superfícies de cimento alisado', 'Córregos e rios Limpos, retilíneos e uniformes',
                                'Igual anterior porém c/ pedras e vegetação',
                                'Com meandros, bancos e poços, limpos', 'Margens espraiadas, pouca vegetação',
                                'Margens espraiadas, muita vegetação']

        for i in self.l_materiais:
            self.lbx1.insert(END, str(i))
        self.lbx1.pack(side=LEFT, fill=BOTH)
        self.scb1.config(command=self.lbx1.yview)

        self.bt1 = Button(self.fr3, text='Selecionar o Material', command=self.material)
        self.bt1.pack()

    def material(self):
        self.fr1.pack_forget()
        self.fr2.pack_forget()
        self.fr3.pack_forget()

        font = ('Arial', 12, 'bold')
        self.lb1 = Label(self.fr4, text='Condições do Material:')
        self.lb1['font'] = font
        self.lb1.pack()

        self.lb2 = Label(self.tx1, text='0 - Muito Boa')
        self.lb2['font'] = font
        self.lb2.pack()

        self.lb3 = Label(self.tx2, text='1 - Boa')
        self.lb3['font'] = font
        self.lb3.pack()

        self.lb4 = Label(self.tx3, text='2 - Regular')
        self.lb4['font'] = font
        self.lb4.pack()

        self.lb5 = Label(self.tx4, text='3 - Má')
        self.lb5['font'] = font
        self.lb5.pack()

        self.sc1 = Scale(self.fr5, from_=0, to=3, orient=HORIZONTAL)
        self.sc1.pack()

        self.bt2 = Button(self.fr5, text='Selecionar Condições do Material', command=self.condicao)
        self.bt2.pack()

    def condicao(self):
        self.selecao = self.lbx1.curselection()
        print(self.selecao)
        self.t = self.selecao[0]
        self.n_mat = self.l_materiais[self.t]
        self.nome = self.dic_materiais[self.n_mat]
        print(self.nome)
        self.coeficiente = self.nome[self.sc1.get()]
        print(self.coeficiente)

    def calculo2(self):
        self.n = float(self.coeficiente)
        try:
            self.h = float(self.altura.get())
            self.i = float(self.declividade.get())
            self.b = float(self.base.get())
            self.m = float(self.menor.get())
        except:
            self.h = 1
            self.i = 0
            self.b = 0
            self.m = 1
        self.dif = self.b-self.m
        self.z = self.dif/self.h
        self.a = (self.b + (self.z * self.h)) ** 5
        self.x = (self.i ** 3 / 2) * (self.h ** 5)
        self.y = (4 * (self.n**3) * (1 + (self.z ** 2)) * (self.h**2))
        self.w = (4 * (self.n ** 3) * self.b * ((1 + (self.z**2)) ** 1 / 2)*self.h)
        self.t = (self.n ** 3) * (self.b ** 2)
        self.q = ((self.a * self.x) / (self.y + self.w + self.t)) ** 1 / 3

        '''Escrevendo o Resultado'''
        self.lb5 = Label(self.frame7, text=f'A vazão desta seção quadrada (Q) é {self.q:.4f} m³/s')
        self.lb5['fg'] = 'black'
        self.lb5['font'] = ('Arial', 12, 'bold')
        self.lb5.pack()


