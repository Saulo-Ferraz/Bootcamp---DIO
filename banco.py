menu = """

[D] Depósito
[S] Saque
[E] Extrato
[X] Sair

=> """

saldo = 0
limiteSaque = 800
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Insira o valor a ser Depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso no valor de R${valor:.2f}")

        else:
            print("Operação falhou! Valor inválido")

    elif opcao == "S":
        valor = float(input("Insira o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limiteSaque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Indisponível! Você não tem saldo suficiente ,-,")

        elif excedeu_limite:
            print(f"Operação Indisponível! Você não pode sacar mais que {limiteSaque}")

        elif excedeu_saques:
            print("Operação Indisponível! Excedeu o limite de Saques para o dia")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso no valor de R${valor:.2f}")

        else:
            print("Operação Indisponível! Valor inválido")

    elif opcao == "E":
        print("\n================ SEU EXTRATO ================")
        print("Não há registros" if not extrato else extrato)
        print(f"\nSeu Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "X":
        break

    else:
        print("Operação Indisponível! por favor revise as opções.")