import tkinter as tk

def cadastrar():
    nome = entrada_nome.get()
    email = entrada_email.get()
    senha = entrada_senha.get()

    # Aqui você pode fazer o que quiser com os dados inseridos pelo usuário, como salvá-los em um banco de dados, por exemplo.

    print("Usuário cadastrado com sucesso!")
    janela.destroy()

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Cadastro")

# Cria as entradas de texto para o nome, email e senha
tk.Label(janela, text="Nome").grid(row=0, column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="E-mail").grid(row=1, column=0)
entrada_email = tk.Entry(janela)
entrada_email.grid(row=1, column=1)

tk.Label(janela, text="Senha").grid(row=2, column=0)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.grid(row=2, column=1)

# Cria o botão de cadastro
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.grid(row=3, column=1)

# Inicia a janela principal
janela.mainloop()
