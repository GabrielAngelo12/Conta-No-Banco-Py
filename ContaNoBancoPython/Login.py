from getpass import getpass
from Menu import Menu

menu = Menu()

class Conta:
    def __init__(self):
        self.nome = None
        self.senha = None
        self.cpf = None
    
    def criar_conta(self):
        self.nome = input("Digite seu NOME: ")
        self.senha = getpass("Digite a SENHA: ")
        senha2 = getpass("CONFIRME A SENHA: ")
        self.cpf = input("Digite seu CPF: ")
        
        if len(self.cpf) != 11:
            print("CPF inválido! O CPF deve ter 11 dígitos.")
            self.criar_conta()
            return
        
        if self.senha == senha2:
            with open('arquivo.txt', 'w') as arquivo:
                arquivo.write(f"NOME: {self.nome}\n")
                arquivo.write(f"SENHA: {self.senha}\n")
                arquivo.write(f"CPF: {self.cpf}\n")
            print("\nConta criada com sucesso!")
            self.login()
        else:
            print("Erro! Senhas não coincidem. Voltando ao início...\n")
            self.criar_conta()
    
    def login(self):   
        print("\nFaça login")
        self.nome2 = input("Digite seu NOME: ")
        self.senhaL = getpass("Digite a SENHA: ")
        self.cpf2 = input("Digite seu CPF: ")
        
        if len(self.cpf2) != 11:
            print("CPF inválido! O CPF deve ter 11 dígitos.")
            self.login()
            return
        
        with open('arquivo.txt', 'r') as arquivo:
            dados = arquivo.readlines()
            nome_salvo = dados[0].split(":")[1].strip()
            senha_salva = dados[1].split(":")[1].strip()
            cpf_salvo = dados[2].split(":")[1].strip() 
        
        if self.nome2 == nome_salvo and self.senhaL == senha_salva and self.cpf2 == cpf_salvo:
            print("\nLogin realizado com sucesso!")
            menu.escolher_opcao()
        else:
            print("Dados incorretos! Tente novamente.")
            self.login()
