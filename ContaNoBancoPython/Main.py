from Login import Conta
import sys

conta = Conta()

opcaoInicial = int(input("\nDigite uma opção:\n1 - Fazer Login\n2 - Criar Conta\n3 - Sair\n"))
match opcaoInicial:
    case 1 :
        conta.login()
    
    case 2 :
        conta.criar_conta()
    
    case 3 :
        sys.exit()

