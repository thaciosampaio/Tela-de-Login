from tkinter import *
from tkinter import messagebox

master = Tk()
master.title('Login')
master.geometry('490x560+610+153')
master.resizable(width=1, height=1)

# Funções
def nova_janela():
    master1 = Tk()
    master1.title('Login')
    master1.geometry('490x560+400+153')
    lab_usuario = Label(master1, text=f'Bem Vindo!', font=('', 20))
    lab_usuario.place(x=150, y=220)

    master.destroy()

def click_button():
    usuario = en_usuario.get()
    senha = en_senha.get()
    if usuario == "admin" and senha == "admin":
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o usuario e senha')

# Variáveis Globais
esconda_senha = StringVar()


# Importar imagens
img_fundo = PhotoImage(file='imagens\\Fundo.png')
img_botao = PhotoImage(file='imagens\\Botão.png')


# Criação de labels
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

# Criação de caixas de entrada
en_usuario = Entry(master, bd=2, font=('Calibri', 15), justify=CENTER)
en_usuario.place(width=392, height=45, x=49, y=170)

en_senha = Entry(master, textvariable=esconda_senha, show='*', bd=2, font=('Calibri', 15), justify=CENTER)
en_senha.place(width=392, height=45, x=49, y=307)

# Criação de botões
bt_entrar = Button(master, bd=0, image=img_botao, command=click_button)
bt_entrar.place(width=163, height=69, x=163, y=442)


master.mainloop()
