import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [D]\tDepósito
    [S]\tSaque
    [E]\tExtrato
    [NC]\tCriar Nova Conta
    [LC]\tListar Contas
    [NU]\tCriar Novo Usuário
    [X]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print(f"\nDepósito realizado no valor de R${valor:.2f} !!!")
    else:
        print("\nO Depósito não pôde ser Realizado")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente para esta operação.")

    elif excedeu_limite:
        print("\nO Valor Limite de Saque foi ultrapassado, favor revisar")

    elif excedeu_saques:
        print("\nVocê não pode realizar mais saques Hoje ,-,")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque realizado no valor de R${valor:.2f} !!!")

    else:
        print("\nValor inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ SEU EXTRATO ================")
    print("Não há registros" if not extrato else extrato)
    print(f"\nSeu Saldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF Já Cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso !!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso !!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontado no sistema, operação encerrada")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 4
    AGENCIA = "0001"

    saldo = 0
    limite = 5000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Insira o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Insira o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "X":
            break

        else:
            print("Operação Indisponível! por favor revise as opções.")


main()  