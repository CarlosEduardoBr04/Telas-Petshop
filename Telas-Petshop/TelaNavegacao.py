from tkinter import *
from PIL import ImageTk
import subprocess

def abrir_arquivo1():
    subprocess.run(["python", "TelaLogin.py"])

def abrir_arquivo2():
    subprocess.run(["python", "TelaCadastroCliente.py"])

def abrir_arquivo3():
   subprocess.run(["python", "TelaCadastroServiços.py"])

def abrir_arquivo4():
    subprocess.run(["python", "TelaCadastroAnimal.py"])

def abrir_arquivo5():
    subprocess.run(["python", "TelaFeedBack.py"])

janela = Tk()
janela.title("Navegação")

# Carrega as imagens
imagem1 = ImageTk.PhotoImage(file="icones/login1.png")
imagem2 = ImageTk.PhotoImage(file="icones/cadastro.png")
imagem3 = ImageTk.PhotoImage(file="icones/pet.png")
imagem4 = ImageTk.PhotoImage(file="icones/cpets.png")
imagem5 = ImageTk.PhotoImage(file="icones/feedback.png")

# Cria os botões com as imagens
botao1 = Button(janela, image=imagem1, command=abrir_arquivo1, text="Login", compound=TOP)
botao2 = Button(janela, image=imagem2, command=abrir_arquivo2, text="Cadastro Cliente", compound=TOP)
botao3 = Button(janela, image=imagem3, command=abrir_arquivo3, text="Cadastro Serviços", compound=TOP)
botao4 = Button(janela, image=imagem4, command=abrir_arquivo4, text="Cadastro Animal", compound=TOP)
botao5 = Button(janela, image=imagem5, command=abrir_arquivo5,  text="FeedBack", compound=TOP)

# Adiciona os botões à janela
botao1.pack(side=LEFT)
botao2.pack(side=LEFT)
botao3.pack(side=LEFT)
botao4.pack(side=LEFT)
botao5.pack(side=LEFT)

janela.mainloop()
