from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import mysql.connector

def selecionar_imagem():
    file_path = filedialog.askopenfilename()
    if file_path:
        imagem = Image.open(file_path)
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem.configure(image=imagem_tk)
        label_imagem.image = imagem_tk

def criar_banco_dados():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS TelasPython")

    cursor.execute("USE TelasPython")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            codigo INT PRIMARY KEY,
            nome VARCHAR(100),
            cpf VARCHAR(14),
            data_nascimento DATE,
            endereco VARCHAR(100),
            celular VARCHAR(15),
            telefone VARCHAR(15),
            data_cadastro DATE,
            genero VARCHAR(50)
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_cliente():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="TelasPython"
    )

    cursor = conexao.cursor()
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    cpf = txt_cpf.get()
    data_nascimento = txt_dataNasci.get()
    endereco = txt_endereco.get()
    celular = txt_celular.get()
    telefone = txt_telefone.get()
    data_cadastro = txt_dataCadas.get()
    genero = txt_genero.get()

    cursor.execute("""
        INSERT INTO clientes (codigo, nome, cpf, data_nascimento, endereco, celular, telefone, data_cadastro, genero)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (codigo, nome, cpf, data_nascimento, endereco, celular, telefone, data_cadastro, genero))

    conexao.commit()
    conexao.close()
    messagebox.showinfo("Mensagem", "Cadastro realizado com sucesso")

def redefinir():
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_cpf.delete(0, END)
    txt_dataNasci.delete(0, END)
    txt_endereco.delete(0, END)
    txt_celular.delete(0, END)
    txt_telefone.delete(0, END)
    txt_dataCadas.delete(0, END)
    txt_genero.delete(0, END)

def consultar():
    codigo = txt_codigo.get()

    if codigo == "":
        messagebox.showinfo("ALERTA", "Digite um código para consultar")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="TelasPython")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM clientes WHERE codigo='" + codigo + "'")
        rows = cursor.fetchall()
        conectar.close()

        for row in rows:
            txt_nome.insert(0, row[1])
            txt_cpf.insert(0, row[2])
            txt_dataNasci.insert(0, row[3])
            txt_endereco.insert(0, row[4])
            txt_celular.insert(0, row[5])
            txt_telefone.insert(0, row[6])
            txt_dataCadas.insert(0, row[7])
            txt_genero.insert(0, row[8])

def excluir():
    codigo = txt_codigo.get()

    if codigo == "":
        messagebox.showinfo("ALERTA", "Digite um código para deletar")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="TelasPython")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM clientes WHERE codigo=%s", (codigo,))
        conectar.commit()
        messagebox.showinfo("Mensagem", "Informação Excluída com Sucesso")
        conectar.close()

def alterar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    cpf = txt_cpf.get()
    data_nasci = txt_dataNasci.get()
    endereco = txt_endereco.get()
    celular = txt_celular.get()
    telefone = txt_telefone.get()
    data_cadas = txt_dataCadas.get()
    genero = txt_genero.get()

    if (codigo == "" or nome == "" or cpf == "" or data_nasci == "" or endereco == "" or celular == "" or telefone == "" or data_cadas == "" or genero == ""):
        messagebox.showinfo("Erro", "Há campos em branco")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="TelasPython")
        cursor = conectar.cursor()
        cursor.execute("UPDATE clientes SET nome=%s, cpf=%s, data_nascimento=%s, endereco=%s, celular=%s, telefone=%s, data_cadastro=%s, genero=%s WHERE codigo=%s", (nome, cpf, data_nasci, endereco, celular, telefone, data_cadas, genero, codigo))
        conectar.commit()
        messagebox.showinfo("Mensagem", "Alteração realizada com sucesso")
        conectar.close()

criar_banco_dados()

tela = Tk()
tela.title("Cadastro Cliente")
tela.geometry("500x300")

background_image = Image.open("icones/10.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(tela, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_imagem = Label(tela)
label_imagem.place(x=10, y=7)

botao_selecionar_imagem = Button(tela, text="Imagem", command=selecionar_imagem)
botao_selecionar_imagem.place(x=10, y=60)

lbl_codigo = Label(tela, text="Codigo:")
lbl_codigo.place(x=75, y=20)
lbl_nome = Label(tela, text="Nome:")
lbl_nome.place(x=80, y=50)
lbl_cpf = Label(tela, text="CPF:")
lbl_cpf.place(x=87, y=80)
lbl_dataNasci = Label(tela, text="Data Nascimento:")
lbl_dataNasci.place(x=20, y=110)
lbl_endereco = Label(tela, text="Endereco:")
lbl_endereco.place(x=60, y=140)
lbl_celular = Label(tela, text="Celular:")
lbl_celular.place(x=285, y=20)
lbl_telefone = Label(tela, text="Telefone:")
lbl_telefone.place(x=277, y=50)
lbl_dataCadas = Label(tela, text="Data Cadastro:")
lbl_dataCadas.place(x=250, y=80)
lbl_genero = Label(tela, text="Gênero:")
lbl_genero.place(x=70, y=170)

txt_codigo = Entry(tela, width=20)
txt_codigo.place(x=120, y=20)
txt_nome = Entry(tela, width=20)
txt_nome.place(x=120, y=50)
txt_cpf = Entry(tela, width=20)
txt_cpf.place(x=120, y=80)
txt_dataNasci = Entry(tela, width=20)
txt_dataNasci.place(x=120, y=110)
txt_endereco = Entry(tela, width=20)
txt_endereco.place(x=120, y=140)
txt_celular = Entry(tela, width=20)
txt_celular.place(x=330, y=20)
txt_telefone = Entry(tela, width=20)
txt_telefone.place(x=330, y=50)
txt_dataCadas = Entry(tela, width=20)
txt_dataCadas.place(x=330, y=80)
txt_genero = Entry(tela, width=20)
txt_genero.place(x=120, y=170)

btn_adicionar_1 = PhotoImage(file=r"icones\finalizar.png")
btn_adicionar = Button(tela, text="Cadastrar", command=adicionar_cliente, image=btn_adicionar_1, compound=TOP)
btn_adicionar.place(x=441, y=230)

btn_redefinir_2 = PhotoImage(file=r"icones/7.png")
btn_redefinir = Button(tela, text="Redefinir", image=btn_redefinir_2, command=redefinir, compound=TOP)
btn_redefinir.place(x=195, y=230)

btn_consultar_3 = PhotoImage(file="icones/historico.png")
btn_consultar = Button(tela, text="Consultar", image=btn_consultar_3, command=consultar, compound=TOP)
btn_consultar.place(x=330, y=110)

btn_excluir_4 = PhotoImage(file="icones/voltar.png")
btn_excluir = Button(tela, text="Excluir", image=btn_excluir_4, command=excluir, compound=TOP)
btn_excluir.place(x=1, y=230)

btn_alterar_5 = PhotoImage(file="icones/redefinir.png")
btn_alterar = Button(tela, text="Alterar", image=btn_alterar_5, command=alterar, compound=TOP)
btn_alterar.place(x=250, y=230)

tela.mainloop()
