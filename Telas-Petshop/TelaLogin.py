import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

# Criar a interface gráfica
tela = Tk()
tela.title("Login Cliente")
tela.geometry("500x200")

#Adicionar backgroud 
background_image = Image.open("icones/8.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(tela, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Função para fazer login
def fazer_login():
    nome = entry_nome.get()
    cpf = entry_cpf.get()

    # Conectar ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="TelasPython"
    )

    # Criar um cursor
    cursor = conexao.cursor()

    # Executar a consulta para verificar se o usuário existe
    sql = "SELECT * FROM clientes WHERE nome = %s AND cpf = %s"
    valores = (nome, cpf)
    cursor.execute(sql, valores)

    # Verificar se há um resultado na consulta
    resultado = cursor.fetchone()

    # Verificar se o login foi bem-sucedido
    if resultado is not None:
        label_status["text"] = "Login bem-sucedido!"
    else:
        label_status["text"] = "Usuário ou senha inválidos."

    # Fechar a conexão
    conexao.close()

# Criar labels
label_nome = Label(tela, text="Nome:")
label_nome.place(x=20, y=20)

label_cpf = Label(tela, text="CPF:")
label_cpf.place(x=20, y=50)

label_status = Label(tela, text="")
label_status.place(x=20, y=80)

# Criar campos de entrada
entry_nome = Entry(tela, width=30)
entry_nome.place(x=100, y=20)

entry_cpf = Entry(tela, width=30)
entry_cpf.place(x=100, y=50)

# Criar botão de login
btn_adicionar_foto = PhotoImage(file=r"icones\entra1.png")
btn_login = Button(tela, text="Login", image=btn_adicionar_foto, command=fazer_login, compound=TOP)
btn_login.place(x=20, y=110)

# Criar botão para sair
btn_excluir_2= PhotoImage(file=r"icones\entrar.png")
btn_excluir= Button(tela,text="Sair",image=btn_excluir_2, command=exit,compound=TOP).place(x=100,y=110)

tela.mainloop()
