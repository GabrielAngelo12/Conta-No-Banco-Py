import sys

class Menu :
    def __init__(self):
        self.opcao = None
        self.saldo = 0
        
    def escolher_opcao(self):
        while(self.opcao !=5):    
            self.opcao = int(input("\nEscolha uma opção:\n1 - Sacar\n2 - Depositar\n3 - Transferir\n4 - Consultar Saldo\n5 - Sair\n"))
        
            match self.opcao:
                case 1:
                    valorASacar = float(input("Digite o valor que deseja Sacar:"))
                    if valorASacar <= self.saldo:
                        self.saldo -= valorASacar
                        print("\nSeu saldo atual: ", self.saldo)
                    else:
                        print("Saldo insuficiente.")
                
                case 2:
                    valorADepositar = float(input("Digite o valor que deseja Depositar: "))
                    self.saldo += valorADepositar
                    print("\nSeu saldo atual: ", self.saldo)
                
                case 3:
                    valorATransferir = float(input("Digite o valor que deseja Transferir: "))
                    if valorATransferir < self.saldo:
                        nomeRecebedor = input("Digite o nome do recebedor: ")
                        self.saldo -= valorATransferir
                        print("Transferência realizada para ", nomeRecebedor,". \nSeu saldo atual: ", self.saldo)
                    else:
                        print("Saldo insuficiente para transferir.")
                           
                case 4:
                    print("\nSeu saldo atual: ", self.saldo)
                
                case 5:
                    sys.exit()
                