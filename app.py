import customtkinter as ctk

ctk. set_appearance_mode('dark')

app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criar função
def login_valid():
    usuario = entry_user.get()
    senha = entry_senha.get()

    if usuario == 'Rafael' and senha == '2307':
        resultado_login.configure(text='Login feito com sucesso',
        text_color='green')
    else:  
        resultado_login.configure(text='Usuário ou senha incorretos',
        text_color='red')





#label

label_user = ctk.CTkLabel(app, text='Usuário')
label_user.pack(pady=10)

#entry 
entry_user = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
entry_user.pack(pady=10)

#label

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

#entry 
entry_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha')
entry_senha.pack(pady=10)

#button 
botao_login = ctk.CTkButton(app, text='Login', command=login_valid)
botao_login.pack()



#Funçao login 
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack()





app.mainloop()