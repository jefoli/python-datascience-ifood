import datetime

CURRENT_DATE = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
CLIENTE_MENU = """Faça o seu cadastro/login:\n[1] Novo cliente\n[] Cliente Existente\n=> """
MENU = """Escolha uma das opções abaixo:\n[c] Cadastrar Cliente\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> """
LIMITE_SAQUES = 3
MSG_ADVICE = f"Consulte seu gerente para mais informações."

clientes = []
extrato = []
quantidade_saques = 0
saldo = 0

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
    criar_conta_corrente = criar_conta()
    clientes.append({'nome':nome, 'sobrenome':sobrenome, 'CPF':cpf, **endereco, 'conta bancária' : {**criar_conta_corrente}})
    return True

def criar_conta():
    AGENCIA = '0001'
    conta = '0001'
    conta_corrente = {'Agência':AGENCIA, 'Conta corrente:': conta}
    return conta_corrente


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

def checar_limite_saque(qtd_saque):
    numeros_saque = qtd_saque
    
    if numeros_saque >= LIMITE_SAQUES:
        print(f'\nLimite de operações excedidas para este tipo de conta!\n'
            f'Quantidade de saques disponíveis para essa conta: {LIMITE_SAQUES} (três).')
        print(MSG_ADVICE)
        return False
    return True

def saque(valor):
    valor_saldo = saldo
    limite = 500
    global quantidade_saques

    checar_qtd_saque = checar_limite_saque(quantidade_saques)

    if checar_qtd_saque == False:
        return valor_saldo

    if valor <= 0:
        print("Valor inválido!")
        return valor_saldo
    
    if valor > valor_saldo:
        print("Você não possui saldo suficiente para esta operação!\n")
        return valor_saldo
        
    if valor > limite:
        print(f"\nO valor informado excede o o limite disponível para essa conta.\nLimite de valor por saque R$: {limite:.2f}!")
        print(MSG_ADVICE)
        return valor_saldo
    
    quantidade_saques += 1
    valor_saldo -= valor
    extrato.append(valor_saque)

    print(f"Operação realizada com sucesso!\n")
    return valor_saldo

# func extrato
def extratos(extrato):
    print('Extrato consolidado:')
    for valor in extrato:
        print('Operação: R$:', valor)
    print('Saldo total R$:', saldo)
    return True

def checar_entrada_valores(valor):
    entrada_valor = valor
    analisar_entrada = entrada_valor.isdigit() 
    
    if not analisar_entrada:
        return False
    return entrada_valor

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

            if checar_valor_deposito:
                valor_entrada = deposito(int(valor_para_deposito))
                saldo = valor_entrada
            else:
                print('Digite somente números!')
            print()
        case "s" | "S":
            valor_saque = input(f"Informe o valor que deseja sacar R$: ")
            checar_valor_saque = checar_entrada_valores(valor_saque)

            if checar_valor_saque:
                valor_saida = saque(int(valor_saque))
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