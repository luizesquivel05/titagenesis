from tkinter import *
from PIL import Image, ImageTk

# cria a janela principal
janela_principal = Tk()
janela_principal.title("TITÃGÊNESIS, COLONIZANDO A LUA DE SATURNO")
janela_principal.geometry('600x400')
janela_principal.resizable(False, False)

# título da janela
titulo_label = Label(janela_principal, text="TITÃGÊNESIS COLONIZANDO A LUA DE SATURNO", font=("Montserrat", 16), bg="#2b2b2b", fg="#ffffff")
titulo_label.pack(fill=X, padx=20, pady=20)

# carrega a imagem de fundo
imagem_fundo = Image.open("img/tita.png")
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
label_fundo = Label(janela_principal, image=imagem_fundo)
label_fundo.pack()

# adiciona os botões
botao_historia_individual = Button(janela_principal, text="HISTÓRIA - INDIVIDUAL", font=('Montserrat', 14), command=lambda: abrir_tela_login("História - individual"))
botao_historia_individual.place(x=190, y=220)
botao_historia_coletivo = Button(janela_principal, text="HISTÓRIA - COLETIVO", font=('Montserrat', 14), command=lambda: abrir_tela_login("História - coletivo"))
botao_historia_coletivo.place(x=190, y=270)
botao_competitivo = Button(janela_principal, text="COMPETITIVO", font=('Montserrat', 14), command=lambda: abrir_tela_login("Competitivo"))
botao_competitivo.place(x=210, y=320)

# define a função para abrir a tela de login
def abrir_tela_login(tipo_jogo):
    
# define a função para realizar o login
    def dadosUSER(p1, p2, p3, p4, p5, p6, tipo_jogo):
        # implemente sua lógica de login aqui
        # ...
        dadosJOGO = {'p1': f'{p1}','p2': f'{p2}','p3': f'{p3}','p4': f'{p4}','p5': f'{p5}','p6': f'{p6}','tipo_jogo': f'{tipo_jogo}',}
        return dadosJOGO
    
    janela_principal.destroy()
    
    # cria a janela de login
    janela_login = Tk()
    janela_login.title("Login")
    janela_login.geometry('600x400')
    janela_login.resizable(False, False)

    # adiciona os widgets da janela de login
    label_p1 = Label(janela_login, font=('Montserrat', 20), text="P1:")
    label_p1.place(x=30, y=30)
    entry_p1 = Entry(janela_login, font=('Montserrat', 20))
    entry_p1.place(x=110, y=30)
    label_p2 = Label(janela_login, font=('Montserrat', 20), text="P2:")
    label_p2.place(x=30, y=80)
    entry_p2 = Entry(janela_login, font=('Montserrat', 20))
    entry_p2.place(x=110, y=80)
    label_p3 = Label(janela_login, font=('Montserrat', 20), text="P3:")
    label_p3.place(x=30, y=140)
    entry_p3 = Entry(janela_login, font=('Montserrat', 20))
    entry_p3.place(x=110, y=140)
    label_p4 = Label(janela_login, font=('Montserrat', 20), text="P4:")
    label_p4.place(x=30, y=190)
    entry_p4 = Entry(janela_login, font=('Montserrat', 20))
    entry_p4.place(x=110, y=190)
    label_p5 = Label(janela_login, font=('Montserrat', 20), text="P5:")
    label_p5.place(x=30, y=240)
    entry_p5 = Entry(janela_login, font=('Montserrat', 20))
    entry_p5.place(x=110, y=240)
    label_p6 = Label(janela_login, font=('Montserrat', 20), text="P6:")
    label_p6.place(x=30, y=300)
    entry_p6 = Entry(janela_login, font=('Montserrat', 20))
    entry_p6.place(x=110, y=300)
    botao_login = Button(janela_login, font=('Montserrat', 20),  text="Entrar", command=lambda: dadosUSER(entry_p1.get(), entry_p2.get(),entry_p3.get(), entry_p4.get(),entry_p5.get(), entry_p6.get(), tipo_jogo))
    botao_login.place(x=210, y=340)
    label_mensagem = Label(janela_login, font=('Montserrat', 20),  text="")
    label_mensagem.place(x=400, y=340)

# inicia o loop principal da janela
janela_principal.mainloop()