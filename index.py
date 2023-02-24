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
    janela_principal.destroy()
    
    # cria a janela de login
    janela_login = Tk()
    janela_login.title("Login")
    janela_login.geometry('600x400')
    janela_login.resizable(False, False)

    # adiciona os widgets da janela de login
    label_usuario = Label(janela_login, font=('Montserrat', 20), text="Usuário:")
    label_usuario.place(x=110, y=30)
    entry_usuario = Entry(janela_login, font=('Montserrat', 20))
    entry_usuario.place(x=260, y=30)
    label_senha = Label(janela_login, font=('Montserrat', 20), text="Senha:")
    label_senha.place(x=110, y=140)
    entry_senha = Entry(janela_login, font=('Montserrat', 20),  show="*")
    entry_senha.place(x=260, y=140)
    botao_login = Button(janela_login, font=('Montserrat', 20),  text="Login", command=lambda: realizar_login(entry_usuario.get(), entry_senha.get(), tipo_jogo))
    botao_login.place(x=210, y=190)
    label_mensagem = Label(janela_login, font=('Montserrat', 20),  text="")
    label_mensagem.place(x=210, y=360)

# inicia o loop principal da janela
janela_principal.mainloop()

# define a função para realizar o login
def realizar_login(usuario, senha, tipo_jogo):
    # implemente sua lógica de login aqui
    # ...
    usuario = ...
    senha = ...
    tipo_jogo = ...