#texto = input ("Digite um texto: ")
texto = ""
VOGAIS = "AEIOU"


#Exemplo utilizando um iterável (string) com o laço for

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Adiciona uma nova linha após imprimir todas as vogais
    print("Executa no final do laço")  # Adiciona uma nova linha após imprimir todas as vogais



#Exemplo uttilizando a função built-in range() com o laço for
    for numero in range(0, 51, 5):
        print(numero, end=" ")

        