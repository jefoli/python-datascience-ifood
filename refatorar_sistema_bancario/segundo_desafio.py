
LIMITE_SAQUES = 3
MSG_ADVICE = f"Consulte seu gerente para mais informações.\n"
saldo = 0
limite = 500
numero_saque = 0
extrato = ""

# func deposito - v.01.
def deposito(valor_dep):
    global extrato,saldo

    if valor_dep <= 0:
        print("Valor inválido. Tente novamente!\n")
    else:
        extrato += f"00/07/23: R$ +{valor_dep:.2f}\n"
        saldo += valor_dep
    return saldo

def saque(numero_saque):
    global extrato, saldo

    if numero_saque > 2:
        print(f"\nLimite de operações excedidas para este tipo de conta!")
        print(f"Quantidades de saques disponíveis para essa conta: {LIMITE_SAQUES} (três).")
        print(MSG_ADVICE)
    elif valor_saq <= 0:
        print("Valor inválido!")
    elif valor_saq > limite:
        print(f"\nO valor informado excede o o limite disponível para essa conta!")
        print(f"Limite de valor por saque R$: {limite:.2f}!")
        print(MSG_ADVICE)
    elif valor_saq > saldo:
        print("Você não possui saldo suficiente para esta operação!\n")
    else:
        saldo = saldo - valor_saq
        numero_saque += 1
        extrato += f"00/07/23: R$ -{valor_saq:.2f}\n"
        print(f"Operação realizada com sucesso!\n")
    return saldo


print("Bem-vindo ao BTG Pactual!\n")
menu = """Escolha uma das opções abaixo:\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> """

while True:

    opcao = input(menu)
    if opcao == "d":
        
        valor_dep = int(input("Informe o valor que deseja depositar R$: "))
        func_dep = deposito(valor_dep)
        print("Depósito realizado com sucesso!\n")
        print(func_dep)
    elif opcao == "s":
        valor_saq = int(input("Informe o valor que deseja sacar R$: "))
        saque(valor_saq)

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações. ")
        else:
            print(f"Extrato consolidado:\n\n{extrato}")
            print(f"Saldo total R$: {saldo:.2f}")
    elif opcao == "q":
        print("O banco BTG agradece a sua parceria!\nVolte sempre!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")


