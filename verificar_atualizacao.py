# Importando bibliotecas e funções necessárias para funcionamento do código
import time
from funcoes import obter_data, verificar_atualizacao, atualizar_arquivo, tentar_versao_anterior
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Adquirindo a data atual para controle de dados por mês

mes, ano = obter_data()

data = mes+ano

datav = ano+mes

chrome_options = webdriver.ChromeOptions()

prefs = {'download.default_directory' : '/Users/edilsonribeiro/PycharmProjects/TCC_Edilson/'}

chrome_options.add_experimental_option('prefs', prefs)

# Iniciando o WebDriver do Google Chrome

if verificar_atualizacao(datav) == True:
    print("Há possibilidade de uma nova versão de documento")
else:
    print("Versão desse mês já baixada")
    exit()

driver = webdriver.Chrome('/Users/edilsonribeiro/PycharmProjects/TCC_Edilson/chromedriver', options=chrome_options)

# Acessando o site na página de download do excel dos insumos


driver.get("https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_640")

driver.maximize_window()

print("Procurando arquivo...")

while verificar_atualizacao(datav) == True:

    try:

        arquivo = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((
                By.PARTIAL_LINK_TEXT, "SINAPI_ref_Insumos_Composicoes_AM_"+data+"_Desonerado")))

        arquivo.click()

        print("Aguardando download")

        time.sleep(20)

        print("Download concluído com a versão mais recente")

        atualizar_arquivo(datav)


    except:

        print('Ainda não há registros do mês ' + mes + ' '+ ano)

        mes, ano = tentar_versao_anterior(mes, ano)

        print('Verificando no mês anterior')

        datav = ano + mes

        data = mes + ano

    if verificar_atualizacao(datav) == False:
        print('A versão disponível é a mais recente')
        break

driver.quit()



