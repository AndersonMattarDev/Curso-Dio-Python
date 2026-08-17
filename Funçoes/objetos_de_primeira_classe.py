def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a,b):
    return a*2 + b*3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")


exibir_resultado(10, 10, somar)  # Passando a função 'somar' como argumento
exibir_resultado(10, 10, subtrair)  # Passando a função 'subtrair' como argumento
exibir_resultado(10, 10, test)  # Passando a função 'test' como argumento

op = somar
print(op(1, 23))  # Chamando a função 'somar' através da variável 'op'