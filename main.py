import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import *


def Entrar():
    login = entry_login.get()
    senha = entry_senha.get()

    if not(login == "v.victor" and senha == "123"):
        label_erro_login.configure(text="Credenciais incorretas!",text_color='red')

    else:
        label_erro_login.configure(text="Logado!",text_color='green')


Janela_Login = ctk.CTk()
janela_x = 400
janela_y = 235
Janela_Login.geometry(f"{janela_x}x{janela_y}")
Janela_Login.resizable(False, False)
Janela_Login.title("Sug-Flora Login")
Janela_Login._set_appearance_mode('light')


icon_logo = PhotoImage(file="Logo-sug.png")
# Obtendo a largura e altura da imagem
width = icon_logo.width()
height = icon_logo.height()
# Definindo a largura e altura da label
label_width = 200
label_height = 200
# Verificando se a imagem precisa ser redimensionada
if width > label_width or height > label_height:
    # Redimensionando a imagem para caber dentro da label
    scale = min(label_width/width, label_height/height)
    icon_logo = icon_logo.subsample(round(1/scale), round(1/scale))

frame_login = ctk.CTkFrame(Janela_Login,width=janela_x-20,height=janela_y-20).place(x=10,y=10)

logo = Label(Janela_Login,image=icon_logo,width=label_width,height=label_height).place(x=15,y=15)

label_login = ctk.CTkLabel(Janela_Login,text="Bem vindo ao Sug-Flora",fg_color="grey85").place(x=label_width+37,y=30)
entry_login = ctk.CTkEntry(Janela_Login,placeholder_text="Insira seu E-mail")
entry_login.place(x=label_width+35,y=55)
entry_senha = ctk.CTkEntry(Janela_Login,placeholder_text="Insira sua senha",show="*")
entry_senha.place(x=label_width+35,y=85)
label_erro_login = ctk.CTkLabel(Janela_Login, text='', fg_color="grey85")
label_erro_login.place(x=label_width + 40, y=175)
btn_logar = ctk.CTkButton(Janela_Login,text="Entrar",fg_color='green',command=Entrar).place(x=label_width+35,y=115)
btn_cadastrar = ctk.CTkButton(Janela_Login,text="Cadastrar",fg_color='blue').place(x=label_width+35,y=145)


Janela_Login.mainloop()