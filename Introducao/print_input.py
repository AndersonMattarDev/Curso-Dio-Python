nome = input("Informe o seu nome: ")
idade = input("informe a sua idade:")
print(f"Olá, {nome}! Você tem {idade} anos.")
print(nome, idade, end='... \n')  # O end='...' adiciona '...' ao final da linha, e o \n é para quebrar a linha depois.
print(nome, idade, sep='#')  # O sep=' - ' adiciona ' - ' entre os valores.