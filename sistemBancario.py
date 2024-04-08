menu = """

Digite { d } parara depositar .
Digite { s } para sacar . 
Digite { e } para ver seu exrato . 
Digite { q } para Sair .


    """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato = f"Depósito :R$ {valor:.2f}\n"
        else:
            print("Falha na operação, digite um valor válido para o depósito ser realizado!")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("O valor solicitado é maior que o limkte de saque.")
        elif excedeu_saques:
            print("Limite de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato = f"Saque : R$ {valor:.2f}\n"
            numero_saques += 1 
        else:
            print("Operação falhou!! o valor inormado é invalido.")
    elif opcao == "e":
        print("\n================EXTRATO=================")
        print("Não foi realizad nemhum operação. " if not extrato else extrato)
        print(f"\nSaldo : R$ {saldo:.2f}")
    elif opcao == "q": 
        break
    else:
        print("Opção invalida, por favor selecione uma opção valida.")
