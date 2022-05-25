# TESTE COMMIT
# IMPORTANDO TKINTER (GUI - Graphical user interface)
from tkinter import * 
from tkinter import ttk

# - cores
preto = "#1e1f1e"
branca = "#feffff"
azul = "#38576b" # Azul carregado, quase cinza
cinzento = "#ECEFF1"
laranja = "#FFAB40"


# ---------- FRAMES (DIVISÕES DA TELA) 

# - Criar a janela e suas config. básicas
janela = Tk()
janela.title("CalculadoraGui")
janela.geometry("245x310")
janela.config( bg = preto)

# VIZOR ONDE APARECE RESULTADO
frame_tela = Frame(janela, width = 245 ,height = 50, bg = azul)
frame_tela.grid(row = 0, column = 0)

# - Corpo onde fica os botões
 
frame_corpo = Frame(janela, width = 245 , height = 268)
frame_corpo.grid(row = 1, column = 0)

# - Variável todos os valores

todos_os_valores = ''

valor_texto = StringVar()
# ------------------------------- Função entrada de valores

def entrar_valores(event):
    
    global todos_os_valores

    todos_os_valores += str(event)

    

    # passando valor para a tela
    valor_texto.set(todos_os_valores) # Colocando o resultado da operação

#    FUNÇÃO PARA CALCULAR ------------------------------------------------------------------

def calcular():
    
    global todos_os_valores
    resultado = eval(todos_os_valores) # EVAL CALCULA OS VALORES DE UMA STR
    
    valor_texto.set(str(resultado)) # APARECE O RESULTADO NA TELA, Se declara str para evitar erro.
    
# FUNÇÃO: LIMPAR TELA ----------------------------------------------------------------------

def limpar_tela():
    global todos_os_valores 
    
    todos_os_valores = ''
    valor_texto.set('')



# - Criando label ----------------------------------------------------------------

app_label = Label(frame_tela, textvariable= valor_texto, width=16, height=2, padx=8, relief=FLAT,
anchor="e", justify=RIGHT,font=("Ivy 18 "), bg=azul, fg=branca) # -» O textvariable permite ser modificado dinamicamente.
# Logo nos permite colocar valores e mudalos    

app_label.place(x=0, y=0)

# ---------------- Botões
clean = Button(frame_corpo, command = limpar_tela,
text = "C", width = 11, height = 2, bg = cinzento, font = ("Ivy 13 bold"),relief = RAISED,
overrelief = RIDGE)

clean.place(x = 2, y = 0) # x é a linha horizontal e y é a linha vertical

# RESTO DA DIVISÃO % -------------» Função lambada permite exercutar cód em uma só linha
restoDaDivisão = Button(frame_corpo, command = lambda: entrar_valores("%"),text = "%", width = 5,
height = 2, bg = cinzento, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)

restoDaDivisão.place (x = 124, y = 0)

# DIVISÃO 
divisão = Button(frame_corpo,command = lambda: entrar_valores("/"), text = "/", width = 5,height=2,
bg = laranja, fg = branca, font=("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)

divisão.place(x =186, y = 0)

#MULTIPLICAÇÃO
multiplicação = Button(frame_corpo,command = lambda:entrar_valores('*'), text = "*", width = 5,
height=2, bg=laranja, fg=branca, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)

multiplicação.place(x=186, y=52)

#SUBTRAÇÃO
subtração = Button(frame_corpo,command=lambda:entrar_valores('-'), text = "-", width = 5, height=2,
bg=laranja, fg=branca,font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)

subtração.place(x=186, y=104)

#ADIÇÃO
adição = Button(frame_corpo,command=lambda:entrar_valores('+'), text="+", width=5, height=2,
bg=laranja, fg=branca, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)

adição.place(x=186, y=156)

# - IGUAL
igual = Button(frame_corpo,command = calcular,
text="=", width=5, height=2, bg=laranja, fg=branca, font=("Ivy 13 bold"),relief=RAISED,
overrelief=RIDGE)

igual.place(x=186, y=208)


# ------------------- Botões numéricos ---------------------------------------------------------
#Botão 1 -----------------------------------------------------------------------------------------

b_1 = Button(frame_corpo,command=lambda:entrar_valores('1'),
text=1, width = 5,height = 2,bg = cinzento,font =("Ivy 13 bold"),relief=RAISED, overrelief = RIDGE)

b_1.place(x=0, y = 52)

#Botão 2 ----------------------------------------------------------------------------------------- 
b_2 = Button(frame_corpo,command=lambda:entrar_valores('2'),
text = 2, width = 5, height =2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED,overrelief= RIDGE)

b_2.place(x=62, y=52)

#Botão 3 -----------------------------------------------------------------------------------------
b_3 = Button(frame_corpo,command=lambda:entrar_valores('3'),
text=3, width=5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief = RIDGE)

b_3.place(x=124, y=52)

#Botão 4 -----------------------------------------------------------------------------------------
b_4 = Button(frame_corpo,command=lambda:entrar_valores('4'),
text=4, width=5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)

b_4.place(x=0, y=104)

#Botão 5 -----------------------------------------------------------------------------------------
b_5 = Button(frame_corpo,command=lambda:entrar_valores('5'),
text=5, width=5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)

b_5.place(x = 62, y = 104)

#Botão 6 -----------------------------------------------------------------------------------------
b_6 = Button(frame_corpo,command=lambda:entrar_valores('6'),
text=6, width=5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief = RIDGE)

b_6.place(x=124, y=104)

#Botão 7 -----------------------------------------------------------------------------------------
b_7 = Button(frame_corpo,command=lambda:entrar_valores('7'),
text=7, width=5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief= RIDGE)

b_7.place(x=0, y=156)

#Botão 8 -----------------------------------------------------------------------------------------
b_8 = Button(frame_corpo,command=lambda:entrar_valores('8'),
text = 8, width = 5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief= RIDGE)
b_8.place(x= 62, y =156)

#Botão 9 -----------------------------------------------------------------------------------------
b_9 = Button(frame_corpo,command=lambda:entrar_valores('9'),
text = 9, width=5, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief = RIDGE)
b_9.place(x=124, y=156)

# 0 ZERO ------------------------------------------------------------------------------------------
b_zero = Button(frame_corpo,command=lambda:entrar_valores('0'),
text=0, width=11, height=2, bg=cinzento, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_zero.place(x=2, y=208)

# ----- PONTO
b_ponto = Button(frame_corpo, command=lambda:entrar_valores('.'),
text = ".", width = 5, height=2, bg=cinzento, font=("Ivy 13 bold"),relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=124, y=208)


# Roda a calculadora.
janela.mainloop()
