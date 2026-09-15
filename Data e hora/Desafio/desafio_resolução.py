import textwrap


def menu():
    menu = """\n
    =================== MENU ===================
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\t Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor: 2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ \Operação falhou! O valor informado é invalido. @@@")

    return saldo, extrato
        

   

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)


