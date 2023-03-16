import time
from zipfile import ZipFile
import pandas as pd
from funcoes import obter_versao, valores_itens, botao_atualizacao

pd.set_option('display.max_colwidth', None)

pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

versao = obter_versao()

arquivo = "SINAPI_ref_Insumos_Composicoes_AM_" + versao + "_Desonerado"

try:
    zip_file = ZipFile(arquivo + '.zip')

except FileNotFoundError:

    print("Buscando a versão mais recente")

    botao_atualizacao()

    print('Processando dados...')

    time.sleep(10)

    versao = obter_versao()

    arquivo = "SINAPI_ref_Insumos_Composicoes_AM_" + versao + "_Desonerado"

    zip_file = ZipFile(arquivo + '.zip')

df = pd.read_excel(zip_file.open('SINAPI_Preco_Ref_Insumos_AM_'+versao+'_Desonerado' + '.XLS'))

df.rename(columns={'        PRECOS DE INSUMOS':'CODIGO', 'Unnamed: 1':'DESCRICAO DO INSUMO', 'Unnamed: 2':'UNIDADE', 'Unnamed: 3':'ORIGEM DO PRECO', 'Unnamed: 4':'PRECO'}, inplace=True)

df = df.drop(1)

df = df.drop(2)

df = df.drop(3)

df = df.drop(4)

df = df.drop(5)

df = df.drop(6)

#nome = pd.DataFrame

