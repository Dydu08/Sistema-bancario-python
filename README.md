  [![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Terminal](https://img.shields.io/badge/CLI-Terminal-black?style=for-the-badge&logo=windows-terminal&logoColor=white)]()
  [![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)](https://opensource.org/licenses/MIT)
  [![Bugs](https://img.shields.io/badge/Bugs-Inclusos_de_Graça-red?style=for-the-badge)]()

# Python CLI Bank 🏦

Sistema bancário via terminal (Command Line Interface), desenvolvido inteiramente em Python. Este projeto simula as operações fundamentais de uma instituição financeira, permitindo a criação de contas, autenticação de usuários e movimentações bancárias como depósitos, saques, transferências e investimentos. 

📚 **O "Primeiro Projeto":** Desenvolvido como o primeiro contato prático com programação, com foco no aprendizado de lógica de programação, estruturas de repetição, condicionais e manipulação de arrays (listas) em Python puro, sem uso de bibliotecas externas de persistência.

## ✨ Funcionalidades

**Autenticação e Cadastro**
* Cadastro de nova conta com captura de dados (Nome, CPF, Ano de nascimento, Estado civil, E-mail e Senha).
* Geração automática e aleatória de número de conta (4 dígitos).
* Sistema de login baseado em E-mail e Senha.

**Operações Bancárias**
* **Extrato:** Consulta em tempo real do saldo da conta.
* **Depósito:** Adição de saldo com validação de valores positivos.
* **Saque:** Retirada de valores com verificação de saldo em conta e teto de limite por operação (R$ 1.000,00).
* **Transferência:** Envio de valores para outros usuários cadastrados no sistema, validando a existência da conta destino e o saldo do remetente.
* **Investimentos:** Simulação de aplicação financeira com projeção de rendimento de 5% (renda passiva).

**Gerenciamento de Conta**
* Visualização completa do perfil do cliente (cálculo de idade dinâmica, CPF, E-mail, etc.).
* Navegação via menu interativo com limpeza automática de tela (Clear Screen) para melhor UX no terminal.

## 💡 O que este projeto demonstra

* **Lógica de Programação:** Uso intensivo de controle de fluxo (`while`, `if/else`, `match/case`).
* **Estrutura de Dados Básica:** Utilização de listas paralelas globais para gerenciamento de estado e simulação de banco de dados em memória.
* **Interação com Usuário (I/O):** Captura e formatação de dados no terminal, blindando entradas básicas.
* **Modularidade Básica:** Separação de escopo através de funções customizadas (ex: `criar_nova_conta`, `funcao_bancaria_principal`, `limpar_tela`).

## 🛠️ Tecnologias utilizadas

* Python (Versão 3.10+)
* Bibliotecas nativas: `os` (manipulação do terminal) e `random` (geração de identificadores).
* Paradigma Procedural estruturado.

## 📁 Estrutura do projeto

```text
python-cli-bank/
└── main.py          # Arquivo único contendo a lógica de menus, funções e variáveis globais
