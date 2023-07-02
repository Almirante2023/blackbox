import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Função para abrir a segunda janela em uma nova aba
def abrir_segunda_janela():
    janela_segunda_aba = customtkinter.CTk()
    janela_segunda_aba.geometry("600x300")

    texto2 = customtkinter.CTkLabel(janela_segunda_aba, text="Coletar Dados")
    texto2.pack(padx=10, pady=10)

    cpf = customtkinter.CTkEntry(janela_segunda_aba, placeholder_text="Seu CPF")
    cpf.pack(padx=10, pady=10)

    cidade = customtkinter.CTkEntry(janela_segunda_aba, placeholder_text="Sua cidade")
    cidade.pack(padx=10, pady=10)

    telefone = customtkinter.CTkEntry(janela_segunda_aba, placeholder_text="Seu telefone")
    telefone.pack(padx=10, pady=10)

    botao_entrar = customtkinter.CTkButton(janela_segunda_aba, text="Entrar", command=clique_segunda_tela)
    botao_entrar.pack(padx=10, pady=10)

    janela_segunda_aba.mainloop()

def clique_segunda_tela():
    print("Botão 'Entrar' clicado")

# Janela principal
janela = customtkinter.CTk()
janela.geometry("600x300")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

def clique():
    abrir_segunda_janela()  # Chama a função para abrir a segunda janela em uma nova aba

cidade = customtkinter.CTkEntry(janela, placeholder_text="Sua cidade")
cidade.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
