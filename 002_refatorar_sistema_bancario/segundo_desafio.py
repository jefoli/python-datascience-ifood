import datetime

CURRENT_DATE = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
MENU = """Escolha uma das opções abaixo:\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> """
LIMITE_SAQUES = 3
MSG_ADVICE = f"Consulte seu gerente para mais informações.\n"

saldo = 0
limite = 500
numero_saque = 0
extrato = ""

def deposito(valor_dep):
    global extrato, saldo
    if valor_dep <= 0:
        print("Valor inválido. Tente novamente!\n")
    else:
        saldo += saldo+ valor_dep
        print("Depósito realizado com sucesso!\n")
        print(saldo)
        extrato += f"{CURRENT_DATE} R$ + {valor_dep:.2f}\n"
    return saldo

def saque(valor_saq):
    global saldo, extrato, numero_saque
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
        extrato += f"{CURRENT_DATE} R$ -{valor_saq:.2f}\n"
        print(f"Operação realizada com sucesso!\n")
    return

def extratos(extratos):
    if extratos == "":
        print("Não foram realizadas movimentações. ")
    else:
        print(f"Extrato consolidado:\n\n{extratos}\nSaldo total R$: {saldo:.2f}")
    return

print("Bem-vindo ao BTG Pactual!\n")
while True:
    opcao = input(MENU)
    match opcao:
        case "d":
            valor_dep = int(input(f"Informe o valor que deseja depositar R$: "))
            deposito(valor_dep)
        case "s":
            valor_saq = int(input(f"Informe o valor que deseja sacar R$: "))
            saque(valor_saq)
        case "e":
            extratos(extrato)
        case "q":
            print(f"O banco BTG agradece a sua parceria!\nVolte sempre!")
            break
        case other:
            print("Operação inválida, por favor selecione novamente a operação desejada.\n")