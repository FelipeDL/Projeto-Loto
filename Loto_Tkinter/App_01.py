from tkinter import *
from tkinter import ttk
import sqlite3
import random
from math import factorial

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser




root =Tk()

class Relatorios():
    def printConcurso(self):
        webbrowser.open("concurso.pdf")
    def geraRelatConcurso(self):
        num = str(random.randrange(0,10000))

        self.c = canvas.Canvas('Concurso'+ num + '.pdf')

        self.concursoRel = self.concurso_entry.get()
        self.bola1Rel = self.bola1_entry.get()
        self.bola2Rel = self.bola2_entry.get()
        self.bola3Rel = self.bola3_entry.get()
        self.bola4Rel = self.bola4_entry.get()
        self.bola5Rel = self.bola5_entry.get()
        self.bola6Rel = self.bola6_entry.get()
        self.bola7Rel = self.bola7_entry.get()
        self.bola8Rel = self.bola8_entry.get()
        self.bola9Rel = self.bola9_entry.get()
        self.bola10Rel = self.bola10_entry.get()
        self.bola11Rel = self.bola11_entry.get()
        self.bola12Rel = self.bola12_entry.get()
        self.bola13Rel = self.bola13_entry.get()
        self.bola14Rel = self.bola14_entry.get()
        self.bola15Rel = self.bola15_entry.get()

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(200, 790, 'Concursos Apurados')
        self.c.drawString(10, 700, 'Concurso: ')
        self.c.drawString(75, 700, self.concursoRel)

        self.c.setFont("Helvetica-Bold", 11)
        self.c.drawString(85, 700, ' - ')
        self.c.drawString(95, 700, self.bola1Rel)
        self.c.drawString(120, 700, self.bola2Rel)
        self.c.drawString(145, 700, self.bola3Rel)
        self.c.drawString(170, 700, self.bola4Rel)
        self.c.drawString(195, 700, self.bola5Rel)
        self.c.drawString(220, 700, self.bola6Rel)
        self.c.drawString(245, 700, self.bola7Rel)
        self.c.drawString(270, 700, self.bola8Rel)
        self.c.drawString(295, 700, self.bola9Rel)
        self.c.drawString(320, 700, self.bola10Rel)
        self.c.drawString(345, 700, self.bola11Rel)
        self.c.drawString(370, 700, self.bola12Rel)
        self.c.drawString(395, 700, self.bola13Rel)
        self.c.drawString(420, 700, self.bola14Rel)
        self.c.drawString(445, 700, self.bola15Rel)





        self.c.showPage()
        self.c.save()


class Funcoes():
    def limpa_tela(self):
        self.concurso_entry.delete(0, END)
        self.bola1_entry.delete(0, END)
        self.bola2_entry.delete(0, END)
        self.bola3_entry.delete(0, END)
        self.bola4_entry.delete(0, END)
        self.bola5_entry.delete(0, END)
        self.bola6_entry.delete(0, END)
        self.bola7_entry.delete(0, END)
        self.bola8_entry.delete(0, END)
        self.bola9_entry.delete(0, END)
        self.bola10_entry.delete(0, END)
        self.bola11_entry.delete(0, END)
        self.bola12_entry.delete(0, END)
        self.bola13_entry.delete(0, END)
        self.bola14_entry.delete(0, END)
        self.bola15_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("resultLoto2.db")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def variaveis(self):
        self.concurso = self.concurso_entry.get()
        self.bola1 = self.bola1_entry.get()
        self.bola2 = self.bola2_entry.get()
        self.bola3 = self.bola3_entry.get()
        self.bola4 = self.bola4_entry.get()
        self.bola5 = self.bola5_entry.get()
        self.bola6 = self.bola6_entry.get()
        self.bola7 = self.bola7_entry.get()
        self.bola8 = self.bola8_entry.get()
        self.bola9 = self.bola9_entry.get()
        self.bola10 = self.bola10_entry.get()
        self.bola11 = self.bola11_entry.get()
        self.bola12 = self.bola12_entry.get()
        self.bola13 = self.bola13_entry.get()
        self.bola14 = self.bola14_entry.get()
        self.bola15 = self.bola15_entry.get()
    def addConcurso(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO tb_concursos
         (ID_CONCURSO, TBOLA1, TBOLA2, TBOLA3, TBOLA4,
         TBOLA5, TBOLA6, TBOLA7, TBOLA8, TBOLA9, TBOLA10,
         TBOLA11, TBOLA12, TBOLA13, TBOLA14, TBOLA15)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (self.concurso, self.bola1, self.bola2, self.bola3,
         self.bola4, self.bola5, self.bola6, self.bola7, self.bola8,
         self.bola9, self.bola10, self.bola11, self.bola12, self.bola13,
         self.bola14, self.bola15))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaBanco.delete(*self.listaBanco.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT ID_CONCURSO,
        TBOLA1, TBOLA2, TBOLA3, TBOLA4, TBOLA5, TBOLA6, TBOLA7,
        TBOLA8,TBOLA9,TBOLA10,TBOLA11,TBOLA12,TBOLA13,TBOLA14,TBOLA15
        from tb_concursos; """)
        for i in lista:
            self.listaBanco.insert("", END, values=i)
        self.desconecta_bd()
    def doisClicks(self,event):
        self.limpa_tela()
        self.listaBanco.selection()

        for n in self.listaBanco.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = self.listaBanco.item(n, 'values')
            self.concurso_entry.insert(END, col1)
            self.bola1_entry.insert(END,col2)
            self.bola2_entry.insert(END, col3)
            self.bola3_entry.insert(END, col4)
            self.bola4_entry.insert(END, col5)
            self.bola5_entry.insert(END, col6)
            self.bola6_entry.insert(END, col7)
            self.bola7_entry.insert(END, col8)
            self.bola8_entry.insert(END, col9)
            self.bola9_entry.insert(END, col10)
            self.bola10_entry.insert(END, col11)
            self.bola11_entry.insert(END, col12)
            self.bola12_entry.insert(END, col13)
            self.bola13_entry.insert(END, col14)
            self.bola14_entry.insert(END, col15)
            self.bola15_entry.insert(END, col16)
    def deleta_Concurso(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM tb_concursos WHERE ID_CONCURSO = ? """, (self.concurso,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def busca_Concurso(self):
        self.conecta_bd()
        self.listaBanco.delete(*self.listaBanco.get_children())
        self.concurso_entry.insert(END, '%')
        nome = self.concurso_entry.get()
        self.cursor.execute("""
        SELECT ID_CONCURSO, TBOLA1, TBOLA2, TBOLA3, TBOLA4, TBOLA5,
        TBOLA6,TBOLA7,TBOLA8,TBOLA9,TBOLA10,TBOLA11,TBOLA12,TBOLA13,
        TBOLA14,TBOLA15 FROM tb_concursos WHERE ID_CONCURSO LIKE '%s' """ % nome)

        buscaconcurso = self.cursor.fetchall()
        for i in buscaconcurso:
            self.listaBanco.insert("", END, values=i)
            self.limpa_tela()

        self.desconecta_bd()
    def calc(self):

        num1 = int(self.tb1.get())
        res = int(3268760/(num1))
        self.final.set("A sua probabilidade é 1 em " + str(res))



class Application(Funcoes,Relatorios):
    def __init__(self):
        self.root =root
        self.Tela()
        self.frameTela()
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()

        root.mainloop()
    def Tela(self):
        self.root.title("Lotofácil sendo Fácil")
        self.root.configure(bg='#000000')
        self.root.geometry(newGeometry="900x700")
        self.root.resizable(False, False)
        self.root.state("zoomed")
        #self.root.maxsize(width=1500, height=1500)
        #self.root.minsize(width=300, height=200)
    def frameTela(self):
        self.frame_1 = Frame(self.root,bd=4, bg='#00CED1', highlightbackground='#363636', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth=0.96,relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='#00CED1', highlightbackground='#363636', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba3 = Frame(self.abas)

        self.aba1.configure(bg="#40E0D0")
        self.aba2.configure(bg="#40E0D0")
        self.aba3.configure(bg="#40E0D0")

        self.abas.add(self.aba1, text = "Gerenciar BD")
        self.abas.add(self.aba2, text="Probabilidades")
        self.abas.add(self.aba3, text="Sortear")

        self.abas.place(relx=0.010, rely=0.01, relwidth=0.98, relheight=0.98)

        self.bt_limpar = Button(self.aba1, text="Limpar",bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'),command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Buscar
        self.bt_buscar = Button(self.aba1, text="Buscar",bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'), command= self.busca_Concurso)
        self.bt_buscar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Novo Concurso
        self.bt_novo = Button(self.aba1, text="Inserir",bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'),command=self.addConcurso)
        self.bt_novo.place(relx=0.44, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Deletar Registro incorreto
        self.bt_deletar = Button(self.aba1, text="Deletar", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'),command=self.deleta_Concurso)
        self.bt_deletar.place(relx=0.56, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Gerar Relatório
        self.bt_relatorio = Button(self.aba1, text="Gerar Relatório",bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'),command=self.geraRelatConcurso)
        self.bt_relatorio.place(relx=0.68, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação da label e entrada de novo registro
        self.lb_concurso = Label(self.aba1, text = "Inserir nº Concurso",bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_concurso.place(relx=0.034,rely=0.19)

        self.concurso_entry = Entry(self.aba1)
        self.concurso_entry.place(relx=0.03, rely=0.25, relwidth=0.1)

        # Criação da label das bolas
        self.lb_bola1 = Label(self.aba1, text="Bola 01",bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola1.place(relx=0.137, rely=0.39)

        self.bola1_entry = Entry(self.aba1)
        self.bola1_entry.place(relx=0.12, rely=0.45, relwidth=0.07)

        self.lb_bola2 = Label(self.aba1, text="Bola 02", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola2.place(relx=0.216, rely=0.39)

        self.bola2_entry = Entry(self.aba1)
        self.bola2_entry.place(relx=0.20, rely=0.45, relwidth=0.07)

        self.lb_bola3 = Label(self.aba1, text="Bola 03", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola3.place(relx=0.296, rely=0.39)

        self.bola3_entry = Entry(self.aba1)
        self.bola3_entry.place(relx=0.28, rely=0.45, relwidth=0.07)

        self.lb_bola4 = Label(self.aba1, text="Bola 04", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola4.place(relx=0.377, rely=0.39)

        self.bola4_entry = Entry(self.aba1)
        self.bola4_entry.place(relx=0.36, rely=0.45, relwidth=0.07)

        self.lb_bola5 = Label(self.aba1, text="Bola 05", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola5.place(relx=0.457, rely=0.39)

        self.bola5_entry = Entry(self.aba1)
        self.bola5_entry.place(relx=0.44, rely=0.45, relwidth=0.07)

        self.lb_bola6 = Label(self.aba1, text="Bola 06", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola6.place(relx=0.537, rely=0.39)

        self.bola6_entry = Entry(self.aba1)
        self.bola6_entry.place(relx=0.52, rely=0.45, relwidth=0.07)

        self.lb_bola7 = Label(self.aba1, text="Bola 07", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola7.place(relx=0.617, rely=0.39)

        self.bola7_entry = Entry(self.aba1)
        self.bola7_entry.place(relx=0.60, rely=0.45, relwidth=0.07)

        self.lb_bola8 = Label(self.aba1, text="Bola 08", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola8.place(relx=0.697, rely=0.39)

        self.bola8_entry = Entry(self.aba1)
        self.bola8_entry.place(relx=0.68, rely=0.45, relwidth=0.07)

        self.lb_bola9 = Label(self.aba1, text="Bola 09", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola9.place(relx=0.177, rely=0.59)

        self.bola9_entry = Entry(self.aba1)
        self.bola9_entry.place(relx=0.16, rely=0.65, relwidth=0.07)

        self.lb_bola10 = Label(self.aba1, text="Bola 10", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola10.place(relx=0.257, rely=0.59)

        self.bola10_entry = Entry(self.aba1)
        self.bola10_entry.place(relx=0.24, rely=0.65, relwidth=0.07)

        self.lb_bola11 = Label(self.aba1, text="Bola 11", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola11.place(relx=0.337, rely=0.59)

        self.bola11_entry = Entry(self.aba1)
        self.bola11_entry.place(relx=0.32, rely=0.65, relwidth=0.07)

        self.lb_bola12 = Label(self.aba1, text="Bola 12", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola12.place(relx=0.417, rely=0.59)

        self.bola12_entry = Entry(self.aba1)
        self.bola12_entry.place(relx=0.40, rely=0.65, relwidth=0.07)

        self.lb_bola13 = Label(self.aba1, text="Bola 13", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola13.place(relx=0.497, rely=0.59)

        self.bola13_entry = Entry(self.aba1)
        self.bola13_entry.place(relx=0.48, rely=0.65, relwidth=0.07)

        self.lb_bola14 = Label(self.aba1, text="Bola 14", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola14.place(relx=0.577, rely=0.59)

        self.bola14_entry = Entry(self.aba1)
        self.bola14_entry.place(relx=0.56, rely=0.65, relwidth=0.07)

        self.lb_bola15 = Label(self.aba1, text="Bola 15", bd=2,bg='#1C1C1C',fg='white',font=('verdana',8, 'bold'))
        self.lb_bola15.place(relx=0.657, rely=0.59)

        self.bola15_entry = Entry(self.aba1)
        self.bola15_entry.place(relx=0.64, rely=0.65, relwidth=0.07)

        # ABA 2 - Probabilidades

        # Label de Apresentação
        self.lb_aprese = Label(self.aba2,
        text="""Nessa Seção é possível Calcular sua probabilidade\n 
                A medida que você faz mais jogos sua chance de ganhar aumenta!!\n
                Use a calculdora de probabilidade e descubra suas chances!""",
        bd=2, bg='#1C1C1C', fg='white', font=('verdana', 8, 'bold'),anchor = 'nw',justify = 'center')
        self.lb_aprese.place(relx=0.2, rely=0)


        # Botões de Cálculo de probabilidades

        self.label1 = Label(self.aba2, text="Digite a quantidade de jogos que deseja realizar", font="times 12", bd=2,
                            bg='#1C1C1C', fg='white')
        self.label1.place(relx=0, rely=0.4)

        self.tb1 = Entry(self.aba2)
        self.tb1.place(relx=0.21, rely=0.4, relwidth=0.05, relheight=0.08)

        self.final = StringVar()
        self.b = Button(self.aba2, text="Calcular", command=self.calc, bd=2, bg='#1C1C1C', fg='white',
                        font=('verdana', 10, 'bold'))
        self.b.place(relx=0.21, rely=0.5, relwidth=0.05, relheight=0.08)

        self.label_resultado = Label(self.aba2, textvariable=self.final, font='Times 20', bd=2, bg='#1C1C1C',
                                     fg='white')
        self.label_resultado.place(relx=0.31, rely=0.4, relwidth=0.5, relheight=0.2)


        # ABA 3 Sortear

        # Label de Apresentação
        self.lb_aprese = Label(self.aba3,
                               text="""Clique no botão sortear e gere jogos de qualidade!""",
                               bd=2, bg='#1C1C1C', fg='white', font=('verdana', 8, 'bold'), anchor='nw',
                               justify='center')
        self.lb_aprese.place(relx=0, rely=0)

        # Botão Sortear
        self.bt_sortear = Button(self.aba3, text="Sortear", bd=2, bg='#1C1C1C', fg='white', font=('verdana', 8, 'bold'),
                                command=self.busca_Concurso)
        self.bt_sortear.place(relx=0.085, rely=0.3, relwidth=0.1, relheight=0.15)

        self.lb_sortear = Label(self.aba3, text="Digite a quantidade de jogos que desejar fazer: ",
                              bd=2, bg='#1C1C1C', fg='white', font=('verdana', 10, 'bold'))
        self.lb_sortear.place(relx=0, rely=0.2)

        self.sortear_entry = Entry(self.aba3, font=('verdana', 10, 'bold'))
        self.sortear_entry.place(relx=0.255, rely=0.2, relwidth=0.04, relheight=0.07)


    def lista_frame2(self):
        self.listaBanco = ttk.Treeview(self.frame_2,height=3,column=("col1", "col2", "col3","col4", "col5", "col6", "col7", "col8", "col9","col10", "col11", "col12","col13", "col14", "col15","col16"))
        self.listaBanco.heading("#0", text="")
        self.listaBanco.heading("#1", text="CON")
        self.listaBanco.heading("#2", text="B01")
        self.listaBanco.heading("#3", text="B02")
        self.listaBanco.heading("#4", text="B03")
        self.listaBanco.heading("#5", text="B04")
        self.listaBanco.heading("#6", text="B05")
        self.listaBanco.heading("#7", text="B06")
        self.listaBanco.heading("#8", text="B07")
        self.listaBanco.heading("#9", text="B08")
        self.listaBanco.heading("#10", text="B09")
        self.listaBanco.heading("#11", text="B10")
        self.listaBanco.heading("#12", text="B11")
        self.listaBanco.heading("#13", text="B12")
        self.listaBanco.heading("#14", text="B13")
        self.listaBanco.heading("#15", text="B14")
        self.listaBanco.heading("#16", text="B15")

        self.listaBanco.column("#0", width=1)
        self.listaBanco.column("#1", width=10)
        self.listaBanco.column("#2", width=10)
        self.listaBanco.column("#3", width=10)
        self.listaBanco.column("#4", width=10)
        self.listaBanco.column("#5", width=10)
        self.listaBanco.column("#6", width=10)
        self.listaBanco.column("#7", width=10)
        self.listaBanco.column("#8", width=10)
        self.listaBanco.column("#9", width=10)
        self.listaBanco.column("#10", width=10)
        self.listaBanco.column("#11", width=10)
        self.listaBanco.column("#12", width=10)
        self.listaBanco.column("#13", width=10)
        self.listaBanco.column("#14", width=10)
        self.listaBanco.column("#15", width=10)
        self.listaBanco.column("#16", width=10)

        self.listaBanco.place(relx=0.025, rely=0.02, relwidth=0.95, relheight=0.85)
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaBanco.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.975, rely=0.02, relwidth=0.025,relheight=0.85)
        self.listaBanco.bind("<Double-1>", self.doisClicks)


Application()