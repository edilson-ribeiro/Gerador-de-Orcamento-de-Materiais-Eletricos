import PySimpleGUI as sg
from ler_arquivo import df
from funcoes import valores_itens, botao_atualizacao, obter_versao, gerar_excel
import pandas as pd

print = sg.Print
versao = obter_versao()
itens = df[["DESCRICAO DO INSUMO"]]
lista_nome = []
lista_unidade = []
lista_valor = []
lista_quantidade = []

sg.theme('DarkGreen')

layout = [
            [sg.Text("Versão no banco de dados: " + versao)],
            [sg.Button('Verifique uma nova atualização'), ],
            [sg.InputText('Pesquise um item'), sg.Button('Pesquisar')],
            [sg.InputText('Escreva o índice de um item desejado*'), sg.Button('Ok')],
            [sg.InputText("Quantas unidades deseja adicionar?*"), sg.Button('Adicionar item no orçamento')],
            [sg.Button("Mostrar orçamento atual"), sg.Button("Limpar orçamento atual"), sg.InputText("Digite o nome do Orçamento*"), sg.Button('Gerar arquivo Excel do Orçamento')],
            [sg.Button('Encerrar')]
]

window = sg.Window('TCC Edilson Ribeiro', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Encerrar':

        break

    if event == 'Verifique uma nova atualização':

        botao_atualizacao()

    if event == 'Ok':

        try:

            print('Esses são os dados deste índice: \n')

            print(valores_itens(df, int(values[1])))

        except ValueError:

            print('Tente um número inteiro')

    if event == 'Pesquisar':

        try:

            df_result = df.loc[df['DESCRICAO DO INSUMO'].str.contains(values[0].upper(), na=False)]
            print(df_result.loc[:,'DESCRICAO DO INSUMO'])

        except ValueError:

            print('Tente novamente')

    if event == 'Adicionar item no orçamento':

        try:

            nome, unidade, valor = valores_itens(df, int(values[1]))

            quantidade = values[2]

            lista_nome.append(nome)

            lista_unidade.append(unidade)

            lista_valor.append(valor)

            lista_quantidade.append(quantidade)

        except ValueError:
            print('Adicione um valor de unidade')

    if event == 'Digite o nome do Orçamento':
        try:
            nome_arquivo = int(values[2])
        except NameError:
            print('Digite um nome válido')

    if event == 'Mostrar orçamento atual':
        print(lista_nome)

        print(lista_unidade)

        print(lista_valor)

        print(lista_quantidade)

    if event == "Limpar orçamento atual":
        lista_nome = []

        lista_unidade = []

        lista_valor = []

        lista_quantidade = []

    if event == 'Gerar arquivo Excel do Orçamento':

        if len(lista_nome) > 0:

            try:
               nome_arquivo = str(values[3])

               gerar_excel(pd, nome_arquivo, lista_nome, lista_unidade, lista_valor, lista_quantidade)

               print("Arquivo gerado com sucesso")

            except NameError or ValueError:
                print("Digite um nome válido")

        else:
            print("Preencha os dados obrigatórios")


window.close()

