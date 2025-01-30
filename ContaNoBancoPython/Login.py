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
        
        if len(self.cpf) == 11 :
            return self.cpf
        else:
            print("CPF inválido! O CPF deve ter 11 dígitos")
            self.criar_conta()
            
        if self.senha == senha2:
            with open('arquivo.txt', 'w') as arquivo:
                arquivo.write(f"NOME: {self.nome}\n")
                arquivo.write(f"SENHA: {self.senha}\n")
                arquivo.write(f"CPF: {self.cpf}\n")
            print("\nConta criada com sucesso!")
            self.login()
        else:
            print("Erro! Senhas não coincidem. Voltando ao início...")
            self.criar_conta()
    
    def login(self):
        print("\nFaça login")
        nome2 = input("Digite seu NOME: ")
        senhaL = getpass("Digite a SENHA: ")
        cpf2 = input("Digite seu CPF: ")
        
        if len(self.cpf2) == 11 :
            return self.cpf2
        else:
            print("CPF inválido! O CPF deve ter 11 dígitos")
            self.login()
            
        with open('arquivo.txt', 'r') as arquivo:
            dados = arquivo.readlines()
            nome_salvo = dados[0].split(":")[1].strip()
            senha_salva = dados[1].split(":")[1].strip()
            cpf_salvo = int(dados[2].split(":")[1].strip())
            
        if nome2 == nome_salvo and senhaL == senha_salva and cpf2 == cpf_salvo:
            print("\nLogin realizado com sucesso!")
            menu.escolher_opcao()
            
        else:
            print("Dados incorretos! Tente novamente.")
            self.login()  
            
