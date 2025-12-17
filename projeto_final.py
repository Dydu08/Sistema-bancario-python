# Sistema bancário
import random
import os

# Armazenamento dos dados das contas
Nomes = []
CPFs = []
Data_nsc = []
Est_civ = []
Emails = []
Senhas = []

# Armazenamento dos dados bancários
Num_conta = []
Extrato = []

# Criação da conta
def criar_nova_conta(nome, cpf, data, est_civ, email, senha, num_conta, extrato):
    Nomes.append(nome)
    CPFs.append(cpf)
    Data_nsc.append(data)
    Est_civ.append(est_civ)
    Emails.append(email)
    Senhas.append(senha)
    Num_conta.append(num_conta)
    Extrato.append(extrato)

# Função de investimentos
def aplicar_investimento(valor, indice_conta_inv):
    renda = valor * 0.05
    print(f'Seu rendimento anual estimado será de: R${renda:.2f}')
    Extrato[indice_conta_inv] -= valor
    pausar()

# Função bancária
def funcao_bancaria_principal(indice_conta):
    while True:
        limpar_tela()
        print(f'|=========[MENU BANCÁRIO]=========|')
        print('|Digite [1] para verificar o seu extrato')
        print('|Digite [2] para realizar um depósito na sua conta')
        print('|Digite [3] para realizar um saque')
        print('|Digite [4] para realizar uma transferência ')
        print('|Digite [5] para realizar um investimento')
        print('|Digite [6] para verificar os dados da sua conta')
        print('|Digite [0] para sair da sua conta')
        opcao_menu_bank = input('-> ')
        
        limite = 1000

        match opcao_menu_bank:

            case '1':
                limpar_tela()
                print('|===============[EXTRATO]===============|')
                print(f'O extrato do cliente {Nomes[indice_conta]} é: R${Extrato[indice_conta]:.2f}')
                pausar()
            
            case '2':
                while True:
                    limpar_tela()
                    print('|===============[DEPÓSITO]===============|')
                    print(f'Sua conta atualmente possui: R${Extrato[indice_conta]:.2f}\n'+ '='*41)
                    valor_deposito = float(input('Digite o valor que deseja depositar na sua conta: '))
                    if valor_deposito > 0:
                        limpar_tela()
                        Extrato[indice_conta] += valor_deposito
                        print('Depósito realizado com sucesso!\n' + '='*41)
                        print(f'Seu extrato após a movimentação é: R${Extrato[indice_conta]:.2f}')
                        pausar()
                        break
                    else:
                        print('Você digitou um valor inválido. Tente novamente')
                        pausar()

            case '3':
                while True:
                    limpar_tela()
                    print('|===============[SAQUE]===============|')
                    print(f'Sua conta atualmente possui: R${Extrato[indice_conta]:.2f}\n'+ '='*41)
                    valor_saque = float(input('Digite o valor que deseja sacar da sua conta: '))
                    if valor_saque <= Extrato[indice_conta]:
                        if valor_saque <= limite:
                            if valor_saque > 0:
                                limpar_tela()
                                Extrato[indice_conta] -= valor_saque
                                print('Saque realizado com sucesso!')
                                print(f'Seu extrato após a movimentação é: R${Extrato[indice_conta]:.2f}')
                                pausar()
                                break
                            else:
                                print('Você digitou um valor inválido. Tente novamente.\n'+ '='*41)
                                pausar()
                        else:
                            print(f'='*41 + '\nA quantidade que você deseja sacar ultrapassa o limite de saque único de R${limite:.2f}. Tente novamente')
                            pausar()
                    else:
                        print('O valor do saque ultrapassou o extrato atual. Tente novamente.')
                        pausar()

            case '4':
                while True:
                    limpar_tela()
                    print('|===============[TRANSFERÊNCIA]===============|')
                    numero_conta_destino = int(input('Digite o número da conta para qual você quer transferir: '))
                    print('='*41)
                    if numero_conta_destino in Num_conta and numero_conta_destino != Num_conta[indice_conta]:
                        indice_destino = Num_conta.index(numero_conta_destino)
                        
                        print(f'A conta digitada pertence à {Nomes[indice_destino]}\n' + '='*41)
                        
                        valor_transferencia = float(input('Digite o valor que deseja transferir: '))
                        
                        if valor_transferencia <= Extrato[indice_conta]:
                            while True:
                                if valor_transferencia > 0:
                                    limpar_tela()
                                    Extrato[indice_conta] -= valor_transferencia
                                    Extrato[indice_destino] += valor_transferencia
                                    print('A transferência foi realizada com sucesso!\n' + '='*41)
                                    print(f'Seu saldo após a movimentação: {Extrato[indice_conta]:.2f}')
                                    pausar()
                                    break
                                else:
                                    print('Você digitou um valor inválido. Tente novamente')
                                    pausar()
                            break
                        else:
                            print('Você não possui saldo suficiente na sua conta.')
                            pausar()
                            break
                    else:
                        print('O número da conta digitado não é valido. Tente novamente.')
                        pausar()

            case '5':
                while True:
                    limpar_tela()
                    print('|===========[Painel de investimentos]===========|')
                    print('|>Investimento em renda passiva')
                    print('|>Rendimento de 5% no ano')
                    valor_invest = float(input('|Digite o valor que deseja investir -> '))
                    print('='*41)
                    if Extrato[indice_conta] >= valor_invest:
                        if valor_invest > 0:
                            aplicar_investimento(valor_invest, indice_conta)
                            break
                        else:
                            print('Você digitou um valor inválido.')
                            pausar()
                    else:
                        print('Você não possui saldo suficiente.')
                        pausar()
                        break

            case '6':
                limpar_tela()
                print('|===========[Dados da conta]===========|')
                print(f'|Nome: {Nomes[indice_conta]}')
                print(f'|CPF: {CPFs[indice_conta]}')
                print(f'|Idade: {2025 - Data_nsc[indice_conta]}')
                print(f'|Estado civil: {Est_civ[indice_conta]}')
                print(f'|Email: {Emails[indice_conta]}')
                print(f'|Número da conta: {Num_conta[indice_conta]}')
                pausar()
            
            case '0':
                print('Saindo...')
                pausar()
                break
        
            case _:
                print('Você digitou um número inválido. Tente novamente.')
                pausar()

def limpar_tela():
    os.system('cls')

def pausar():
    input('[ENTER] para continuar...')

# Menu de cadastro
while True:
    limpar_tela()
    
    print('|=========[MENU DE ENTRADA]=========|')
    print('|Digite [1] para logar em uma conta |')
    print('|Digite [2] para criar uma conta    |')
    print('|Digite [0] para sair               |')
    print('|===================================|')
    opcao_menu = input('-> ')
    
    match opcao_menu:
        case '1':
            limpar_tela()
            print('|============[Login]============|')
            
            email = input('Email: ')
            if email in Emails:
                while True:
                    senha = input('Senha: ')
                    posicao = Emails.index(email)
                    
                    if senha == Senhas[posicao]:
                        limpar_tela()
                        print(f'[Bem-vindo {Nomes[posicao]}!]')
                        pausar()
                        break
                    else:
                        print('='*34 + '\nSenha incorreta! Tente novamente.\n' + '='*34)
                
                funcao_bancaria_principal(posicao)
            
            else:
                limpar_tela()
                print('Email não cadastrado no sistema.')
                pausar()

        case '2':
            limpar_tela()
            print('|===== [Nova conta] =====|\n')
            
            novo_nome = input('Informe o seu nome: ')
            
            while True:
                novo_cpf = input('Informe o seu CPF: ')
                if novo_cpf in CPFs:
                    print('='*34 + '\nCPF já cadastrado! Tente outro.\n' + '='*34)
                else:
                    break
            
            novo_nasce = int(input('Informe o seu ano de nascimento: '))
            
            novo_estad_civ = input('Informe o seu estado civil: ')
            
            while True:
                novo_email = input('Cadastre um e-mail: ')
                if novo_email in Emails:
                    print('='*34 + '\nE-mail já cadastrado! Tente outro.\n' + '='*34)
                else:
                    break
            
            nova_senha = input('Cadastre uma senha: ')
            
            while True:
                novo_num_conta = random.randint(1000, 9999)
                if novo_num_conta not in Num_conta:
                    break
            
            novo_extrato = float(0)        

            criar_nova_conta(novo_nome, novo_cpf, novo_nasce, novo_estad_civ, novo_email, nova_senha, novo_num_conta, novo_extrato)
            
            limpar_tela()
            print('Conta criada com sucesso!\n' + '='*34)
            print(f'O número da sua conta é {novo_num_conta}\n' + '='*34)
            print('Você pode verificá-lo novamente ao logar na sua conta.')
            pausar()

        case '0':
            print('Saindo...')
            break
        
        case _:
            print('Opção inválida!')
            pausar() 