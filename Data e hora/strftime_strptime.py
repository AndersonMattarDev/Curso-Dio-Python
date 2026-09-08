from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2026-09-08 19:50'
mascara_pt_BR = '%d/%m/%Y %H:%M'
mascara_en = '%Y-%m-%d %H:%M'


print("Data e hora atual:", data_hora_atual.strftime(mascara_pt_BR))

data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(data_convertida)
print(type(data_convertida))