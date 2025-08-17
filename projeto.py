#Sistema bancario
import os

#Armazenamento dos dados
Nomes = []
CPFs = []
Data_nsc =[]
Est_civ = []
Emails = []
Senhas = []
Saldos = []
Extratos = []
NumeroSaques = []

# Limites bancários
LIMITE = 500
LIMITE_SAQUES = 2


def criar_nova_conta(nome, cpf, data, est_civ, email, senha):
    Nomes.append(nome)
    CPFs.append(cpf)
    Data_nsc.append(data)
    Est_civ.append(est_civ)
    Emails.append(email)
    Senhas.append(senha)
    Saldos.append(0.0)           
    Extratos.append("")       
    NumeroSaques.append(0)       
                                

def limpar_tela():
    os.system('cls')


def pausar():
    input('[ENTER] para continuar...')


# Menu bancário (depois do login)
def menu_banco(usuario):
    while True:
        limpar_tela()
        menu = f"""
        |===== [BANCO - {Nomes[usuario]}] =====|
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [f] Sair da conta
        => """
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                Saldos[usuario] += valor
                Extratos[usuario] += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

            pausar()

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeuSaldo = valor > Saldos[usuario]
            excedeuLimite = valor > LIMITE
            excedeuSaques = NumeroSaques[usuario] >= LIMITE_SAQUES

            if excedeuSaldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeuLimite:
                print("Operação falhou! O valor do saque excedeu o limite.")
            elif excedeuSaques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                Saldos[usuario] -= valor
                Extratos[usuario] += f"Saque:    R$ {valor:.2f}\n"
                NumeroSaques[usuario] += 1
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

            pausar()

        elif opcao == "e":
            print(f"\n ======== EXTRATO {Nomes[usuario]} ==========")
            print("Não foram realizadas movimentações."
                  if not Extratos[usuario] else Extratos[usuario])
            print(f"\nSaldo: R$ {Saldos[usuario]:.2f}")
            print("=========================================")
            pausar()

        elif opcao == "f":
            print("Saindo da conta...")
            pausar()
            break

        else:
            print("Operação inválida! Selecione a opção correta.")
            pausar()


#Menu inicial de cadastro
while True:
    limpar_tela()
    
    print('|=========[MENU DE ENTRADA]=========|')
    print('|Digite [1] para logar em uma conta |')
    print('|Digite [2] para criar uma conta    |')
    print('|Digite [0] para sair               |')
    print('|===================================|')
    iniciacao = int(input('-> '))
    
    
    match iniciacao:
        case 1:
            limpar_tela()
            print('|===== [Login] =====|\n')
            
            email = input('Email: ')
            if email in Emails:
                while True:
                    senha = input('Senha: ')
                    pos = Emails.index(email)
                    
                    if senha == Senhas[pos]:
                        limpar_tela()
                        print(f'[Bem vindo {Nomes[pos]}!]')
                        pausar()
                        break
                    else:
                        print('='*34 + '\nSenha incorreta! Tente novamente.\n' + '='*34)
                
                #Colocar a função aqui
            else:
                limpar_tela()
                print('Email não cadastrado no sistema.')
                pausar()

        
        case 2:
            limpar_tela()
            print('|===== [Nova conta] =====|\n')
            
            novo_nome = input('Informe o seu nome: ')
            while True:
                novo_cpf = input ('informe o seu CPF: ')
                if novo_cpf in CPFs:
                    print('='*34 + '\nCPF já cadastrado! Tente outro.\n' + '='*34)
                else:
                    break
            novo_nasce = input('Informe o seu ano de nascimento: ')
            novo_estad_civ = input('Informe o seu estado civil: ')
            while True:
                novo_email = input('Cadastre um email: ')
                if novo_email in Emails:
                    print('='*34 + '\nEmail já cadastrado! Tente outro.\n' + '='*34)
                else:
                    break
            nova_senha = input('Cadastre uma senha: ')
            criar_nova_conta(novo_nome, novo_cpf, novo_nasce, novo_estad_civ, novo_email, nova_senha)
            
            limpar_tela()
            print('Conta criada com sucesso!')
            pausar()

        
        case 0:
            print('Saindo...')
            break
        
        
        case _:
            print('Opção inválida!')
            pausar() 
