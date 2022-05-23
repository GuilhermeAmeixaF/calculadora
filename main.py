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
janela.geometry("245x318")
janela.config( bg = preto)

# VIZOR ONDE APARECE RESULTADO
frame_tela = Frame(janela, width = 245 ,height = 50, bg = azul)
frame_tela.grid(row = 0, column = 0)

# - Corpo onde fica os botões
 
frame_corpo = Frame(janela, width = 245 , height = 268)
frame_corpo.grid(row = 1, column = 0) 



# ---------------- Botões
clean = Button(frame_corpo, text = "C", width = 11, height = 2, bg = cinzento, font = ("Ivy 13 bold"),
relief = RAISED, overrelief = RIDGE)

clean.place(x = 0, y = 0) # x é a linha horizontal e y é a linha vertical

# RESTO DA DIVISÃO %
restoDaDivisão = Button(frame_corpo, text = "%", width = 5, height = 2, bg = cinzento, font = 
("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)

restoDaDivisão.place (x = 124, y = 0)

# DIVISÃO 
divisão = Button(frame_corpo, text = "/", width = 5, height = 2, bg = laranja, fg = branca, font=
("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)

divisão.place(x =186, y = 0)

# ------------------- Botões numéricos :
b_1 = Button(frame_corpo, text=1, width = 5, height = 2, bg = cinzento, font =("Ivy 13 bold"),
relief=RAISED, overrelief = RIDGE)

b_1.place(x=0, y = 55)

# Botão 2
b_2 = Button(frame_corpo, text = 2, width = 5, height =2, bg=cinzento, font=("Ivy 13 bold"), relief=
RAISED, overrelief = RIDGE)

b_2.place(x=62, y=55)
# Roda a calculadora.
janela.mainloop()
