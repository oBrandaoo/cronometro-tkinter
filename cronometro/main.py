from tkinter import *
import tkinter

#cores
cor1 = '#050505'
cor2 = '#f7f7f7'
cor3 = '#0ceb47'
cor4 = '#eb1010'
cor5 = '#474646'
cor6 = '#1a10de'

#configs janela
janela = Tk()
janela.title("")
janela.geometry("300x200")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#definir variaveis globais
global tempo
global rodar
global contador
global limitador

tempo = "00:00:00"
rodar = False
contador = -5
limitador = 59

#criando funcoes
def iniciar():
    global tempo
    global contador
    global limitador


    if rodar:
        #antes do cronometro começar
        if contador <=-1:
            inicio = "Começando em " + str(contador)
            label_tempo["text"] = inicio
            label_tempo["font"] = "Arial 10"
        
        #rodando o cronometro
        else:
            label_tempo["font"] = "Times 50 bold"

            temporaria = str(tempo)
            h,m,s = map(int,temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if(s>=limitador):
                contador = 0
                m += 1

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #atualizando valores atuais
            temporaria=str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo["text"] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador +=1            

#funcao que começa a funcao iniciar
def start():
    global rodar
    rodar = True
    iniciar()

#funcao para pausar
def pausar():
    global rodar
    rodar = False

#reiniciando o contador e tempo
def reiniciar():
    global contador
    global tempo

    contador = 0
    tempo = "00:00:00"
    label_tempo["text"] = tempo


#labels
label_app = Label(janela, text="Cronômetro", font=("Arial 10 bold"), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=("Times 50 bold"), bg=cor1, fg=cor4)
label_tempo.place(x=20, y=30)

#buttons
botao_iniciar = Button(janela, text="Iniciar",command=start, width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief="raised", overrelief="ridge")
botao_iniciar.place(x=20, y=130)


botao_pausar = Button(janela, text="Pausar",command=pausar, width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief="raised", overrelief="ridge")
botao_pausar.place(x=106, y=130)


botao_reiniciar = Button(janela, text="Reiniciar",command=reiniciar, width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief="raised", overrelief="ridge")
botao_reiniciar.place(x=191, y=130)

janela.mainloop()