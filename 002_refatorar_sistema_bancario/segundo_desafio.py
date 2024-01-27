import datetime

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
    val_saldo = saldo
    if valor_deposito <= 0:
        print("Valor inválido. Tente novamente!\n")
    val_saldo += valor_deposito
    print("Depósito realizado com sucesso!\n")
    extrato.append(valor_deposito)
    return val_saldo

# func saque
def saque(valor_saque):
    global numero_saque
    valor_saldo = saldo
    limite = 500
    if valor_saque <= 0:
        print("Valor inválido!")
        return
    elif valor_saque > limite:
        print(f"\nO valor informado excede o o limite disponível para essa conta.\nLimite de valor por saque R$: {limite:.2f}!")
        print(MSG_ADVICE)
        return
    elif valor_saque > valor_saldo:
        print("Você não possui saldo suficiente para esta operação!\n")
    elif numero_saque >= 3:
        print(f"\nLimite de operações excedidas para este tipo de conta!\nQuantidade de saques disponíveis para essa conta: {LIMITE_SAQUES} (três).")
        print(MSG_ADVICE)
        return
    else:
        numero_saque += 1
        extrato.append(-valor_saque)
        print(f"Operação realizada com sucesso!\n")
        valor_saldo -= valor_saque
    return valor_saldo

# func extrato
def extratos(extrato):
    print('Extrato consolidado:')
    for valor in extrato:
        print(f'Operação: R$: {valor:.2f}')
    print(f"Saldo total R$: {saldo:.2f}\n")
    return True


print("Bem-vindo ao BTG Pactual!\n")
while True:
    opcao = input(MENU)
    match opcao:
        case "c" | "C":
            nova_conta_bancaria = cadastrar_clientes()
            for cliente in clientes:
                print(cliente)
        case "d" | "D":
            valor_dep = int(input(f"Informe o valor que deseja depositar R$: "))
            recebe_saldo = deposito(valor_dep)
            saldo = recebe_saldo
        case "s" | "S":
            valor_saq = int(input(f"Informe o valor que deseja sacar R$: "))
            sacar = saque(valor_saq)
            saldo = sacar
        case "e" | "E":
            extratos(extrato)
        case "q" | "Q":
            print(f"O banco BTG agradece a sua parceria!\nVolte sempre!")
            break
        case other:
            print("Operação inválida, por favor selecione novamente a operação desejada.\n")