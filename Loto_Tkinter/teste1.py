from tkinter import *
from math import factorial


#--------------------------------------------
# Funções
def Combinacaofix():
    cUniv = 25

    qNescolh = 15

    subt = cUniv - qNescolh

    fcUniv = factorial(cUniv)

    fqNescolh = factorial(qNescolh)

    fsubt = factorial(subt)

    comb = fcUniv / (fsubt * fqNescolh)

    qjogos = (int(qtjog_entry.get()))


    res = 3268760/qjogos


    final.set("A sua Probabilidade é 1 em " + str(res))



#--------------------------------------------
# GUI
root = Tk()
root.title("Calculadora")
root.geometry("1000x1000")
final= StringVar()

#--------------------------------------------
# Widgets

lb_qtjog = Label(root, text="Digite a quantidade de jogos que desejar fazer: ",
                      bd=2, bg='#1C1C1C', fg='white', font=('verdana', 10, 'bold'))
lb_qtjog.place(relx=0, rely=0.4)
qtjog_entry = Entry(root, font=('verdana', 10, 'bold'))

qtjog_entry.place(relx=0.248, rely=0.4, relwidth=0.04, relheight=0.07)
bt_proba = Button(root, text="Calcular", bd=2, bg='#1C1C1C', fg='white',
                       font=('verdana', 12, 'bold'), command= Combinacaofix)
bt_proba.place(relx=0.8, rely=0.1, relwidth=0.12, relheight=0.15)
label_resultado = Label(root,textvariable=final, font='Times 20').place(relx=0.148, rely=0.5, relwidth=0.3, relheight=0.21)

#--------------------------------------------
# Layout


root.mainloop()