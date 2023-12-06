import cv2
import numpy as np
import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk


def rotate_image(image, angle):
    # Obtém as dimensões da imagem
    height, width = image.shape[:2]

    # Calcula o tamanho da imagem rotacionada
    rotation_angle = np.radians(angle)
    cos_theta = abs(np.cos(rotation_angle))
    sin_theta = abs(np.sin(rotation_angle))
    new_width = int((width * cos_theta) + (height * sin_theta))
    new_height = int((width * sin_theta) + (height * cos_theta))

    # Calcula a matriz de transformação de rotação
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Realiza a rotação da imagem usando a matriz de transformação
    rotated_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

    return rotated_image


def rotate_left():
    global angle
    angle -= 5
    rotated = rotate_image(original_image, angle)
    display_image(rotated)


def rotate_right():
    global angle
    angle += 5
    rotated = rotate_image(original_image, angle)
    display_image(rotated)


def display_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    canvas.configure(image=image)
    canvas.image = image


def save_evaluation():
    codigo_avaliacao = entry_data_avaliacao.get()
    codigo_usuario = entry_cpf.get()
    satisfacao_atendimento = entry_satisfacao.get()
    descricao = entry_descricao.get()

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TelasPython'
    )
    cursor = conn.cursor()
    insert_query = "INSERT INTO avaliacoes (data_avaliacao, cpf, satisfacao_atendimento, descricao) VALUES (%s, %s, %s, %s)"
    values = (codigo_avaliacao, codigo_usuario, satisfacao_atendimento, descricao)
    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Avaliação salva com sucesso!")


# Carrega a imagem
image_path = 'icones/seta.png'
original_image = cv2.imread(image_path)

# Configuração inicial
angle = 0

# Cria a janela
window = tk.Tk()
window.title("FeedBack")
window.geometry("500x500")  # Define a dimensão da janela como 500x500

# Cria um Label e um Entry para o código de avaliação
label_data_avaliacao = tk.Label(window, text="Data Avaliação:")
label_data_avaliacao.pack()
entry_data_avaliacao = tk.Entry(window)
entry_data_avaliacao.pack()

# Cria um Label e um Entry para o código de usuário
label_cpf = tk.Label(window, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(window)
entry_cpf.pack()

# Cria um Label e um Entry para a satisfação de atendimento
label_satisfacao = tk.Label(window, text="Satisfação de Atendimento:")
label_satisfacao.pack()
entry_satisfacao = tk.Entry(window)
entry_satisfacao.pack()

# Cria um Label e um Entry para a descrição
label_descricao = tk.Label(window, text="Descrição:")
label_descricao.pack()
entry_descricao = tk.Entry(window)
entry_descricao.pack()

# Cria o botão para salvar a avaliação
button_save = tk.Button(window, text="Salvar Avaliação", command=save_evaluation)
button_save.pack()

# Conecta ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='TelasPython'
)

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela "avaliacoes"
create_table_query = """
CREATE TABLE IF NOT EXISTS avaliacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_avaliacao DATE,
    cpf VARCHAR(11),
    satisfacao_atendimento VARCHAR(20),
    descricao VARCHAR(100)
)
"""
cursor.execute(create_table_query)

# Confirma as alterações no banco de dados
conn.commit()

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conn.close()

# Cria um frame para a imagem fixa 1
frame_imagem_fixa = tk.Frame(window, width=50, height=50)
frame_imagem_fixa.place(x=150, y=190)  # Posição da imagem fixa

# Carrega a imagem fixa 1
imagem_fixa_path = 'icones/ruim.png'
imagem_fixa = Image.open(imagem_fixa_path)
imagem_fixa = imagem_fixa.resize((50, 50), Image.ANTIALIAS)  # Ajusta o tamanho da imagem
imagem_fixa = ImageTk.PhotoImage(imagem_fixa)

# Cria um label para exibir a imagem fixa 1
label_imagem_fixa = tk.Label(frame_imagem_fixa, image=imagem_fixa)
label_imagem_fixa.pack()

# Cria um frame para a imagem fixa 2
frame_imagem_fixa2 = tk.Frame(window, width=50, height=50)
frame_imagem_fixa2.place(x=222, y=260)  # Posição da imagem fixa

# Carrega a imagem fixa 2
imagem_fixa_path2 = 'icones/neutro.png'
imagem_fixa2 = Image.open(imagem_fixa_path2)
imagem_fixa2 = imagem_fixa2.resize((50, 50), Image.ANTIALIAS)  # Ajusta o tamanho da imagem
imagem_fixa2 = ImageTk.PhotoImage(imagem_fixa2)

# Cria um label para exibir a imagem fixa 2
label_imagem_fixa2 = tk.Label(frame_imagem_fixa2, image=imagem_fixa2)
label_imagem_fixa2.pack()

# Cria um frame para a imagem fixa 3
frame_imagem_fixa3 = tk.Frame(window, width=50, height=50)
frame_imagem_fixa3.place(x=300, y=190)  # Posição da imagem fixa

# Carrega a imagem fixa 3
imagem_fixa_path3 = 'icones/feliz.png'
imagem_fixa3 = Image.open(imagem_fixa_path3)
imagem_fixa3 = imagem_fixa3.resize((50, 50), Image.ANTIALIAS)  # Ajusta o tamanho da imagem
imagem_fixa3 = ImageTk.PhotoImage(imagem_fixa3)

# Cria um label para exibir a imagem fixa 3
label_imagem_fixa3 = tk.Label(frame_imagem_fixa3, image=imagem_fixa3)
label_imagem_fixa3.pack()

# Cria o canvas para a imagem rotacionada
canvas = tk.Label(window)
canvas.pack()

# Cria os botões de rotação
button_left = tk.Button(window, text="⬅", command=rotate_left)
button_left.pack(side=tk.LEFT)
button_right = tk.Button(window, text="➡", command=rotate_right)
button_right.pack(side=tk.LEFT)

# Exibe a imagem original
display_image(original_image)

# Inicia o loop da interface gráfica
window.mainloop()
