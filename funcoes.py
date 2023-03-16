import os
from datetime import date

import numpy as np


def obter_data():
    hoje = date.today()

    mes = hoje.strftime("%m")

    ano = hoje.strftime("%Y")

    return mes, ano


def verificar_atualizacao(datav):
    with open('/Users/edilsonribeiro/PycharmProjects/TCC_Edilson/lastupdate.txt', 'r') as f:

        linha = f.readline()

    if linha == datav:

        f.close()

        return False

    elif datav > linha:

        f.close()

        return True


def atualizar_arquivo(datav):
    with open('/Users/edilsonribeiro/PycharmProjects/TCC_Edilson/lastupdate.txt', 'w+') as f:
        f.write(datav)

        print("A nova referência é " + datav)

        f.close()


def tentar_versao_anterior(mes, ano):

    mes = int(mes)

    ano = int(ano)

    if mes != 1:

        mes = mes-1

        mes = str(mes)

        if len(mes) == 1:

            mes = '0'+mes

        ano = str(ano)

        return mes, ano

    else:

        ano = ano-1

        mes = 12

        mes = str(mes)

        ano = str(ano)

        return mes, ano


def obter_versao():
    with open('/Users/edilsonribeiro/PycharmProjects/TCC_Edilson/lastupdate.txt', 'r') as f:

        versao = f.readline()

        parte1 = versao[0:4]

        parte2 = versao[4:6]

        versao = parte2 + parte1

        return versao


def valores_itens(dataframe, id):
    nome = dataframe.values[id-6][1]
    unidade = dataframe.values[id-6][2]
    valor = dataframe.values[id-6][4]

    return nome, unidade, valor


def botao_atualizacao():
    os.system('python verificar_atualizacao.py')


def gerar_excel(pd, nome, lista1, lista2, lista3, lista4):

    nome_arquivo = pd.DataFrame()

    nome_arquivo['Item'] = lista1

    nome_arquivo['Unidade'] = lista2

    nome_arquivo['Preço'] = lista3

    nome_arquivo['Quantidade'] = lista4

    for i in range(len(lista3)):

        lista3[i] = lista3[i].replace(',', '.')

    i = len(lista3)

    nome_arquivo = nome_arquivo.replace(r'^\s*$', np.nan, regex=True)

    nome_arquivo.to_excel(str(nome)+'.xlsx', index = False)

    return 'Concluido'

