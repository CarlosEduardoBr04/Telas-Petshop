import mysql.connector
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk



# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TelasPython"
)

# Criar o banco de dados se ele não existir
cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS TelasPython")

print("Banco de dados criado com sucesso!")

# Criar a tabela (caso ainda não exista)
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS animal (
        codigo INT PRIMARY KEY,
        nome VARCHAR(100),
        sexo VARCHAR(20),
        raca VARCHAR(20),
        peso VARCHAR(20),
        idade VARCHAR(20),
        observacao VARCHAR(100),
        data_cadastro DATE
    )
""")
conexao.commit()

# Função para adicionar um animal
def adicionar_animal():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    sexo = txt_sexo.get()
    raca = txt_raca.get()
    peso = txt_peso.get()
    idade = txt_idade.get()
    observacao = txt_observacao.get()
    data_cadastro = txt_dataCadas.get()
    
    # Inserir os dados na tabela
    cursor.execute("""
        INSERT INTO animal (codigo, nome, sexo, raca, peso, idade, observacao, data_cadastro)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (codigo, nome, sexo, raca, peso, idade, observacao, data_cadastro))
    
    conexao.commit()

# Função para limpar as caixas de entrada
def redefinir():
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_sexo.delete(0, END)
    txt_raca.delete(0, END)
    txt_peso.delete(0, END)
    txt_idade.delete(0, END)
    txt_observacao.delete(0, END)
    txt_dataCadas.delete(0, END)
    
# Função alterar
def alterar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    sexo = txt_sexo.get()
    raca = txt_raca.get()
    peso = txt_peso.get()
    idade = txt_idade.get()
    observacao = txt_observacao.get()
    data_cadastro = txt_dataCadas.get()
    
    # Verifica se há campos em branco
    if (codigo == "" or nome == "" or sexo == "" or raca == "" or peso == "" or idade == "" or observacao == "" or data_cadastro == ""):
        messagebox.showinfo("Erro", "Há campos em branco")
    else:
        # Estabelece a conexão com o banco de dados
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="TelasPython")
        cursor = conectar.cursor()
        
        # Executa a atualização no banco de dados
        cursor.execute("UPDATE animal SET nome=%s, sexo=%s, peso=%s, idade=%s, observacao=%s ,data_cadastro=%s WHERE codigo=%s", (nome, sexo, peso, idade, observacao, data_cadastro, codigo))
        conectar.commit()
        
        # Exibe a mensagem de sucesso
        messagebox.showinfo("Mensagem", "Alteração realizada com sucesso")
        
        # Fecha a conexão com o banco de dados
        conectar.close()


# Função Excluir
def excluir():
    codigo = txt_codigo.get()
    if codigo == "":
        messagebox.showinfo("ALERTA", "Digite um código para deletar")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="TelasPython")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM animal WHERE codigo=%s", (codigo,))
        conectar.commit()
        messagebox.showinfo("Mensagem", "Informação Excluída com Sucesso")
        conectar.close()


# Função Select
def consultar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    sexo = txt_sexo.get()
    raca = txt_raca.get()
    peso = txt_peso.get()
    idade = txt_idade.get()
    observacao = txt_observacao.get()
    data_cadastro = txt_dataCadas.get()

    if codigo == "":
        messagebox.showinfo("ALERTA", "Digite um código para consultar")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="TelasPython")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM animal WHERE codigo='" + codigo + "'")
        rows = cursor.fetchall()
        conectar.close()

        for row in rows:
            txt_nome.insert(0, row[1])
            txt_sexo.insert(0, row[2])
            txt_raca.insert(0, row[3])
            txt_peso.insert(0, row[4])
            txt_idade.insert(0, row[5])
            txt_observacao.insert(0, row[6])
            txt_dataCadas.insert(0, row[7])

def selecionar_imagem():
    file_path = filedialog.askopenfilename()
    if file_path:
        imagem = Image.open(file_path)
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem.configure(image=imagem_tk)
        label_imagem.image = imagem_tk

# Criar a interface gráfica
tela = Tk()
tela.title("Cadastro Animal")
tela.geometry("500x300")

#Adicionar backgroud 
background_image = Image.open("icones/espaco.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(tela, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#637344535
label_imagem = Label(tela)
label_imagem.place(x=10, y=7)

botao_selecionar_imagem = Button(tela, text="Imagem", command=selecionar_imagem)
botao_selecionar_imagem.place(x=10, y=60)

lbl_codigo = Label(tela, text="Codigo:")
lbl_codigo.place(x=75, y=20)
lbl_nome = Label(tela, text="Nome:")
lbl_nome.place(x=80, y=50)
lbl_sexo = Label(tela, text="Sexo:")
lbl_sexo.place(x=87, y=80)
lbl_raca = Label(tela, text="Raca:")
lbl_raca.place(x=87, y=110)
lbl_peso = Label(tela, text="Peso:")
lbl_peso.place(x=87, y=140)
lbl_idade = Label(tela, text="Idade:")
lbl_idade.place(x=295, y=20)
lbl_observacao = Label(tela, text="Observação:")
lbl_observacao.place(x=261, y=50)
lbl_dataCadas = Label(tela, text="Data Cadastro:")
lbl_dataCadas.place(x=250, y=80)

txt_codigo = Entry(tela, width=20)
txt_codigo.place(x=120, y=20)
txt_nome = Entry(tela, width=20)
txt_nome.place(x=120, y=50)
txt_sexo = Entry(tela, width=20)
txt_sexo.place(x=120, y=80)
txt_raca = Entry(tela, width=20)
txt_raca.place(x=120, y=110)
txt_peso = Entry(tela, width=20)
txt_peso.place(x=120, y=140)
txt_idade = Entry(tela, width=20)
txt_idade.place(x=330, y=20)
txt_observacao = Entry(tela, width=20)
txt_observacao.place(x=330, y=50)
txt_dataCadas = Entry(tela, width=20)
txt_dataCadas.place(x=330, y=80)

btn_adicionar_1 = PhotoImage(file="icones/finalizar.png")
btn_adicionar = Button(tela, text="Cadastrar", command=adicionar_animal, image=btn_adicionar_1, compound=TOP)
btn_adicionar.place(x=441, y=230)

btn_excluir_2 = PhotoImage(file="icones/voltar.png")
btn_excluir = Button(tela, text="Excluir", image=btn_excluir_2, command=excluir, compound=TOP)
btn_excluir.place(x=1, y=230)

btn_alterar_3 = PhotoImage(file="icones/redefinir.png")
btn_alterar = Button(tela, text="Alterar", image=btn_alterar_3, command=alterar, compound=TOP)
btn_alterar.place(x=250, y=230)

btn_consultar_4 = PhotoImage(file="icones/historico.png")
btn_consultar = Button(tela, text="Consultar", image=btn_consultar_4, command=consultar, compound=TOP)
btn_consultar.place(x=330, y=110)

btn_consultar_5 = PhotoImage(file="icones/7.png")
btn_redefinir = Button(tela, text="Redefinir", image=btn_consultar_5, command=redefinir, compound=TOP)
btn_redefinir.place(x=195, y=230)

tela.mainloop()

# Fechar a conexão com o banco de dados
conexao.close()
