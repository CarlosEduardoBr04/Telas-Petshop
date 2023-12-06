import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox



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
    CREATE TABLE IF NOT EXISTS servicos (
        codigo INT PRIMARY KEY,
        nome VARCHAR(100),
        descricao VARCHAR(100),
        valor_servicos VARCHAR(100),
        data_servico VARCHAR(20)  
    )
""")
conexao.commit()

# Função para adicionar um serviço
def adicionar_servicos():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    descricao = txt_descricao.get()
    valor_servicos = txt_valor_servicos.get()
    data_servico = txt_data_servico.get()

    # Verifica se há campos em branco
    if codigo == "" or nome == "" or descricao == "" or valor_servicos == "" or data_servico == "":
        messagebox.showinfo("Erro", "Há campos em branco")
    else:
        # Inserir os dados na tabela
        cursor.execute("""
            INSERT INTO servicos (codigo, nome, descricao, valor_servicos, data_servico)
            VALUES (%s, %s, %s, %s, %s)
        """, (codigo, nome, descricao, valor_servicos, data_servico))

        conexao.commit()
        messagebox.showinfo("Mensagem", "Cadastro realizado com sucesso")

# Função para alterar um serviço
def alterar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    descricao = txt_descricao.get()
    valor_servicos = txt_valor_servicos.get()
    data_servico = txt_data_servico.get()

    # Verifica se há campos em branco
    if codigo == "" or nome == "" or descricao == "" or valor_servicos == "" or data_servico == "":
        messagebox.showinfo("Erro", "Há campos em branco")
    else:
        # Executa a atualização no banco de dados
        cursor.execute("""
            UPDATE servicos SET nome=%s, descricao=%s, valor_servicos=%s, data_servico=%s
            WHERE codigo=%s
        """, (nome, descricao, valor_servicos, data_servico, codigo))

        conexao.commit()
        messagebox.showinfo("Mensagem", "Alteração realizada com sucesso")

# Função para excluir um serviço
def excluir():
    codigo = txt_codigo.get()

    if codigo == "":
        messagebox.showinfo("ALERTA", "Digite um código para deletar")
    else:
        # Executa a exclusão no banco de dados
        cursor.execute("DELETE FROM servicos WHERE codigo=%s", (codigo,))
        conexao.commit()
        messagebox.showinfo("Mensagem", "Informação excluída com sucesso")

# Função para consultar um serviço
def consultar():
    codigo = txt_codigo.get()

    if codigo == "":
        messagebox.showinfo("ALERTA", "Digite um código para consultar")
    else:
        # Executa a consulta no banco de dados
        cursor.execute("SELECT * FROM servicos WHERE codigo=%s", (codigo,))
        rows = cursor.fetchall()

        if len(rows) == 0:
            messagebox.showinfo("Mensagem", "Nenhum registro encontrado")
        else:
            for row in rows:
                nome = row[1]
                descricao = row[2]
                valor_servicos = row[3]
                data_servico = row[4]

                # Atualiza os campos de entrada com os dados consultados
                txt_nome.delete(0, END)
                txt_nome.insert(0, nome)
                txt_descricao.delete(0, END)
                txt_descricao.insert(0, descricao)
                txt_valor_servicos.delete(0, END)
                txt_valor_servicos.insert(0, valor_servicos)
                txt_data_servico.delete(0, END)
                txt_data_servico.insert(0, data_servico)
                
# Função para limpar as caixas de entrada
def redefinir():
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_descricao.delete(0, END)
    txt_valor_servicos.delete(0, END)
    txt_data_servico.delete(0, END)
   

# Criar a interface gráfica
tela = Tk()
tela.title("Cadastro Serviços")
tela.geometry("500x300")

#Adicionar backgroud 
background_image = Image.open("icones/9.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(tela, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl_codigo = Label(tela, text="Codigo:")
lbl_codigo.place(x=75, y=20)
lbl_nome = Label(tela, text="Nome:")
lbl_nome.place(x=80, y=50)
lbl_descricao = Label(tela, text="Descrição:")
lbl_descricao.place(x=64, y=80)
lbl_valor_servicos = Label(tela, text="Valor Serviços:")
lbl_valor_servicos.place(x=40, y=110)
lbl_data_servico = Label(tela, text="Data Serviço:")
lbl_data_servico.place(x=45, y=140)

txt_codigo = Entry(tela, width=20)
txt_codigo.place(x=120, y=20)
txt_nome = Entry(tela, width=20)
txt_nome.place(x=120, y=50)
txt_descricao= Entry(tela, width=20)
txt_descricao.place(x=120, y=80)
txt_valor_servicos= Entry(tela, width=20)
txt_valor_servicos.place(x=120, y=110)
txt_data_servico = Entry(tela, width=20)
txt_data_servico.place(x=120, y=140)

btn_adicionar_1 = PhotoImage(file=r"icones\finalizar.png")
btn_adicionar = Button(tela, text="Cadastrar", command=adicionar_servicos, image=btn_adicionar_1, compound=TOP)
btn_adicionar.place(x=441, y=230)

btn_excluir_2 = PhotoImage(file=r"icones\voltar.png")
btn_excluir = Button(tela, text="Excluir", command=excluir, image=btn_excluir_2, compound=TOP)
btn_excluir.place(x=1, y=230)

btn_alterar_3= PhotoImage(file=r"icones\redefinir.png")
btn_alterar= Button(tela,text="Alterar", image=btn_alterar_3, command=alterar, compound=TOP)
btn_alterar.place(x=250,y=230)

btn_consultar_4 = PhotoImage(file=r"icones\listaServi.png")
btn_consultar = Button(tela, text="Consultar", command=consultar, image=btn_consultar_4, compound=TOP)
btn_consultar.place(x=260, y=30)

btn_consultar_5 = PhotoImage(file="icones/7.png")
btn_redefinir = Button(tela, text="Redefinir", image=btn_consultar_5, command=redefinir, compound=TOP)
btn_redefinir.place(x=195, y=230)

tela.mainloop()

# Fechar a conexão com o banco de dados
conexao.close()
