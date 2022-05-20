import pandas as pd

dados = pd.read_csv('dados.csv', sep=';', header=[0])

for i in range(len(dados)):
    print(dados['Simbolo'][i] + ' - ' + dados['Nome'][i])
    print('Número atômico: ' + str(dados['Numero'][i]))
    print('Série química: ' + dados['Serie quimica'][i])
    print('Grupo: ' + str(dados['Grupo'][i]))
    print('')
