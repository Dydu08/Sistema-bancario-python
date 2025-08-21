#Sistema bancario
import random
import os

#Armazenamento dos dados das contas
Nomes = []
CPFs = []
Data_nsc =[]
Est_civ = []
Emails = []
Senhas = []


#Armazenamento dos dados bancarios
Num_conta = []
Extrato = []


#Criação da conta
def criar_nova_conta(nome, cpf, data, est_civ, email, senha, num_conta, extrato):
    Nomes.append(nome)
    CPFs.append(cpf)
    Data_nsc.append(data)
    Est_civ.append(est_civ)
    Emails.append(email)
    Senhas.append(senha)
    Num_conta.append(num_conta)
    Extrato.append(extrato)
    

def funcao_bancaria_principal(posicao):
    while True:
        limpar_tela()
        print(f'|=========[Menu de {Nomes[posicao]} ]=========|')
        print('|Digite [1] para verificar o seu extrato')
        print('|Digite [2] para realizar um deposito na sua conta')
        print('|Digite [3] para realizar um saque')
        print('|Digite [4] para realizar uma transferencia ')
        print('|Digite [5] para realizar um investimento')
        print('|Digite [6] para verificar os dados da sua conta')
        print('|Digite [0] para sair da sua conta')
        inp = int(input('-> '))
        
        limite = 1000

        match inp:

            case 1:
                limpar_tela()
                print(f'O extrato do cliente {Nomes[posicao]} é: R${Extrato[posicao]}')
                pausar()
            
            case 2:
                while True:
                    limpar_tela()
                    print(f'Sua conta atualmente possui: R${Extrato[posicao]}')
                    dep = float(input('Digite o valor que deseja depositar na sua conta: '))
                    if dep > 0:
                        limpar_tela()
                        Extrato[posicao] += dep
                        print('Deposito realizado com sucesso!')
                        print(f'Seu extrato após a movimentação é: R${Extrato[posicao]}')
                        pausar()
                        break
                    else:
                        print('Você Digitou um valor invalido. Tente novamente')
                        pausar()

            case 3:
                while True:
                    limpar_tela()
                    
                    print(f'Sua conta atualmente possui: R${Extrato[posicao]}')
                    saque = float(input('Digite o valor que deseja sacar da sua conta: '))
                    if saque < Extrato[posicao]:
                        if saque < limite:
                            limpar_tela()
                            Extrato[posicao] -= saque
                            print('Saque realizado com sucesso!')
                            print(f'Seu extrato após a movimentação é: R${Extrato[posicao]}')
                            pausar()
                            break
                        else:
                            print(f'A quantidade que você deseja sacar ultrapassa o limite de saque unico de R${limite}')
                    else:
                        print('O valor do saque ultrapassou o valor do extrato atual. Tente novamente.')
                        pausar()


            case 4:
                while true:
                    limpar_tela()
                    tran_cont = int(input('Digite o número da conta para qual você quer realizar a tranferencia: '))
                    
                    if tran_cont in Num_conta:
                        tran_pos = Num_conta.index(tran_cont)
                        
                        print(f'A conta digitada pertence à {Nomes[tran_pos]}')
                        
                        tran_valor = float(input('Digite o valor que deseja tranferir: '))
                        
                        Extrato[posicao] -= tran_valor
                        
                        Extrato[tran_pos] += tran_valor

                        print(f'A transferencia foi realizada com suceso!\nSeu saldo atual é: {Extrato[posicao]}')
                        pausar()
                        break

                    else:
                        print('O número da conta digitado não esta regitrado. Tente novamente.')
            
            case 5:
            
            case 6:
                limpar_tela()
                print('|===========[Dados da conta]===========|')
                print(f'|Nome: {Nomes[posicao]}               |')
                print(f'|CPF: {CPFs[posicao]}                 |')
                print(f'|Idade: {2025 - Data_nsc[posicao]}    |')
                print(f'|Estado civil: {Est_civ[posicao]}     |')
                print(f'|Email: {Emails[posicao]}             |')
                print(f'|Senha: {Senhas[posicao]}             |')
                print(f'|Número da conta: {Num_conta[posicao]}|')
                pausar()
            
            case 0:
                print('Tem certeza que deseja deslogar?')
                pausar()
                break
        
            case _:
                print('Você digitou um número invalido. tente novamente.')
                pausar()
          

def limpar_tela():
    os.system('cls')


def pausar():
    input('[ENTER] para continuar...')


#Menu de cadastro
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
                
                funcao_bancaria_principal(pos)
            
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
            
            while True:
                novo_num_conta = random.randint(100000, 999999)
                if novo_num_conta not in Num_conta:
                    break
            
            novo_extrato = float(0)        

            criar_nova_conta(novo_nome, novo_cpf, novo_nasce, novo_estad_civ, novo_email, nova_senha, novo_num_conta, novo_extrato)
            
            limpar_tela()
            print('Conta criada com sucesso!')
            print(f'O número da sua conta é {novo_num_conta}')
            print('Você pode verifica-lo novamente ao logar na sua conta.')
            pausar()

        
        case 0:
            print('Saindo...')
            break
        
        
        case _:
            print('Opção inválida!')
            pausar()