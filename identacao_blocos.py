def sacar(valor):

    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso!")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente.")


def depositar(valor):

    saldo = 500

    saldo += valor
    print("Depósito realizado com sucesso!")

sacar(1000)
depositar(500)