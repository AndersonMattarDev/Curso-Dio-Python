#if para criar uma estrutura condicional simples
#else para criar uma estrutura condicional alternativa
#elif para criar uma estrutura condicional alternativa com múltiplas condições

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade. Já pode tirar a sua carteira de motorista.")
elif idade >= 16:
    print("Você é adolescente. Se morasse nos Estados Unidos, poderia tirar a sua carteira de motorista com responsabilidade.")
else:
    print("Você é menor de idade. Que pena! Ainda não pode tirar a sua carteira de motorista.")