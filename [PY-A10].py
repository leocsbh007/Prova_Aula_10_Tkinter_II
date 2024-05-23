'''
[PY-A10] Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter em Python. O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@", ou seja, realizar uma tela de login com restrições de e-mail e senha.
'''

import tkinter as tk
from tkinter.ttk import*

def valida_email_senha():
    lbl_usuario_valido = tk.Label(janela, font=('Arial', 12))   
    lbl_senha_valida = tk.Label(janela, font=('Arial', 12))    

    # Validação do Usuario
    if '@' in entry_usuario.get():
        lbl_usuario_valido.config(text="Email Valido                ",fg='black')
        lbl_usuario_valido.place(x=410, y=5, width=210, height=30)    

    else:
        lbl_usuario_valido.config(text="Email deve conter @           ",fg='red')
        lbl_usuario_valido.place(x=410, y=5, width=210, height=30)  

    # Validação da Senha
    if len(entry_senha.get()) > 6:        
        lbl_senha_valida.config(text="Senha Valida                ",fg='black')
        lbl_senha_valida.place(x=410, y=55, width=210, height=30)        
    elif len(entry_senha.get()) == 0:
        lbl_senha_valida.config(text="Erro - Senha Vazia          ",fg='red')
        lbl_senha_valida.place(x=410, y=55, width=210, height=30)
    else:
        lbl_senha_valida.config(text="Senha acima de 7 caracteres ",fg='red')
        lbl_senha_valida.place(x=410, y=55, width=210, height=30)


janela = tk.Tk()

janela.title('Interface de Login')
janela.geometry('620x200')

lbl_usuario = tk.Label(janela, text="Email:", font=("Arial", 15))
lbl_usuario.place(x=0, y=0, width=100, height=50)

entry_usuario = tk.Entry(janela, width=50)
entry_usuario.place(x=100, y=5, width=300, height=30)

lbl_senha = tk.Label(janela, text="Senha:", font=('Arial', 15))
lbl_senha.place(x=0, y=50, width=100, height=50)

entry_senha = tk.Entry(janela, show="*", width=50)
entry_senha.place(x=100, y=55, width=300, height=30)

btn_converter = tk.Button(janela, text='Login',font=("Arial", 12),fg='black', command=valida_email_senha)
btn_converter.place(x=100, y=100, width=100, height=50)  

janela.mainloop()
