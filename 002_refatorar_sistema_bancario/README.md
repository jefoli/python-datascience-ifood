# 02º Desafio - Otimizando o sistema bancário com Funções Python

**Fase do projeto:** ✅ *Iniciado* | 🔄 *Em desenvolvimento* | 🔜 *concluído*


## Objetivo Geral

- Refatoração do primeiro desafio utilizando funções.
- Exercitar o que foi lecionado durante o curso.
- Separar as funções existentes de saque, depósito e extrato em funções.
- Criar duas novas funções:
- cadastrar usuário (cliente).
- Cadastrar conta bancária.
    

## Desafio

- Precisamos deixar nosso código mais modularizado.
- ***Será necessário criar funções para as operações existentes:***
    - sacar.
    - depositar.
    - visualizar extrato.
- ***Criar duas novas funções:***
    - Usuário (cliente do banco).
    - Criar conta corrente (vincular com o usuário).

## Separação em funções

- Deverá criar funções para todas as operações do sistema.
- Cada função deverá ter uma regra na passagem de argumentos (por posição e argumentos nomeados).
- O retorno e a forma como serão chamadas poderá ser definida a critério do desenvolvedor.

### Função Saque

- A função saque deverá recevber os argumentos apenas por nome (***keyword only***).
- **Sugestão de argumentos**: *saldo (saldo=saldo), valor(valor=valor), extrato, limite, numero_saques, limite_saques.*
- Sugestão de retorno: **saldo e extrato.**

### Função Depósito

- A função depósito deve receber os argumentos apenas por posição (***positional only**)*
- Sugestão de argumentos: ***saldo, valor, extrato.**
- Sugestão de retorno: saldo e extrato.

### Função Extrato

- A função extrado deve receber por posição e nome ***positional only e keyword only**).*
- Sugestão de argumento posicionais: ***saldo.***
- Sugestão de argumento nomeados: ***extrato.***

### Novas Funções

- Precisamos criar duas novas funções:
    - **Criar usuário.**
    - **Criar conta corrente.**
    - Observação: *Fica a critério do desenvolvedor adicionar mais funções, como por exemplo : listar contas.*
    
#
## Requisitos funcionais e regras de negócio

### Função criar usuário (cliente)

- O programa deve armazenar o usuário em uma ***lista***.
- Um usuário é composto por:
    - **Nome.**
    - **Data de nascimento.**
    - **CPF:**
        - Deve ser armazenado somente os números do CPF.
        - Não podemos cadastrar 2 usuários com o mesmo CPF.
    - **Endereço:**
        - Endereço é uma ***string*** com o formato:
            - **Logradouro.**
            - **Número.**
            - **Bairro.**
            - **Cidade/Sigla Estado.**

### Função criar conta corrente

- O programa deve armazenar em uma ***lista.***
- Uma conta corrente será composta por:
    - **Agência**.
    - Número da conta:
        - Número da agência é fixo: 0001.
    - **Usuário da conta**
        - Usuário pode ter mais de uma conta.
        

## Dica

- Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.