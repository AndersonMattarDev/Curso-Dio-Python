from datetime import date, datetime, time

data = date.today()
print(data)

data_hora = datetime.today()
print(data_hora)

# Usando .time() para extrair apenas a hora
hora = datetime.today().time()
print(hora)
