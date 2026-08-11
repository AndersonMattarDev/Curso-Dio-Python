while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break  # Interrompe o laço quando a opção for igual a 10
    print(numero)


for numero in range(100):
    if numero == 10:
        break  # Interrompe o laço quando a opção for igual a 10, se eu usar o continue ele vai pular o 10 e continuar imprimindo os outros números
    print(numero, end=" ")