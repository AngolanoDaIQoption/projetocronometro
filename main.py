from tkinter import *
import tkinter

# cores

cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul
cor7 = "#1b1a1e"  # preto fraco
cor8 = "#1b1a6d"  # azul mais escuro
cor9 = "#dcdfdf"  # esbranquicado

#janela

janela = Tk()
janela.title("")
janela.geometry('360x200')
janela.configure(bg=cor7)
janela.resizable(width=False, height=False)

tempo= '00:00:00'
rodar = False
limitador = 59
seg =0

#funcao para iniciar

def iniciar():
    global contador
    global tempo
    global limitador
    global seg

    if rodar:

        label_tempo['font'] = 'Times 40 bold'

        h, m, s = map(int, tempo.split(":"))
        s += seg

        if s <= 0:
            seg = 1
        elif s >= limitador:
            s = 0
            m += 1
        elif m>= limitador:
            m = 0
            h+=1
        tempo = "{:02d}:{:02d}:{:02d}".format(h, m, s)
        label_tempo['text'] = tempo

        label_tempo.after(1000, iniciar)

#funcao que puxa a iniciar e starta ela

def start():
    global rodar
    rodar =True
    iniciar()


#funcao pausar

def pausar():
    global rodar
    rodar = False

#funcao reiniciar

def reiniciar():
    global tempo
    tempo= '00:00:00'
    label_tempo['text']= tempo


#labels

label_title = Label(janela, text='CRONÔMETRO', font=('Arial 10'), bg=cor7, fg=cor9)
label_title.place(x=137, y=10)

label_tempo = Label(janela, text=tempo, font=('Times 40 bold'), bg=cor7, fg=cor9)
label_tempo.place(x=85, y=45)

#botoes

botao_iniciar = Button(janela, command=start, text='INICIAR', width=8, height=2, bg=cor8, fg=cor9, font='ivy 8 bold', relief='raised', overrelief='ridge')
botao_iniciar.place(x=75, y=135)

botao_pausar = Button(janela, command=pausar, text='PAUSAR', width=8, height=2, bg=cor8, fg=cor9, font='ivy 8 bold', relief='raised', overrelief='ridge')
botao_pausar.place(x=155, y=135)

botao_reiniciar = Button(janela, command=reiniciar, text='REINICIAR', width=8, height=2, bg=cor8, fg=cor9, font='ivy 8 bold', relief='raised', overrelief='ridge')
botao_reiniciar.place(x=235, y=135)



janela.mainloop()
