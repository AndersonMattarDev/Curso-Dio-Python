def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")#funciona mesmo sem passar os parametros por posicao, pois os parametros obrigatorios foram passados por posicao
#criar_carro(modelo="palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  #invalido