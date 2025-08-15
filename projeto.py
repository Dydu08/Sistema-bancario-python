#Sistema bancario
import os

#Armazenamento dos dados
Nomes = []
CPFs = []
Data_nsc =[]
Est_civ = []
Emails = []
Senhas = []


#Criação da conta
def criar_nova_conta(nome, cpf, data, est_civ, email, senha):
    Nomes.append(nome)
    CPFs.append(cpf)
    Data_nsc.append(data)
    Est_civ.append(est_civ)
    Emails.append(email)
    Senhas.append(senha)


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