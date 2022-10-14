from cgi import test
from tkinter import *
from tkinter import ttk

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"


janela = Tk()
janela.title('Calculadora ')
janela.geometry('235x318')
janela.config(bg=cor1)

#Criando Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#logica da calculadora

#criando função de calcular 
todos_valores = ''

#função para entrar valores na tela

def entrar_value(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
   
    valor_texto.set(todos_valores)

valor_texto = StringVar()

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

   

def limpar():
    global todos_valores
    todos_valores =''
    valor_texto.set('')




#criando label

app_label = Label(frame_tela, textvariable=valor_texto, width=16,height=2, padx=7, relief=FLAT,anchor='e',justify=RIGHT, font=('Ivy 18'), bg=cor3,fg=cor2)
app_label.place(x=0, y=0)


#criando botoes

b_1 = Button(frame_corpo, command= limpar ,text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo,command= lambda: entrar_value('%'), text='%', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo,command= lambda: entrar_value('/'), text='/', width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo,command= lambda: entrar_value('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_4.place(x=0, y=56)
b_5 = Button(frame_corpo,command= lambda: entrar_value('8'), text='8', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=56)
b_6 = Button(frame_corpo,command= lambda: entrar_value('9'), text='9', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=56)
b_7 = Button(frame_corpo,command= lambda: entrar_value('*'), text='*', width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=56)

b_12 = Button(frame_corpo,command= lambda: entrar_value('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_12.place(x=0, y=108)
b_13 = Button(frame_corpo,command= lambda: entrar_value('5'), text='5', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=108)
b_14 = Button(frame_corpo,command= lambda: entrar_value('6'), text='6', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=108)
b_15 = Button(frame_corpo,command= lambda: entrar_value('-'), text='-', width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=108)

b_16 = Button(frame_corpo,command= lambda: entrar_value('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_16.place(x=0, y=160)
b_17 = Button(frame_corpo,command= lambda: entrar_value('2'), text='2', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=60, y=160)
b_18 = Button(frame_corpo,command= lambda: entrar_value('3'), text='3', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=120, y=160)
b_19 = Button(frame_corpo,command= lambda: entrar_value('+'), text='+', width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=177, y=160)

b_20 = Button(frame_corpo,command= lambda: entrar_value('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_20.place(x=0, y=218)
b_21 = Button(frame_corpo,command= lambda: entrar_value('.'), text='.', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_21.place(x=120, y=218)
b_22 = Button(frame_corpo,command= calcular, text='=', width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_22.place(x=177, y=218)




janela.mainloop()