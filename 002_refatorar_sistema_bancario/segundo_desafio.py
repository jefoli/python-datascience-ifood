import datetime

CURRENT_DATE = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
CLIENTE_MENU = """Faça o seu cadastro/login:\n[1] Novo cliente\n[] Cliente Existente\n=> """
MENU = """Escolha uma das opções abaixo:\n[c] Cadastrar Cliente\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> """
LIMITE_SAQUES = 3
MSG_ADVICE = f"Consulte seu gerente para mais informações.\n"

saldo = 0
numero_saque = 0
extrato = []

# func deposito
def deposito(valor_dep):
    val_saldo = saldo
    if valor_dep <= 0:
        print("Valor inválido. Tente novamente!\n")
    else:
        val_saldo += valor_dep
        print("Depósito realizado com sucesso!\n")
        extrato.append(valor_dep)
    return val_saldo

# func saque
def saque(valor_saq):
    global saldo, numero_saque
    limite = 500
    if valor_saq <= 0:
        print("Valor inválido!")
        return
    elif valor_saq > limite:
        print(f"\nO valor informado excede o o limite disponível para essa conta.\nLimite de valor por saque R$: {limite:.2f}!")
        print(MSG_ADVICE)
        return
    elif valor_saq > saldo:
        print("Você não possui saldo suficiente para esta operação!\n")
    elif numero_saque >= 3:
        print(f"\nLimite de operações excedidas para este tipo de conta!\nQuantidade de saques disponíveis para essa conta: {LIMITE_SAQUES} (três).")
        print(MSG_ADVICE)
        return
    else:
        saldo = saldo - valor_saq
        numero_saque += 1
        extrato.append(valor_saq)
        print(f"Operação realizada com sucesso!\n")
    return

# func extrato
def extratos(extratos):
    if extratos == "":
        print("Não foram realizadas movimentações. ")
    else:
        print(f"Extrato consolidado:\n\n{extratos}\nSaldo total R$: {saldo:.2f}")
    return

#func cadastrar_cliente
def cadastrar_clientes(cli):
    AGENCIA = "Agência: 0001"
    conta = "Conta:  0001"
    cli = clientes
    nome = input("Digite seu nome: ")
    sobrenome = input ("Digite seu sobrenome: ")
    cpf = input ("Digite seu cpf: ")
    cli.append([AGENCIA,conta, nome, sobrenome, cpf])
    return cli

def criar_conta():
    AGENCIA = "Agência: 0001"
    conta = "Conta:  0001"


print("Bem-vindo ao BTG Pactual!\n")
while True:
    opcao = input(MENU)
    match opcao:
        case "c" | "C":
            clientes = []
            cont_client = cadastrar_clientes(clientes)
            for cl in clientes:
                print(cl, clientes)
        case "d" | "D":
            valor_dep = int(input(f"Informe o valor que deseja depositar R$: "))
            recebe_saldo = deposito(valor_dep)
            saldo = recebe_saldo
        case "s" | "S":
            valor_saq = int(input(f"Informe o valor que deseja sacar R$: "))
            saque(valor_saq)
        case "e" | "E":
            extratos(extrato)
        case "q" | "Q":
            print(f"O banco BTG agradece a sua parceria!\nVolte sempre!")
            break
        case other:
            print("Operação inválida, por favor selecione novamente a operação desejada.\n")