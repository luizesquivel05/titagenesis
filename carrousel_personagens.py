import tkinter as tk
from PIL import Image, ImageTk

personagens = ['img/avatar/ALICE SILVA.png', 'img/avatar/AMANDA FERNANDES.png', 'img/avatar/ANA SOUZA.png', 'img/avatar/BEATRIZ ROCHA.png', 'img/avatar/BRUNA LIMA.png', 'img/avatar/BRUNO MENDES.png', 'img/avatar/CAMILA ALMEIDA.png', 'img/avatar/CAROLINA XAVIER.png', 'img/avatar/DANIEL ROCHA.png', 'img/avatar/FERNANDA PEREIRA.png', 'img/avatar/GABRIELA CARVALHO.png', 'img/avatar/GUILHERME CARVALHO.png', 'img/avatar/GUSTAVO PEREIRA.png', 'img/avatar/ISABELLA MENDES.png', 'img/avatar/JOAO SILVA.png', 'img/avatar/JULIA GOMES.png', 'img/avatar/JULIANA RIBEIRO.png', 'img/avatar/LAURA OLIVEIRA.png', 'img/avatar/LETICIA CARDOSO.png', 'img/avatar/LUCAS CASTRO.png', 'img/avatar/LUIZA SANTOS.png', 'img/avatar/MANUELA VIEIRA.png', 'img/avatar/MARIANA COSTA.png', 'img/avatar/MATHEUS COSTA.png', 'img/avatar/MIGUEL OLIVEIRA.png', 'img/avatar/PEDRO SOUZA.png', 'img/avatar/RAFAEL SANTOS.png', 'img/avatar/SOFIA CASTRO.png', 'img/avatar/THAIS BARBOSA.png', 'img/avatar/VITORIA RODRIGUES.png']

descricao = {
    "ALICE SILVA": "ALICE SILVA, 23 ANOS - ENFERMEIRA",
    "AMANDA FERNANDES": "SOFIA CASTRO, 35 ANOS, DESENVOLVEDORA DE SOFTWARE",
    "ANA SOUZA": "ANA SOUZA, 16 ANOS, sonha em ser ADVOGADA", 
    'BEATRIZ ROCHA': "DESCRIÇÃO",
    'BRUNA LIMA': "DESCRIÇÃO",
    'BRUNO MENDES': "DESCRIÇÃO",
    'CAMILA ALMEIDA': "DESCRIÇÃO",
    'CAROLINA XAVIER': "DESCRIÇÃO",
    'DANIEL ROCHA': "DESCRIÇÃO",
    'FERNANDA PEREIRA': "DESCRIÇÃO",
    'GABRIELA CARVALHO': "DESCRIÇÃO",
    'GUILHERME CARVALHO': "DESCRIÇÃO",
    'GUSTAVO PEREIRA': "DESCRIÇÃO",
    'ISABELLA MENDES': "DESCRIÇÃO",
    'JOAO SILVA': "DESCRIÇÃO",
    'JULIA GOMES': "DESCRIÇÃO",
    'JULIANA RIBEIRO': "DESCRIÇÃO",
    'LAURA OLIVEIRA': "DESCRIÇÃO",
    'LETICIA CARDOSO': "DESCRIÇÃO",
    'LUCAS CASTRO': "DESCRIÇÃO",
    'LUIZA SANTOS': "DESCRIÇÃO",
    'MANUELA VIEIRA': "DESCRIÇÃO",
    'MARIANA COSTA': "DESCRIÇÃO",
    'MATHEUS COSTA': "DESCRIÇÃO",
    'MIGUEL OLIVEIRA': "DESCRIÇÃO",
    'PEDRO SOUZA': "DESCRIÇÃO",
    'RAFAEL SANTOS': "DESCRIÇÃO",
    'SOFIA CASTRO': "DESCRIÇÃO",
    'THAIS BARBOSA': "DESCRIÇÃO",
    'VITORIA RODRIGUES': "DESCRIÇÃO"   
}
# Função para exibir informações sobre a imagem quando ela é clicada
def mostrar_info(imagem):
    # Crie uma janela
    janela_info = tk.Toplevel(root)
    janela_info.title("INFORMAÇÕES DO PERSONAGEM")

    # Adicione um rótulo com o nome do arquivo de imagem
    for i in descricao:
        nome = str(imagem)
        if i in nome:
            label_nome = tk.Label(janela_info, text=descricao[i])
            label_nome.pack()

    # Adicione um rótulo com informações adicionais sobre a imagem
    label_info = tk.Label(janela_info, text="SOBRE O PERSONAGEM")
    label_info.pack()

# Crie a janela principal
root = tk.Tk()
root.title("Galeria de imagens")

# Crie uma matriz de botões para exibir as imagens
for linha in range(5):
    for coluna in range(6):
        # Calcule o índice da imagem na lista
        indice = linha * 6 + coluna
        if indice < len(personagens):
            # Carregue a imagem usando a biblioteca PIL
            imagem = Image.open(personagens[indice])
            imagem = imagem.resize((100, 100)) # redimensione a imagem
            imagem = ImageTk.PhotoImage(imagem)

            # Crie um botão para exibir a imagem
            botao = tk.Button(root, image=imagem, command=lambda indice=indice: mostrar_info(personagens[indice]))
            botao.imagem = imagem # armazene a imagem como atributo do botão
            botao.grid(row=linha, column=coluna)

# Inicie o loop principal do tkinter
root.mainloop()