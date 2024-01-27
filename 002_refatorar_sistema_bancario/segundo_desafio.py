import datetime
import os

CURRENT_DATE = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
CLIENTE_MENU = """Faça o seu cadastro/login:\n[1] Novo cliente\n[] Cliente Existente\n=> """
MENU = """Escolha uma das opções abaixo:\n[c] Cadastrar Cliente\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> """
LIMITE_SAQUES = 3
MSG_ADVICE = f"Consulte seu gerente para mais informações.\n"

saldo = 0
numero_saque = 0
extrato = []
clientes = []


def registrar_endereco():
    rua = input('Informe a rua: ')
    numero_residencia = input('Informe o número da residência: ')
    bairro = input('Informe o bairro: ')
    cidade = input('Informe a cidade: ')
    cep = input('Informe o CEP: ')
    endereco_completo = {'Rua': rua, 'Número:': numero_residencia, 'Bairro:': bairro, 'Cidade':cidade, 'CEP:':cep}
    return endereco_completo

def cadastrar_clientes():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    cpf = input("Digite seu CPF: ")
    endereco = registrar_endereco()
    clientes.append({'nome':nome, 'sobrenome':sobrenome, 'CPF':cpf, **endereco})
    return True

def criar_conta():
    AGENCIA = "Agência: 0001"
    conta = "Conta:  0001"

# func deposito
def deposito(valor_deposito):
    valor_digitado = valor_deposito

    val_saldo = saldo
    if valor_digitado <= 0:
        print("Valor inválido. Tente novamente!\n")
    val_saldo += valor_digitado
    print("Depósito realizado com sucesso!\n")
    extrato.append(valor_digitado)
    return val_saldo

# func saque
def saque(valor):
    global numero_saque
    valor_saldo = saldo
    limite = 500
    if valor <= 0:
        print("Valor inválido!")
        return
    elif valor > limite:
        print(f"\nO valor informado excede o o limite disponível para essa conta.\nLimite de valor por saque R$: {limite:.2f}!")
        print(MSG_ADVICE)
        return
    elif valor > valor_saldo:
        print("Você não possui saldo suficiente para esta operação!\n")
    elif numero_saque >= 3:
        print(f"\nLimite de operações excedidas para este tipo de conta!\nQuantidade de saques disponíveis para essa conta: {LIMITE_SAQUES} (três).")
        print(MSG_ADVICE)
        return
    else:
        numero_saque += 1
        extrato.append(valor_saque)
        valor_saldo -= valor
        print(f"Operação realizada com sucesso!\n")

    return valor_saldo

# func extrato
def extratos(extrato):
    print('Extrato consolidado:')
    for valor in extrato:
        print('Operação: R$:', valor)
    print(f"Saldo total R$: {saldo:.2f}\n")
    return True

def checar_entrada_valores(valor):
    entrada_valor = valor
    analisar_entrada = entrada_valor.isdigit()
    
    if analisar_entrada:
        entrada_valor = int(entrada_valor)
        return entrada_valor
    
    return False

print("Bem-vindo ao BTG Pactual!\n")
while True:
    opcao = input(MENU)
    match opcao:
        case "c" | "C":
            nova_conta_bancaria = cadastrar_clientes()
            for cliente in clientes:
                print(cliente)
        case "d" | "D":
            valor_para_deposito = input(f"Informe o valor que deseja depositar R$: ")
            checar_valor_deposito = checar_entrada_valores(valor_para_deposito)

            if checar_valor_deposito != False:
                valor_entrada = deposito(checar_valor_deposito)
                saldo = valor_entrada
            else:
                print('Digite somente números!')
            print()

        case "s" | "S":
            valor_saque = input(f"Informe o valor que deseja sacar R$: ")
            checar_valor_saque = checar_entrada_valores(valor_saque)

            if checar_valor_saque != False:
                valor_saida = saque(checar_valor_saque)
                saldo = valor_saida
            else:
                print('Digite somente números!')
            print()

        case "e" | "E":
            extratos(extrato)
        case "q" | "Q":
            print(f"O banco BTG agradece a sua parceria!\nVolte sempre!")
            break
        case other:
            print("Operação inválida, por favor selecione novamente a operação desejada.\n")